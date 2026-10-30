from .token import Token
from .token_types import TokenType
from .errors import LexicalError
from .recognizers.number import NumberRecognizer


class Lexer:

    def __init__(self, source: str):
        self.source = source
        self.position = 0

        self.recognizers = [NumberRecognizer()]

    def tokenize(self) -> list[Token]:
        tokens = []

        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isspace():
                self.position += 1
                continue

            possible_recognizers = (
                item for item in self.recognizers if item.can_start(current)
            )
            recognizer = next(possible_recognizers, None)

            # check if none of recognizers can recognize the current character
            if recognizer is None:
                raise LexicalError(
                    f"No recognizer available for {current!r}.", self.position
                )

            # recognize one token
            token, next_position = recognizer.recognize(self.source, self.position)

            if next_position <= self.position:
                raise RuntimeError("Recognizer did not advance the cursor.")

            tokens.append(token)
            self.position = next_position

        tokens.append(Token(type=TokenType.EOF, lexeme="", position=len(self.source)))

        return tokens