from models.model import Model


class Department(Model):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        pass

    @property
    def name(self) -> str:
        return self.__name


class Faculty(Model):
    def __init__(self, name: str, departments: list[Department]) -> None:
        self.__name: str = name
        self.__departments: list[Department] = departments

    @property
    def name(self) -> str:
        return self.__name

    @property
    def departments(self) -> list[Department]:
        return self.__departments
