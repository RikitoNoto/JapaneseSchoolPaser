class Major:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        pass

    @property
    def name(self) -> str:
        return self.__name


class GraduateSchool:
    def __init__(self, name: str, majors: list[Major]) -> None:
        self.__name: str = name
        self.__majors: list[Major] = majors

    @property
    def name(self) -> str:
        return self.__name

    @property
    def majors(self) -> list[Major]:
        return self.__majors
