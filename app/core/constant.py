from enum import Enum


class ContentType(str, Enum):
    POST = "post"
    COMMENT = "comment"
    TOOL = "tool"

    def __str__(self):
        return str(self.value)


class CategoryGroup(str, Enum):
    TOOL = "tool"
    POST = "post"

    def __str__(self):
        return str(self.value)
