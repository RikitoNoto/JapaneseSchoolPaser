class Departments:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        pass

    @property
    def name(self) -> str:
        return self.__name


class Faculty:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def departments(self) -> list[Departments]:
        return []
