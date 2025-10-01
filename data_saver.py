from abc import ABC, abstractmethod

class DataSaver(ABC):
    @abstractmethod
    def save(self, data: dict, filename: str):
        pass