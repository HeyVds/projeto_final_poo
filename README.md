# Projeto Final - Programação Orientada a Objetos

Este projeto é o trabalho final da disciplina de Programação Orientada a Objetos (POO), desenvolvido por Victor Mafra, Ricardo Junior e Denner Souza. O objetivo é implementar um sistema de gerenciamento acadêmico que permita o cadastro e gerenciamento de alunos, professores e disciplinas, com persistência de dados em arquivos `.txt`.

## Estrutura do Projeto

```
projeto_final_poo/
├── cadastro.py
├── disciplina.py
├── main.py
├── persistencia.py
├── pessoa.py
├── relatorio.py
├── dados/
│   ├── alunos.txt
│   ├── professores.txt
│   └── disciplinas.txt
└── Projeto Final.pdf
```

## Funcionalidades

- Cadastro de alunos, professores e disciplinas.
- Matrícula de alunos em disciplinas.
- Lançamento de notas para alunos.
- Geração de relatórios.
- Persistência de dados em arquivos `.txt`.
- Tratamento de exceções para:
  - Arquivos inexistentes.
  - Dados inválidos ou corrompidos.
  - Duplicidade de registros.
  - Matrícula em disciplina inexistente.
  - Inserção de nota em disciplina não cursada.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/HeyVds/projeto_final_poo.git
   cd projeto_final_poo
   ```

2. Certifique-se de que você possui o Python 3 instalado.

3. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

## Requisitos

- Python 3.x

## 👥 Contribuidores

- [HeyVds (Victor Mafra)](https://github.com/HeyVds)
- [Ricardo-junior-ps (Ricardo Junior)](https://github.com/Ricardo-junior-ps)
- [DSouza-29 (Denner Souza)](https://github.com/DSouza-29)
