from cadastro import *
from pessoa import *
from disciplina import *
from relatorio import *


def main():
    while True:
        inicializar_dados()
        print('\n=== Menu Principal ===')
        print('1 - Menu de Alunos')
        print('2 - Menu de Professores')
        print('3 - Menu de Disciplinas')
        print('4 - Menu de Relatórios')
        print('5 - Sair')
        opcao = input('\nEscolha uma opção: ')
        

        if opcao == '1':
            while True:
                print('\n🎓 Menu de Alunos')
                print('1 - Cadastrar novo aluno')
                print('2 - Listar alunos')
                print('3 - Buscar aluno por matrícula')
                print('4 - Matricular aluno em disciplina')
                print('5 - Adicionar nota')
                print('6 - Desmatricular disciplina')
                print('7 - Voltar')
                escolha = input('\nEscolha uma opção: ')

                if escolha =='1':
                    try:
                        nome = input('Nome do aluno: ')
                        cpf = input('CPF do aluno (apenas números): ')
                        nascimento = input('Data de nascimento (AAAA-MM-DD): ')
                        matricula = input('Matrícula do aluno: ')
                        aluno = Aluno(nome, cpf, datetime.datetime.strptime(nascimento, "%Y-%m-%d").date(), matricula)
                        salvar_aluno(aluno)
                        
                        print(f'Aluno {nome} cadastrado com sucesso!')
                    except ValueError as e:
                        print(f'Erro ao cadastrar aluno: {e}')

                elif escolha == '2':
                    if not alunos:
                        print("Não há alunos cadastrados.")
                        return
                    
                    print("\nLista de Alunos:")
                    for aluno in alunos:
                        print(aluno.exibir_dados()) 
                        print("-" * 30)

                elif escolha == '3':
                    matricula = input("Digite a matrícula do aluno que deseja buscar: ").strip()
                    for aluno in mapa_alunos.values():
                        if aluno.get_matricula() == matricula:
                            print("-" * 30)
                            print("\nAluno encontrado:\n")
                            print(aluno.exibir_dados())
                            print("-" * 30)
                            
                    print("\nAluno com matrícula", matricula, "não encontrado.")
                    
                elif escolha == '4':
                    matricula = input("Digite a matrícula do aluno que deseja matricular: ").strip()
                    codigo_disciplina = input("Digite o nome da disciplina: ").strip()
                    
                    aluno = next((a for a in mapa_alunos.values() if a.get_matricula() == matricula), None)
                    disciplina = next((d for d in disciplinas if d.codigo == codigo_disciplina), None)

                    if not aluno:
                        print(f"\nAluno com matrícula {matricula} não encontrado.")
                        
                    if not disciplina:
                        print(f"\nDisciplina com código {codigo_disciplina} não encontrada.")
                        

                    aluno.matricular_em_disciplina(disciplina)
                    salvar_aluno(aluno)
                    atualizar_disciplina(disciplina)
                    print(f"\nAluno {aluno.nome} matriculado na disciplina {disciplina.nome}.")

                elif escolha == '5':
                    matricula = input("Digite a matrícula do aluno: ").strip()
                    codigo_disciplina = input("Digite o nome da disciplina: ").strip()
                    nota = float(input("Digite a nota do aluno: ").strip())

                    aluno = next((a for a in mapa_alunos.values() if a.get_matricula() == matricula), None)
                    disciplina = next((d for d in disciplinas if d.codigo == codigo_disciplina), None)

                    if not aluno:
                        print(f"\nAluno com matrícula {matricula} não encontrado.")
                        return
                    if not disciplina:
                        print(f"\nDisciplina com código {codigo_disciplina} não encontrada.")
                        return

                    try:
                        aluno.adicionar_nota(disciplina.nome, nota)
                        salvar_aluno(aluno)
                        print(f"\nNota {nota} adicionada ao aluno {aluno.nome} na disciplina {disciplina.nome}.")
                        
                    except ValueError as e:
                        print(f"\nErro ao adicionar nota: {e}")
                elif escolha == '6':                        
                    cpf = input("Informe o CPF do aluno que deseja remover: ").strip()
                    nome_disciplina = (input("Digite o código da disciplina: "))
                    aluno = mapa_alunos.get(cpf)
                    if not aluno:
                        print(f"\nAluno com CPF {cpf} não encontrado.")
                        return None

                    disciplina = next((d for d in disciplinas if d.codigo == codigo_disciplina), None)
                    if not disciplina:
                        print(f"\nDisciplina '{nome_disciplina}' não encontrada.")
                        return None

                    if disciplina not in aluno.disciplinas:
                        print(f"\nAluno {aluno.nome} não está matriculado na disciplina {nome_disciplina}.")
                        return None

                    aluno.disciplinas.remove(disciplina)
                    atualizar_aluno(aluno)

                    disciplina.alunos_matriculados.remove(aluno)
                    atualizar_disciplina(disciplina)

                    print(f"Aluno {aluno.nome} desmatriculado da disciplina {nome_disciplina} com sucesso.")
                elif escolha == '7':
                    break
                else:
                    print('Escolha uma das opções.')

        elif opcao == '2':
            while True:
                print('\n🏫 Menu de Professores')
                print('1 - Cadastrar novo professor')
                print('2 - Listar professores')
                print('3 - Buscar professor por SIAPE')
                print('4 - Atribuir disciplina ao professor')
                print('5 - Remover disciplina do professor')
                print('6 - Voltar')
                escolha = input('\nEscolha uma opção: ')
                if escolha == '1':
                    nome = input("Nome do professor: ")
                    cpf = input("CPF do professor (somente números): ")
                    nascimento = input("Data de nascimento (aaaa-mm-dd): ")
                    siape = input("SIAPE do professor: ")
                    try:
                        professor = cadastrar_professor(nome, cpf, nascimento, siape)
                        print(f"Professor {professor.nome} cadastrado com sucesso!")
                    except ValueError as e:
                        print(f"Erro ao cadastrar professor: {e}")

                elif escolha == '2':
                    if not mapa_professores:
                        print("Nenhum professor cadastrado.")
                    else:
                        for professor in mapa_professores.values():
                            print(professor.exibir_dados())

                elif escolha == '3':
                    siape = input("Digite o SIAPE do professor que deseja buscar: ").strip()
                    for professor in mapa_professores.values():
                        if professor.get_siape() == siape:
                            print("Professor encontrado:")
                            print(professor.exibir_dados())
                            return
                    print("Professor não encontrado.")
               
                elif escolha == '4':
                    siape = input("Digite o SIAPE do professor: ").strip()
                    codigo_disciplina = input("Digite o código da disciplina: ").strip()
                    
                    professor = next((p for p in mapa_professores.values() if p.get_siape() == siape), None)
                    disciplina = mapa_disciplinas.get(codigo_disciplina)
                    
                    if not professor:
                        print(f"Professor com SIAPE {siape} não encontrado.")
                        return
                    if not disciplina:
                        print(f"Disciplina com código {codigo_disciplina} não encontrada.")
                        return
                    
                    professor.adicionar_disciplina(disciplina)
                    disciplina.professor_responsavel = professor
                    atualizar_professor(professor)
                    atualizar_disciplina(disciplina)
                    print(f"Disciplina {disciplina.nome} atribuída ao professor {professor.nome} com sucesso.")

                elif escolha == '5':
                    siape = input("Digite o SIAPE do professor: ")
                    codigo_disciplina = input("Digite o código da disciplina a ser removida: ")
                    remover_disciplina_do_professor(siape, codigo_disciplina)
                elif escolha == '6':
                    break
                else:
                    print('Escolha uma das opções.')

        elif opcao == '3':
            while True:
                print('\n📚 Menu de Disciplinas')
                print('1 - Criar nova disciplina')
                print('2 - Listar disciplinas')
                print('3 - Buscar disciplina por código')
                print('4 - Ver alunos matriculados na disciplina')
                print('5 - Voltar')
                escolha = input('\nEscolha uma opção: ')

                if escolha == '1':
                    codigo = input("Código da Disciplina: ")
                    nome_disciplina = input("Nome da Disciplina: ")
                    professor_nome = input("Nome do Professor Responsável: ")
                    professor = next((p for p in professores if p.nome == professor_nome), None)
                    if professor:
                        cadastrar_disciplina(codigo, nome_disciplina, professor)
                    else:
                        print(f"Professor com o nome '{professor_nome}' não encontrado.")

                elif escolha == '2':
                    if not disciplinas:
                        print("Não há disciplinas cadastradas.")
                        return

                    for disciplina in disciplinas:
                        print(disciplina.exibir_dados())
               
                elif escolha == '3':
                    codigo = input("Digite o código da disciplina que deseja buscar: ")
                    disciplina = next((d for d in disciplinas if d.codigo == codigo), None)
                    if disciplina:
                        print(f"Disciplina encontrada:\n{disciplina.exibir_dados()}")
                    else:
                        print(f"\nDisciplina com código {codigo} não encontrada.")
                
                elif escolha == '4':
                    print("Alunos matriculados nas disciplinas:")
                    for disciplina in disciplinas:
                        print(disciplina.exibir_dados()) 
               
                elif escolha == '5':
                    break
                else:
                    print('Escolha uma das opções.')

        elif opcao == '4':
            while True:
                print('\n📊 Menu de Relatórios')
                print('1 - Alunos aprovados')
                print('2 - Alunos reprovados')
                print('3 - Professores com muitos alunos')
                print('4 - Estatísticas gerais')
                print('5 - Voltar')
                escolha = input('\nEscolha uma opção: ')
                if escolha == '1':
                    relatorio_alunos_aprovados()
                elif escolha == '2':
                    relatorio_alunos_reprovados
                elif escolha == '3':
                    x = int(input("Informe o número mínimo de alunos: "))
                    relatorio_professores_com_mais_de_x_alunos(x)
         
                elif escolha == '4':
                    relatorio_estatisticas_gerais()
                elif escolha == '5':
                    break
                else:
                    print('Função ainda não implementada.')

        elif opcao == '5':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
