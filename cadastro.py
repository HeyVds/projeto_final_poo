from pessoa import Aluno, Professor
from disciplina import Disciplina
from persistencia import salvar_aluno, salvar_professor, salvar_disciplina
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

def cadastrar_disciplina(codigo, nome, professor):
    disciplina = Disciplina(codigo, nome, professor)
    salvar_disciplina(disciplina)
    return disciplina