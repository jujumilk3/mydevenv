from app.repository.tool_repository import ToolRepository
from app.service.base_service import BaseService


class ToolService(BaseService):
    def __init__(self, tool_repository: ToolRepository):
        self.tool_repository = tool_repository
        super().__init__(tool_repository)


class ToolToolRelationService(BaseService):
    def __init__(self, tool_tool_relation_repository: ToolRepository):
        self.tool_tool_relation_repository = tool_tool_relation_repository
        super().__init__(tool_tool_relation_repository)


class ToolTagRelationService(BaseService):
    def __init__(self, tool_tag_relation_repository: ToolRepository):
        self.tool_tag_relation_repository = tool_tag_relation_repository
        super().__init__(tool_tag_relation_repository)
