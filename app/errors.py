"""
different messages processing
was made in educational purposes
"""


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "NotWearingMaskError()") -> None:
        super().__init__(message)


class VaccineError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass
