import abc


CorpusReprType = dict[str, int]


class BaseTokenizer(abc.ABC):
    """
    Base class for all tokenizers
    """

    vocab_amount: int
    all_sentences: list[str]

    @abc.abstractmethod
    def encode(self, text: str) -> list[int]:
        """
        text -> vector
        """

    @abc.abstractmethod
    def decode(self, vector: list[int]) -> str:
        """
        vector -> text
        """
