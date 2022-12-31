from enum import Enum

class ContentType(str, Enum):
    POST = "post"
    COMMENT = "comment"
    TOOL = "tool"
