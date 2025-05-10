from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = self._formatar_cpf(cpf)
        self.data_nascimento = data_nascimento

    @abstractmethod
    def exibir_dados(self):  # Método
        pass

    def get_cpf(self):  # Getter para acessar o CPF fora da classe
        return self.__cpf

    @staticmethod
    def _validar_cpf(cpf):
        # Validar o CPF ccom 11 dígitos
        return cpf.isdigit() and len(cpf) == 11

    @staticmethod
    def _formatar_cpf(cpf):  # Remover caracteres não númericos e formatar CPF
        cpf = ''.join(filter(str.isdigit, cpf))
        if Pessoa._validar_cpf(cpf):
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        else:
            raise ValueError("CPF inválido")


class Aluno(Pessoa):  # Classe Aluno que herda de pessoa
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []

    def get_matricula(self):
        return self.__matricula

    def adicionar_nota(self, nota):  # Adicionar notas a lista
        self.__notas.append(nota)

    def adicionar_disciplina(self, disciplina):  # Adicionar disciplina ao aluno
        self.disciplinas.append(disciplina)

    def exibir_dados(self):
        info = f"Aluno: {self.nome}, Matrícula: {self.__matricula}, Data Nasc.: {self.data_nascimento}"
        info += f"\n  CPF: {self.get_cpf()}"
        if self.__notas:
            info += f"\n  Notas: {', '.join(map(str, self.__notas))}"
        if self.disciplinas:
            info += "\n  Disciplinas:"
            for d in self.disciplinas:
                info += f"\n    - {d.nome} ({d.codigo})"
        return info
    
    def matricular_em_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_aluno(self)
        else:
            print(f"{self.nome} já está matriculado na disciplina {disciplina.nome}.")

    def adicionar_nota(self, disciplina_nome, nota):
        if not hasattr(self, "notas_por_disciplina"):
            self.notas_por_disciplina = {}

        if disciplina_nome not in [d.nome for d in self.disciplinas]:
            raise ValueError(f"Não é possível adicionar nota. O aluno não está matriculado na disciplina {disciplina_nome}.")

        self.notas_por_disciplina.setdefault(disciplina_nome, []).append(nota)


class Professor(Pessoa):  # Clase Professor que herda de pessoa
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []

    # Adicionar disciplina ao professor
    def adicionar_disciplina(self, disciplina):
            if disciplina not in self.disciplinas:
                self.disciplinas.append(disciplina)

    def exibir_dados(self):
        info = f"Professor: {self.nome}, SIAPE: {self.__siape}, Data Nasc.: {self.data_nascimento}"
        info += f"\n  CPF: {self.get_cpf()}"
        if self.disciplinas:
            info += "\n  Disciplinas:"
            for d in self.disciplinas:
                info += f"\n    - {d.nome} ({d.codigo})"
        return info
