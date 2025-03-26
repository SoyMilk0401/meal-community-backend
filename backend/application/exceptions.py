class BackendException(Exception): ...


class UserAlreadyExists(BackendException):
    def __init__(self, message: str = "User already exists."):
        super().__init__(message)


class UserNotFound(BackendException):
    def __init__(self, message: str = "User not found."):
        super().__init__(message)
