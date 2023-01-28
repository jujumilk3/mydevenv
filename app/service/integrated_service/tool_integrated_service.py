from app.service.tool_service import ToolService, ToolTagService, ToolToolRelationService, ToolTagRelationService


class ToolIntegratedService:
    def __init__(
        self,
        tool_service: ToolService,
        tool_tag_service: ToolTagService,
        tool_tool_relation_service: ToolToolRelationService,
        tool_tag_relation_service: ToolTagRelationService,
    ):
        self.tool_service = tool_service
        self.tool_tag_service = tool_tag_service
        self.tool_tool_relation_service = tool_tool_relation_service
        self.tool_tag_relation_service = tool_tag_relation_service
