import sys
class Lox:
    

    def main(): 
        num_arguments = len(sys.argv)
        if num_arguments > 2:
            print("To use the interpreter, type: python src/lox.py [script]")
            print("Or just simply: python lox.py")
            return 64
        elif num_arguments == 2:
            
        if num_arguments == 1:
            try:
                while True:
                    REPL_mode = input()
                    print("Scanner Not Implemented")
            except KeyboardInterrupt:
                print("Exiting REPL mode")


