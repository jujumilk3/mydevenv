from app.repository.tool_repository import ToolRepository
from app.service.base_service import BaseService


class ToolService(BaseService):
    def __init__(self, tool_repository: ToolRepository):
        self.tool_repository = tool_repository
        super().__init__(tool_repository)
