from abc import ABC
from dataclasses import dataclass
from guava_token import Token

from typing import Any
class Expr(ABC):
  @dataclass(frozen=True)
  class Binary(Expr):
    left: 'Expr'
    operator: 'Token'
    right: 'Expr'

  @dataclass(frozen=True)
  class Grouping(Expr):
    expression: 'Expr'

  @dataclass(frozen=True)
  class Literal(Expr):
    value: 'Any'

  @dataclass(frozen=True)
  class Unary(Expr):
    operator: 'Token'
    right: 'Expr'

