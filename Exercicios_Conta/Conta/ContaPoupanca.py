from logging.config import valid_ident
from Conta import Conta


class ContaPoupanca(Conta):
  def __init__(self, agencia, conta, valor):
    super().__init__(agencia, conta, valor)