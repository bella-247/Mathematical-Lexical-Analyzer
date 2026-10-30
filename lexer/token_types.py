from enum import Enum, auto

# auto automatically assigns unique numbers to each of the enum members

class TokenType(Enum):
    # Literals
    NUMBER = auto()

    # Identifiers
    IDENTIFIER = auto()

    # Arithmetic operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    POWER = auto()

    # Grouping symbols
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()

    # Comparison operators
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_THAN = auto()
    LESS_THAN = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()

    # Assignment
    ASSIGN = auto()

    # Separators
    COMMA = auto()

    # Special
    EOF = auto()
