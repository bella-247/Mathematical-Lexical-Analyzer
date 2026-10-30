from dataclasses import dataclass

from .token_types import TokenType

"""
@dataclass automatically generates useful methods such as __init__ and __repr__.

frozen=True makes tokens immutable after creation. Once recognized, a token should not accidentally change.
"""

@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    position: int



