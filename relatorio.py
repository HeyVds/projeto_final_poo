from persistencia import *
from persistencia import professores, inicializar_dados

def relatorio_alunos_aprovados():
    print("\n\\\\\\Alunos Aprovados//////")
    for aluno in alunos:
        for disciplina in aluno.disciplinas:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3: 
                media = notas[2] 
                if media >= 7:
                    print(f"Aluno: {aluno.nome}\nDisciplina: {disciplina.nome}\nMédia: {media}\n")


def relatorio_alunos_reprovados():
    print("\n\\\\\Alunos Reprovados//////")
    for aluno in alunos:
        for disciplina in aluno.disciplinas:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3: 
                media = notas[2] 
                if media < 7:
                    print(f"Aluno: {aluno.nome}\nDisciplina: {disciplina.nome}\nMédia: {media}\n")

def relatorio_professores_com_mais_de_x_alunos(x):
    
    print(f"\\\\Professores com mais de {x} alunos//////")
    for professor in professores:
        total_alunos = sum(len(disciplina.alunos_matriculados) for disciplina in professor.disciplinas)
        if total_alunos > x:
            print(f"Professor: {professor.nome} | Total de Alunos: {total_alunos}")

def relatorio_estatisticas_gerais():
    total_alunos = len(alunos)
    total_professores = len(professores)
    total_disciplinas = len(disciplinas)

    print("-"*30)
    print("\nEstatísticas Gerais:")
    print(f"Número total de alunos: {total_alunos}")
    print(f"Número total de professores: {total_professores}")
    print(f"Número total de disciplinas: {total_disciplinas}")

    print("\nMédia Geral de Notas por Disciplina:")
    for disciplina in disciplinas:
        notas_totais = []
        for aluno in disciplina.alunos_matriculados:
            notas = aluno.notas_por_disciplina.get(disciplina.nome, [])
            if len(notas) >= 3:  
                notas_totais.append(notas[2]) 
        if notas_totais:
            media_disciplina = sum(notas_totais) / len(notas_totais)
            print(f"Disciplina: {disciplina.nome} | Média Geral: {media_disciplina:.2f}")
            print("-"*30)

def gerar_relatorios():
    inicializar_dados()
    relatorio_alunos_aprovados()
    relatorio_alunos_reprovados()  
    relatorio_estatisticas_gerais()


