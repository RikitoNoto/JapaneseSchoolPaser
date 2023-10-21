class BaseInfo:
    def __init__(self, school_code="", president="") -> None:
        self.__school_code: str = school_code
        self.__president: str = president

    @property
    def school_code(self):
        return self.__school_code

    @property
    def president(self):
        return self.__president
