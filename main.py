from persistencia import inicializar_dados, alunos, professores, disciplinas

inicializar_dados()

print("\n=== Professores Carregados ===")
for p in professores:
    print("\n",p.exibir_dados())

print("\n=== Alunos Carregados ===")
for a in alunos:
    print("\n",a.exibir_dados())

print("\n=== Disciplinas Carregadas ===")
for d in disciplinas:
    print("\n",d.exibir_dados())

from cadastro import cadastrar_aluno


#teste cadastro
def menu():
    print("1 - Cadastrar aluno")
    opcao = input("Escolha: ")
    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        matricula = input("Matrícula: ")
        aluno = cadastrar_aluno(nome, cpf, nascimento, matricula)
        print(f"Aluno {aluno.nome} cadastrado com sucesso!")

menu()