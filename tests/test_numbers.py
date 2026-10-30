import pytest

from lexer.lexer import Lexer
from lexer.errors import LexicalError
from lexer.token_types import TokenType


@pytest.mark.parametrize(
    "source, expected",
    [
        ("123", "123"),
        ("0", "0"),
        ("007", "007"),
        ("3.14", "3.14"),
        ("0.25", "0.25"),
        ("100.001", "100.001"),
    ],
)
def test_valid_numbers(source, expected):
    tokens = Lexer(source).tokenize()

    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].lexeme == expected
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize(
    "source",
    [
        ".5",
        "12.",
        "12.3.4",
        "0.",
        "1..2",
    ],
)
def test_invalid_numbers(source):
    with pytest.raises(LexicalError):
        Lexer(source).tokenize()


def test_whitespace_between_numbers():
    tokens = Lexer("12  34").tokenize()

    assert [token.lexeme for token in tokens] == ["12", "34", ""]
