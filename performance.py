from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects: list[str], grades: list[float]):
        self.__subjects = subjects
        self.__grades = grades

    def get_subjects(self):
        return self.__subjects

    def get_grades(self):
        return self.__grades

    @abstractmethod
    def average_grade(self):
        pass