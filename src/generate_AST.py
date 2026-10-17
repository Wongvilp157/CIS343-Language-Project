import sys
import os

def main():
    ##---start AI code---
    # sys.argv includes the script name itself, 
    # so len(sys.argv) == 2 means exactly 1 argument was passed.
    if len(sys.argv) != 2:
        print("Usage: generate_ast <output directory>", file=sys.stderr)
        sys.exit(64)
        
    output_dir = sys.argv[1]
    
    # You can call your upcoming AST generation functions here
    # define_ast(output_dir, "Expr", [...])
    define_ast(output_dir, "Expr", [
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right"
    ##---end AI code---
    ])

##---start AI code---
def define_ast(output_dir: str, base_name: str, types: list[str]):
    # Use os.path.join to securely handle file paths across operating systems
    # Python files should be lowercase by convention (e.g., expr.py)
    path = os.path.join(output_dir, f"{base_name.lower()}.py")
    
    # Python's 'with' block automatically safely closes the file when finished
    with open(path, "w", encoding="utf-8") as writer:
        # Writing Python imports and base class architecture
        writer.write("from abc import ABC\n")
        writer.write("from dataclasses import dataclass\n")
        writer.write("from guava_token import Token\n")  
        writer.write("from typing import Any\n\n") # Required for 'Object value' mapping
        
        # Define the main abstract base class
        writer.write(f"class {base_name}(ABC):\n")
##---end AI code---

        define_visitor(writer, base_name, types)
    
        for type in types:
            type_parts = type.split(":")
            class_name = type_parts[0].strip()
            fields = type_parts[1].strip()
            define_type(writer, base_name, class_name, fields)

        ##---start AI code---
        writer.write("\n")
        writer.write("    @abstractmethod\n")
        writer.write("    def accept(self, visitor: 'Visitor[R]') -> R:\n")
        writer.write("        pass\n\n")
        ##---end AI code---

def define_type(writer, base_name, class_name, fields):
    writer.write("  @dataclass(frozen=True)\n")
    writer.write(f"  class {class_name}({base_name}):\n")

    fields = fields.split(", ")
    for field in fields:
        variable = field.strip().split(" ")
        type_name = variable[0]
        field_name = variable[1]
        
        if type_name == "Object":
            type_name = "Any"
            
            
        writer.write(f"    {field_name}: '{type_name}'\n")

    ##---start AI code---
    writer.write("\n")
    writer.write("    def accept(self, visitor: 'Visitor[R]') -> R:\n")
    # Converts 'visitBinaryExpr(this)' to 'visit_binary_expr(self)'
    writer.write(f"        return visitor.visit_{class_name.lower()}_{base_name.lower()}(self)\n")
    ##---end AI code--

    
    writer.write("\n")

def define_visitor(writer, base_name, types):
    ##---start AI code---
        # 1. Define the Visitor interface with a generic type variable 'R'
    writer.write("from typing import TypeVar, Generic\n")
    writer.write("from abc import ABC, abstractmethod\n\n")
    writer.write("R = TypeVar('R')\n\n")
    
    writer.write(f"class Visitor(ABC, Generic[R]):\n")

    # 2. Generate the abstract visitor methods for each expression type
    for type_str in types:
        type_name = type_str.split(":")[0].strip()
        
        # Python uses snake_case for variable names by convention (e.g., base_name.lower())
        param_name = base_name.lower()
        
        writer.write("    @abstractmethod\n")
        writer.write(f"    def visit_{type_name.lower()}_{param_name}(self, {param_name}: '{type_name}') -> R:\n")
        writer.write("        pass\n\n")
    ##---end AI code---

    for type in types:
        type_name = type.split(":")[0].strip()


if __name__ == "__main__":
    main()