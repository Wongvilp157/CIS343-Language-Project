from expr import Expr, Visitor, Binary, Unary, Literal, Grouping, Logical, Postfix
from token_type import TokenType
from guava_token import Token


##---start AI code---
class AstPrinter(Visitor[str]):
    def print_expr(self, expr: Expr) -> str:
        return expr.accept(self)
##---end AI code---

    def visit_binary_expr(self, expr: 'Binary'):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: 'Grouping'):
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: 'Literal'):
        if expr.value == None: 
            return "null"
        return str(expr.value)

    def visit_unary_expr(self, expr: 'Unary'):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def visit_logical_expr(self, expr: 'Logical'):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    ##---start AI code---
    def visit_postfix_expr(self, expr: 'Postfix'):
        return self.parenthesize("post" + expr.operator.lexeme, expr.operand)
    ##---end AI code---

    ##---start AI code---
    def parenthesize(self, name: str, *exprs: 'Expr') -> str:
        # Replaces StringBuilder with a standard Python list of string fragments
        builder = [f"({name}"]
        
        for expr in exprs:
            builder.append(" ")
            # Passes 'self' as the visitor instance
            builder.append(expr.accept(self))
            
        builder.append(")")
        
        # Joins all array fragments into a single cohesive string output
        return "".join(builder)
    ##---end AI code---

##---start AI code---
def main():
    # Instantiate the syntax tree node for: -123 * (45.67)
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)
        ),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(
            Literal(45.67)
        )
    )

##---end AI code---

    printer = AstPrinter()
    print("initial example")
    print(printer.print_expr(expression))

if __name__ == "__main__":
    main()