import os
import datetime
from pessoa import Aluno, Professor
from disciplina import Disciplina

pasta_dados = os.path.join(os.path.dirname(__file__), "dados")
arquivo_alunos = os.path.join(pasta_dados, "alunos.txt")
arquivo_professores = os.path.join(pasta_dados, "professores.txt")
arquivo_disciplinas = os.path.join(pasta_dados, "disciplinas.txt")

alunos = []
professores = []
disciplinas = []

mapa_alunos = {}
mapa_professores = {}
mapa_disciplinas = {}

def carregar_professores():
    try:
      with open(arquivo_professores, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
          dados = linha.strip().split("|")
          if len(dados) < 5:
              raise ValueError("Dados incompletos no arquivo de professores.")
          siape, nome, cpf, nascimento, lista_disciplinas = dados
          if cpf in mapa_professores:
              raise ValueError(f"Duplicidade de professor com CPF {cpf}")
          data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
          prof = Professor(nome, cpf, data_nasc, siape)
          mapa_professores[cpf] = prof
          professores.append(prof)
    except FileNotFoundError:
      print("Arquivo professores.txt não encontrado. Será criado ao salvar novos dados.")
    except Exception as e:
      print(f"Erro ao carregar professores: {e}")

def carregar_alunos():
  try:
    with open(arquivo_alunos, "r", encoding="utf-8") as arquivo:
      for linha in arquivo:
        dados = linha.strip().split("|")
        if len(dados) < 5:
          raise ValueError("Dados incompletos no arquivo de alunos.")
        nome, cpf, nascimento, matricula, *disciplinas_dados = dados
        if cpf in mapa_alunos:
          raise ValueError(f"Duplicidade de aluno com CPF {cpf}")
        data_nasc = datetime.datetime.strptime(nascimento, "%Y-%m-%d").date()
        aluno = Aluno(nome, cpf, data_nasc, matricula)
        for entrada in disciplinas_dados:
          partes = entrada.split(",")
          nome_disciplina = partes[0]
          notas = list(map(float, partes[1:]))
          if nome_disciplina not in mapa_disciplinas:
            print(f"Disciplina '{nome_disciplina}' não encontrada. Matrícula ignorada.")
            continue
          aluno.matricular_em_disciplina(mapa_disciplinas[nome_disciplina])
          for nota in notas:
            aluno.adicionar_nota(nome_disciplina, nota)
        mapa_alunos[cpf] = aluno
        alunos.append(aluno)
  except FileNotFoundError:
    print("Arquivo alunos.txt não encontrado. Será criado ao salvar novos dados.")
  except Exception as e:
    print(f"Erro ao carregar alunos: {e}")

def carregar_disciplinas():
  try:
    with open(arquivo_disciplinas, "r", encoding="utf-8") as arquivo:
      for linha in arquivo:
        dados = linha.strip().split("|")
        if len(dados) < 4:
          raise ValueError("Dados incompletos no arquivo de disciplinas.")
        cod, nome, nome_prof, lista_alunos = dados
        professor = next((p for p in professores if p.nome == nome_prof), None)
        if not professor:
          print(f"Professor '{nome_prof}' não encontrado para disciplina '{nome}'")
          continue
        disciplina = Disciplina(cod, nome, professor)
        professor.adicionar_disciplina(disciplina)
        mapa_disciplinas[nome] = disciplina
        disciplinas.append(disciplina)
        for nome_aluno in lista_alunos.split(","):
          aluno = next((a for a in alunos if a.nome == nome_aluno), None)
          if aluno:
            aluno.matricular_em_disciplina(disciplina)
            disciplina.adicionar_aluno(aluno)
  except FileNotFoundError:
    print("Arquivo disciplinas.txt não encontrado. Será criado ao salvar novos dados.")
  except Exception as e:
    print(f"Erro ao carregar disciplinas: {e}")

def salvar_professor(prof):
  try:
    with open(arquivo_professores, "a", encoding="utf-8") as arquivo:
      disciplinas_nomes = ",".join(d.nome for d in prof.disciplinas)
      linha = f"{prof.siape}|{prof.nome}|{prof.cpf}|{prof.data_nascimento}|{disciplinas_nomes}\n"
      arquivo.write(linha)
  finally:
    print(f"Professor {prof.nome} salvo.")

def salvar_aluno(aluno):
  try:
    with open(arquivo_alunos, "a", encoding="utf-8") as arquivo:
      dados_disciplinas = []
      for d in aluno.disciplinas:
        notas = aluno.notas_por_disciplina.get(d.nome, [])
        linha_disc = f"{d.nome}," + ",".join(map(str, notas))
        dados_disciplinas.append(linha_disc)
      linha = f"{aluno.nome}|{aluno.get_cpf()}|{aluno.data_nascimento}|{aluno.get_matricula()}|"
      arquivo.write(linha)
  finally:
    print(f"Aluno {aluno.nome} salvo.")

def salvar_disciplina(disc):
  try:
    with open(arquivo_disciplinas, "a", encoding="utf-8") as arquivo:
      nomes_alunos = ",".join(a.nome for a in disc.alunos_matriculados)
      linha = f"{disc.codigo}|{disc.nome}|{disc.professor_responsavel.nome}|{nomes_alunos}\n"
      arquivo.write(linha)
  finally:
      print(f"Disciplina {disc.nome} salva.")

def inicializar_dados():
    carregar_professores()
    carregar_disciplinas()
    carregar_alunos()
