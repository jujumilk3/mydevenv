from typing import Any, Optional

from fastapi import HTTPException
from starlette import status


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class NotFoundError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)
