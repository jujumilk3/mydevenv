from app.model.tool import ToolDto
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

    async def get_tool_by_id(self, tool_id: int):
        return self.tool_service.get_by_id(tool_id)

    async def register_tool(self, tool_upsert: ToolDto.Upsert):
        None if not tool_upsert.tool_ids else await self.tool_service.get_by_ids(model_ids=tool_upsert.tool_ids)
        None if not tool_upsert.tag_ids else await self.tool_service.get_by_ids(model_ids=tool_upsert.tag_ids)
        tool = await self.tool_service.add(dto=tool_upsert)
        return tool
