from lexer.token import Token
from lexer.token_types import TokenType
from lexer.errors import LexicalError


class NumberRecognizer:

    @staticmethod
    def is_digit(char: str) -> bool:
        return "0" <= char <= "9"

    # for external usecase
    def can_start(self, char: str):
        return self.is_digit(char) or char == "."

    def recognize(self, source: str, start: int) -> tuple[Token, int]:

        if source[start] == ".":
            raise LexicalError("A number must start with at least one digit", start)

        position = start

        while position < len(source) and self.is_digit(source[position]):
            position += 1

        if position < len(source) and source[position] == ".":
            decimal_position = position
            position += 1

            # after decimal point require at least one digit
            if position >= len(source) or not self.is_digit(source[position]):
                raise LexicalError(
                    "A decimal point must be followed by at least one digit.",
                    decimal_position,
                )

            while position < len(source) and self.is_digit(source[position]):
                position += 1

            if position < len(source) and source[position] == ".":
                raise LexicalError(
                    "A number cannot contain multiple decimal points.", position
                )

        lexeme = source[start:position]
        token = Token(type=TokenType.NUMBER, lexeme=lexeme, position=start)

        return (token, position)
