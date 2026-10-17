from expr import Expr, Visitor

##---start AI code---
class AstPrinter(Visitor[str]):
    def print_expr(self, expr: Expr) -> str:
        return expr.accept(self)
##---end AI code---