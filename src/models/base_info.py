from models.model import Model


class BaseInfo(Model):
    def __init__(self, school_code="", president="") -> None:
        self.__school_code: str = school_code
        self.__president: str = president

    @property
    def school_code(self) -> str:
        return self.__school_code

    @property
    def president(self) -> str:
        return self.__president
