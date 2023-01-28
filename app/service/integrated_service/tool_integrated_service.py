from app.service.tool_service import ToolService, ToolTagRelationService, ToolToolRelationService


class ToolIntegratedService:
    def __init__(
        self,
        tool_service: ToolService,
        tool_tool_relation_service: ToolToolRelationService,
        tool_tag_relation_service: ToolTagRelationService,
    ):
        self.tool_service = tool_service
        self.tool_tool_relation_service = tool_tool_relation_service
        self.tool_tag_relation_service = tool_tag_relation_service
