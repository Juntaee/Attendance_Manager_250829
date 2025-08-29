from abc import ABC, abstractmethod

# abstract interface
class Grade(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def determine(self, point: int) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
