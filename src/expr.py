from abc import ABC
from dataclasses import dataclass
from guava_token import Token
from typing import Any

from typing import TypeVar, Generic
from abc import ABC, abstractmethod

R = TypeVar('R')

class Visitor(ABC, Generic[R]):
    @abstractmethod
    def visit_binary_expr(self, expr: 'Binary') -> R:
        pass

    @abstractmethod
    def visit_grouping_expr(self, expr: 'Grouping') -> R:
        pass

    @abstractmethod
    def visit_literal_expr(self, expr: 'Literal') -> R:
        pass

    @abstractmethod
    def visit_unary_expr(self, expr: 'Unary') -> R:
        pass

    @abstractmethod
    def visit_logical_expr(self, expr: 'Logical') -> R:
        pass

    @abstractmethod
    def visit_postfix_expr(self, expr: 'Postfix') -> R:
        pass

## Expr is the class Node
class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor[R]') -> R:
        pass

@dataclass(frozen=True)
class Binary(Expr):
    left: 'Expr'
    operator: 'Token'
    right: 'Expr'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_binary_expr(self)

@dataclass(frozen=True)
class Grouping(Expr):
    expression: 'Expr'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_grouping_expr(self)

@dataclass(frozen=True)
class Literal(Expr):
    value: 'Any'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_literal_expr(self)

@dataclass(frozen=True)
class Unary(Expr):
    operator: 'Token'
    right: 'Expr'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_unary_expr(self)

@dataclass(frozen=True)
class Logical(Expr):
    left: 'Expr'
    operator: 'Token'
    right: 'Expr'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_logical_expr(self)

@dataclass(frozen=True)
class Postfix(Expr):
    operand: 'Expr'
    operator: 'Token'

    def accept(self, visitor: 'Visitor[R]') -> R:
        return visitor.visit_postfix_expr(self)

