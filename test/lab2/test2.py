##---start AI code---
import os
import sys

# Add the project's src/ folder (two levels up from test/lab2/) to the import path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from token_type import TokenType
from guava_token import Token
from expr import Expr, Visitor, Binary, Unary, Literal, Grouping, Logical, Postfix
from ast_printer import AstPrinter
##---end AI code---

def main():
    # Expression: 1 < 2 && 3 <= 4 || 5 > 6 && 7 >= 8 || !(True == False) && False != True
    expression_2 = Logical(
        Logical(
            Logical(
                Binary(Literal(1.0), Token(TokenType.LESS, "<", None, 1), Literal(2.0)),
                Token(TokenType.AND, "&&", None, 1),
                Binary(Literal(3.0), Token(TokenType.LESS_EQUAL, "<=", None, 1), Literal(4.0))
            ),
            Token(TokenType.OR, "||", None, 1),
            Logical(
                Binary(Literal(5.0), Token(TokenType.GREATER, ">", None, 1), Literal(6.0)),
                Token(TokenType.AND, "&&", None, 1),
                Binary(Literal(7.0), Token(TokenType.GREATER_EQUAL, ">=", None, 1), Literal(8.0))
            )
        ),
        Token(TokenType.OR, "||", None, 1),
        Logical(
            Unary(
                Token(TokenType.BANG, "!", None, 1),
                Grouping(
                    Binary(Literal(True), Token(TokenType.EQUAL_EQUAL, "==", None, 1), Literal(False))
                )
            ),
            Token(TokenType.AND, "&&", None, 1),
            Binary(Literal(False), Token(TokenType.BANG_EQUAL, "!=", None, 1), Literal(True))
        )
    )

    ##---start AI code---
    # Instantiate the printer and print the resulting string representation
    printer = AstPrinter()
    ##---end AI code---
    print("\nExample 2 (most literals and all comparisons and logic)")
    print(printer.print_expr(expression_2))

if __name__ == "__main__":
    main()