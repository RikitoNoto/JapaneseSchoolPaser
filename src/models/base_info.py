from models.model import Model


class BaseInfo(Model):
    def __init__(self, name="", school_code="", president="") -> None:
        self.__name = name
        self.__school_code: str = school_code
        self.__president: str = president

    @property
    def name(self) -> str:
        return self.__name

    @property
    def school_code(self) -> str:
        return self.__school_code

    @property
    def president(self) -> str:
        return self.__president
