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
    # Expression: "guava" != null
    expression_3 = Binary(
        Literal("guava"),
        Token(TokenType.BANG_EQUAL, "!=", None, 1),
        Literal(None)
    )

    ##---start AI code---
    # Instantiate the printer and print the resulting string representation
    printer = AstPrinter()
    ##---end AI code---
    print("\nExample 3 (The rest of the literals (strings and Null)")
    print(printer.print_expr(expression_3))

if __name__ == "__main__":
    main()