# tests/test_exemplar.py

# ----------------------------------------------------------
# Testes automatizados da classe Exemplar (TDD)
# ----------------------------------------------------------
# Aqui vamos implementar os casos:
#   CT029, CT030, CT031, CT032 e CT043
#
# Esses testes verificam o comportamento do método alterarStatus()
# de acordo com as regras do enunciado.
# ----------------------------------------------------------

import pytest
# Importamos a classe e as exceções do arquivo exemplar.py
from src.exemplar import Exemplar, UnsupportedOperationException, IllegalArgumentException


# ----------------------------------------------------------
# CT029 - Descartar um exemplar que está em restauração
# ----------------------------------------------------------
def test_CT029_descartar_em_restauracao():
    # Criamos um exemplar com ID 1
    ex = Exemplar(1)

    # Definimos o status inicial como 5 (em restauração)
    ex.setStatus(5)

    # Tentamos mudar o status para 9 (descartado)
    resultado = ex.alterarStatus(9)

    # A mudança é válida (de 5 → 9 pode)
    assert resultado is True

    # E o status final deve ser 9
    assert ex.getStatus() == 9


# ----------------------------------------------------------
# CT030 - Reservar um exemplar que esteja aguardando liberação
# ----------------------------------------------------------
def test_CT030_reservar_aguardando_liberacao():
    ex = Exemplar(2)

    # Status 0 (aguardando liberação)
    ex.setStatus(0)

    # Tentamos mudar para 2 (reservado)
    resultado = ex.alterarStatus(2)

    # De 0 → 2 NÃO pode, então o retorno deve ser False
    assert resultado is False

    # E o status permanece o mesmo (0)
    assert ex.getStatus() == 0


# ----------------------------------------------------------
# CT031 - Emprestar um exemplar que esteja aguardando liberação
# ----------------------------------------------------------
def test_CT031_emprestar_aguardando_liberacao():
    ex = Exemplar(3)

    # Status 0 (aguardando liberação)
    ex.setStatus(0)

    # Tentamos mudar para 3 (emprestado)
    resultado = ex.alterarStatus(3)

    # Essa transição também não é permitida (0 → 3 é inválido)
    assert resultado is False

    # O status deve continuar sendo 0
    assert ex.getStatus() == 0


# ----------------------------------------------------------
# CT032 - Colocar como perdido um exemplar que está aguardando liberação
# ----------------------------------------------------------
def test_CT032_perdido_aguardando_liberacao():
    ex = Exemplar(4)

    # Status inicial: 0 (aguardando liberação)
    ex.setStatus(0)

    # Tentamos mudar para 4 (perdido)
    resultado = ex.alterarStatus(4)

    # Também é inválido — de 0 só pode ir para 1
    assert resultado is False

    # O status não deve mudar
    assert ex.getStatus() == 0


# ----------------------------------------------------------
# CT043 - Reservar um exemplar que está em restauração
# ----------------------------------------------------------
def test_CT043_reservar_em_restauracao():
    ex = Exemplar(5)

    # Status inicial: 5 (em restauração)
    ex.setStatus(5)

    # Tentamos mudar para 2 (reservado)
    resultado = ex.alterarStatus(2)

    # De 5 só pode mudar para 1 ou 9 — então deve ser inválido
    assert resultado is False

    # O status deve continuar sendo 5
    assert ex.getStatus() == 5
