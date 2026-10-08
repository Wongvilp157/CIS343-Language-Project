import sys
from scanner import Scanner
from error_handler import ErrorHandler

class Guava:
    def run(self, source):
        ErrorHandler.had_error = False
        for token in Scanner(source).scan_tokens():
            print(token)

    def run_file(self, path):
        with open(path, encoding="utf-8") as source_file:
            self.run(source_file.read())
            return 65 if ErrorHandler.had_error else 0
    
    def run_prompt(self):
        while True:
            try:
                source = input("> ")
            except (KeyboardInterrupt, EOFError):
                print()
                return 0
            self.run(source)

def main(): 
    num_arguments = len(sys.argv)
    guava = Guava()
    if num_arguments > 2:
        print("To use the interpreter, type: python src/lox.py [script]")
        print("Or just simply: python lox.py")
        return 64
    return guava.run_file(sys.argv[1]) if num_arguments == 2 else guava.run_prompt()

if __name__ == "__main__":
    sys.exit(main())


