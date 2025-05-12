from pessoa import Aluno, Professor
from disciplina import Disciplina
from persistencia import *
import datetime

def cadastrar_aluno(nome, cpf, nascimento, matricula):
    data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
    aluno = Aluno(nome, cpf, data_nasc, matricula)
    salvar_aluno(aluno)
    return aluno

def cadastrar_professor(nome, cpf, nascimento, siape):
    data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
    professor = Professor(nome, cpf, data_nasc, siape)
    salvar_professor(professor)
    return professor

def cadastrar_disciplina(codigo=0, nome="padrão", professor="padrão"):
    disciplina = Disciplina(codigo, nome, professor)
    salvar_disciplina(disciplina)
    return disciplina


def desmatricular_aluno(cpf, disciplina_nome):
    aluno = next((a for a in alunos if a.get_cpf() == cpf), None)
    if not aluno:
        print(f"Aluno com CPF {cpf} não encontrado.")
        return None

    disciplina = next((d for d in disciplinas if d.nome == disciplina_nome), None)
    if not disciplina:
        print(f"Disciplina {disciplina_nome} não encontrada.")
        return None

    if disciplina not in aluno.disciplinas:
        print(f"Aluno {aluno.nome} não está matriculado na disciplina {disciplina_nome}.")
        return None

    aluno.disciplinas.remove(disciplina)
    disciplina.alunos_matriculados.remove(aluno)
    atualizar_aluno(aluno)
    atualizar_disciplina(disciplina)

    print(f"Aluno {aluno.nome} desmatriculado da disciplina {disciplina_nome} com sucesso.")

def salvar_todos_alunos():
    try:
        with open(arquivo_alunos, "w", encoding="utf-8") as arquivo:
            for aluno in alunos:

                linha = f"{aluno.nome}|{aluno.get_cpf()}|{aluno.data_nascimento}|{aluno.get_matricula()}|"
                

                dados_disciplinas = []
                for d in aluno.disciplinas:
                    notas = aluno.notas_por_disciplina.get(d.nome, [])
                    linha_disc = f"{d.nome}," + ",".join(map(str, notas))
                    dados_disciplinas.append(linha_disc)
                
                if dados_disciplinas:
                    linha += "|".join(dados_disciplinas)

                linha += "\n"
            
                arquivo.write(linha)
                
    finally:
        print("Todos os alunos foram salvos.")

def remover_disciplina_do_professor(professor_siape, codigo_disciplina):
    professor = next((p for p in professores if p.get_siape() == professor_siape), None)
    if not professor:
        print(f"Professor com SIAPE {professor_siape} não encontrado.")
        return None

    disciplina = next((d for d in professor.disciplinas if d.codigo == codigo_disciplina), None)
    if not disciplina:
        print(f"Disciplina com código {codigo_disciplina} não encontrada para o professor {professor.nome}.")
        return None

    professor.disciplinas.remove(disciplina)

    disciplina.professor_responsavel = None

    atualizar_professor(professor)
    atualizar_disciplina(disciplina)

    print(f"Disciplina {disciplina.nome} removida do professor {professor.nome} com sucesso.")