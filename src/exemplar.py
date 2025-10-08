# src/exemplar.py

# ----------------------------------------------------------
# Classe principal do sistema de biblioteca (ME TDD)
# ----------------------------------------------------------
# Ela representa um exemplar físico de um livro.
# Cada exemplar tem:
#   - Um identificador único (idExemplar)
#   - Um status (aguardando, disponível, emprestado, etc.)
#   - Uma quantidade de empréstimos realizados
#
# O comportamento segue exatamente as regras do enunciado.
# ----------------------------------------------------------


# Criamos uma exceção personalizada para representar operações não permitidas.
# É o equivalente da "UnsupportedOperationException" do Java.
class UnsupportedOperationException(Exception):
    pass


# Outra exceção opcional (para simular o IllegalArgumentException do Java)
class IllegalArgumentException(Exception):
    pass


class Exemplar:
    # -----------------------------------------------
    # Construtor: define o estado inicial do exemplar
    # -----------------------------------------------
    def __init__(self, id_exemplar):
        # Atributo que identifica o exemplar (ex: 101, 102, etc.)
        self.id_exemplar = id_exemplar

        # O status inicial é sempre '0' (aguardando liberação)
        self.status = 0

        # Quantidade de vezes que o livro foi emprestado
        self.qtde_emprestimos = 0

    # -----------------------------------------------
    # Métodos "getters" (consultar os valores)
    # -----------------------------------------------

    def getStatus(self):
        """Retorna o status atual do exemplar"""
        return self.status

    def getQtdeEmprestimos(self):
        """Retorna a quantidade de empréstimos realizados"""
        return self.qtde_emprestimos

    # -----------------------------------------------
    # Métodos "setters" (usados só para os testes)
    # -----------------------------------------------
    # Esses métodos não existem no sistema real,
    # mas são necessários para criar cenários de teste.
    # -----------------------------------------------

    def setStatus(self, novo_status):
        """Define o status manualmente (para casos de teste)"""
        self.status = novo_status

    def setQtdeEmprestimos(self, quantidade):
        """Define a quantidade de empréstimos manualmente"""
        self.qtde_emprestimos = quantidade

    # -----------------------------------------------
    # Método principal: alterarStatus()
    # -----------------------------------------------
    # Esse método tenta alterar o status do exemplar,
    # respeitando todas as regras da tabela do enunciado.
    # -----------------------------------------------
    def alterarStatus(self, novo_status):
        # Se o exemplar estiver "perdido" (4) ou "descartado" (9),
        # nenhuma operação pode ser feita.
        if self.status in [4, 9]:
            raise UnsupportedOperationException(
                "Exemplar em status final não permite nenhuma operação"
            )

        # STATUS 0 (aguardando liberação)
        # Só pode mudar para 1 (disponível)
        if self.status == 0:
            if novo_status == 1:
                self.status = 1
                return True
            else:
                return False

        # STATUS 1 (disponível)
        # Pode mudar para 2 (reservado), 3 (emprestado), 5 (em restauração) ou 9 (descartado)
        if self.status == 1:
            if novo_status in [2, 3, 5, 9]:
                self.status = novo_status
                return True
            else:
                raise IllegalArgumentException("Novo status inválido para o status atual")

        # STATUS 2 (reservado)
        # Pode mudar para 1 (disponível) ou 3 (emprestado)
        if self.status == 2:
            if novo_status in [1, 3]:
                self.status = novo_status
                return True
            else:
                raise IllegalArgumentException("Novo status inválido para o status atual")

        # STATUS 3 (emprestado)
        # Pode mudar para 1 (disponível) ou 4 (perdido)
        if self.status == 3:
            if novo_status in [1, 4]:
                self.status = novo_status
                return True
            else:
                raise IllegalArgumentException("Novo status inválido para o status atual")

        # STATUS 5 (em restauração)
        # Pode mudar para 1 (disponível) ou 9 (descartado)
        if self.status == 5:
            if novo_status in [1, 9]:
                self.status = novo_status
                return True
            else:
                return False  # Aqui não lança exceção, apenas retorna False

        # Se não caiu em nenhum caso anterior, retorna False
        return False
