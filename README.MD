# 📚 TDD - Controle de Exemplar (Biblioteca)

Este projeto foi desenvolvido como parte da disciplina **Testes de Software**, 
com o objetivo de aplicar a prática de **Desenvolvimento Orientado a Testes (TDD)** 
na implementação da classe `Exemplar`, responsável por gerenciar o status 
de exemplares de livros em um sistema de biblioteca.

---

## 🎯 Objetivo

Implementar a classe `Exemplar` seguindo o modelo de negócios proposto, 
criando casos de teste automatizados com **Pytest** para validar as regras de transição de status.

---

## ⚙️ Regras de Negócio

Cada exemplar pode assumir diferentes **status**, com regras específicas de mudança:

| Status | Nome | Pode mudar para... |
|:------:|------|---------------------|
| 0 | Aguardando liberação | 1 |
| 1 | Disponível | 2, 3, 5, 9 |
| 2 | Reservado | 1, 3 |
| 3 | Emprestado | 1, 4 |
| 4 | Perdido | — |
| 5 | Em restauração | 1, 9 |
| 9 | Descartado | — |

Os status `4` (Perdido) e `9` (Descartado) são **finais**, ou seja, 
não permitem mais nenhuma operação.

---

## 🧩 Estrutura do Projeto
tdd_exemplar/
│
├── src/ # Código-fonte principal
│ ├── init.py
│ └── exemplar.py # Implementação da classe Exemplar
│
├── tests/ # Casos de teste automatizados
│ ├── init.py
│ └── test_exemplar.py # Casos CT029, CT030, CT031, CT032 e CT043
│
├── main.py # (Opcional) Execução manual de testes
├── README.md
└── requirements.txt


---

## 🧠 Descrição da Classe `Exemplar`

A classe `Exemplar` representa um exemplar físico de um livro na biblioteca.  
Ela possui os seguintes atributos:

| Atributo | Descrição |
|-----------|------------|
| `id_exemplar` | Identificador único do exemplar |
| `status` | Estado atual do exemplar |
| `qtde_emprestimos` | Quantidade de vezes que o exemplar foi emprestado |

E os principais métodos:

| Método | Função |
|:--------|:--------|
| `alterarStatus(novo_status)` | Altera o status do exemplar conforme as regras |
| `registrarEmprestimo()` | Registra um empréstimo, se permitido |
| `registrarDevolucao()` | Registra uma devolução, atualizando o status |
| `getStatus()` | Retorna o status atual |
| `getQtdeEmprestimos()` | Retorna o total de empréstimos realizados |

---

## 🧪 Casos de Teste Implementados

Os testes foram desenvolvidos com **pytest** e validam o comportamento do método `alterarStatus()`.

| Código | Descrição | Resultado Esperado |
|:-------|:-----------|:-------------------|
| **CT029** | Descartar exemplar em restauração (5 → 9) | ✅ True |
| **CT030** | Reservar exemplar aguardando liberação (0 → 2) | ❌ False |
| **CT031** | Emprestar exemplar aguardando liberação (0 → 3) | ❌ False |
| **CT032** | Marcar como perdido exemplar aguardando liberação (0 → 4) | ❌ False |
| **CT043** | Reservar exemplar em restauração (5 → 2) | ❌ False |

---

🚀 Como Executar o Projeto
### 1️⃣ Instale o Python (3.10 ou superior)
Verifique com:
```bash
python --version

2️⃣ Instale as dependências
Crie o arquivo requirements.txt com:
pytest
E rode:
pip install -r requirements.txt

3️⃣ Execute os testes
Na pasta raiz do projeto:
pytest -v
Você deverá ver uma saída semelhante a:
test_exemplar.py::test_CT029_descartar_em_restauracao PASSED
test_exemplar.py::test_CT030_reservar_aguardando_liberacao PASSED
test_exemplar.py::test_CT031_emprestar_aguardando_liberacao PASSED
test_exemplar.py::test_CT032_perdido_aguardando_liberacao PASSED
test_exemplar.py::test_CT043_reservar_em_restauracao PASSED

Aviso: Caso o comando acima não funcionar lembre-se de instalar o pytest devidamente com: python -m pip install pytest e depois (na clase test_exemplar.py) use o comando: python -m pytest -v

🧰 Execução Manual (Opcional)
Você pode testar o comportamento do código manualmente rodando:
    python main.py
Saída esperada:
=== Simulador de Biblioteca ===
    Status inicial: 0 (aguardando liberação)
    -> Alterando status para 1 (disponível)...
    Mudança bem-sucedida? True
    Status atual: 1
    -> Tentando alterar status de 1 (disponível) para 4 (perdido)...
    Erro: Novo status inválido para o status atual
    Status final: 1 ## 

🧱 Tecnologias Utilizadas
Python 3.10+
Pytest
Prática de TDD (Test-Driven Development)

📅 Desenvolvido em Outubro de 2025.
