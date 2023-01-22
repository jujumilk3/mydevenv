from typing import Any

from fastapi import HTTPException, status


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: dict[str, Any] | None = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class AuthError(HTTPException):
    def __init__(self, detail: Any = None, headers: dict[str, Any] | None = None) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class ForbiddenError(HTTPException):
    def __init__(self, detail: Any = None, headers: dict[str, Any] | None = None) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)


class NotFoundError(HTTPException):
    def __init__(self, detail: Any = None, headers: dict[str, Any] | None = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class ValidationError(HTTPException):
    def __init__(self, detail: Any = None, headers: dict[str, Any] | None = None) -> None:
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail, headers)
