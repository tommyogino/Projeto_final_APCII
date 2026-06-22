# Sistema Acadêmico — Projeto Final APC II

Trabalho final da matéria de Algoritmos e Programação de Computadores II.
Sistema de gerenciamento acadêmico em Python com menu interativo no terminal.

## Funcionalidades

- Cadastro de alunos com matrícula gerada automaticamente
- Listagem de alunos formatada
- Busca por nome (linear) e por matrícula (binária)
- Ordenação por nome (alfabética) ou por média (decrescente)
- Cadastro de notas por disciplina (matriz de notas)
- Cálculo de média individual e média geral da turma
- Relatório geral
- Persistência de dados em arquivo JSON

## Estrutura do Projeto

```
projeto_final/
├── main.py         # Menu principal e loop de interação com o usuário
├── aluno.py        # Criação e listagem de alunos
├── notas.py        # Matriz de notas, cadastro e cálculo de médias
├── busca.py        # Busca linear (nome) e binária (matrícula)
├── ordenacao.py    # Ordenação por nome e por média (bubble sort)
└── utils.py        # Utilitários: validação, persistência JSON, UI helpers

testes/
├── testes_aluno.py
├── testes_notas.py
├── testes_busca.py
├── testes_ordenacao.py
├── testes_utils.py
└── testes_main.py
```

## Como executar

**1. Criar e ativar o ambiente virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate.fish   # fish shell
# ou
source .venv/bin/activate        # bash/zsh
```

**2. Instalar dependências:**
```bash
pip install -r requirements.txt
```

**3. Rodar o sistema:**
```bash
python3 projeto_final/main.py
```

## Como rodar os testes

```bash
pytest -v
```

Os testes usam `pytest` com `pythonpath = projeto_final` (configurado em `pytest.ini`).

## Requisitos Técnicos Atendidos

- Listas e matrizes (matriz de notas: linha = aluno, coluna = disciplina)
- Funções modulares separadas por responsabilidade
- Busca linear e busca binária
- Ordenação implementada manualmente (bubble sort)
- Código modular em múltiplos arquivos
