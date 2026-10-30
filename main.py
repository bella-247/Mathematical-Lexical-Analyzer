from lexer.lexer import Lexer
from lexer.errors import LexicalError

def main():
    expression = input("Enter expression: ")
    lexer = Lexer(expression)

    try:
        tokens = lexer.tokenize()

        for token in tokens:
            print(
                f"{token.type.name: <15}",
                f"lexeme={token.lexeme!r:<12}",
                f"position={token.position}"
            )
    except LexicalError as error:
        print(error)


if __name__ == "__main__":
    main()

    