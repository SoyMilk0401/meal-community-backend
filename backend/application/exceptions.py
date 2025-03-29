class BackendException(Exception): ...


class UserAlreadyExists(BackendException):
    def __init__(self, message: str = "User already exists."):
        super().__init__(message)


class UserNotFound(BackendException):
    def __init__(self, message: str = "User not found."):
        super().__init__(message)


class IncorrectEmailOrPassword(BackendException):
    def __init__(self, message: str = "Incorrect email or password."):
        super().__init__(message)


class PrefixNotBearer(BackendException):
    def __init__(self, message: str = "Prefix not Bearer."):
        super().__init__(message)


class NeedAuth(BackendException):
    def __init__(self, message: str = "Need auth."):
        super().__init__(message)
