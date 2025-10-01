class Student:
    def __init__(self, full_name: str, group_number: str):
        self.__full_name = full_name
        self.__group_number = group_number

    def get_full_name(self):
        return self.__full_name

    def get_group_number(self):
        return self.__group_number