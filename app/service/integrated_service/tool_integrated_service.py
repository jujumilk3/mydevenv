from app.model.tool import ToolDto
from app.service.tag_service import TagService
from app.service.tool_service import ToolService, ToolTagRelationService, ToolToolRelationService


class ToolIntegratedService:
    def __init__(
        self,
        tag_service: TagService,
        tool_service: ToolService,
        tool_tool_relation_service: ToolToolRelationService,
        tool_tag_relation_service: ToolTagRelationService,
    ):
        self.tag_service = tag_service
        self.tool_service = tool_service
        self.tool_tool_relation_service = tool_tool_relation_service
        self.tool_tag_relation_service = tool_tag_relation_service

    async def get_tool_by_id(self, tool_id: int):
        return self.tool_service.get_by_id(tool_id)

    async def get_tool_by_id_with_tools_tags(self, tool_id: int):
        tool = await self.tool_service.get_by_id(tool_id)
        tools = await self.tool_tool_relation_service.get_reference_tools_by_source_tool_id(source_tool_id=tool_id)
        tags = await self.tool_tag_relation_service.get_tags_by_tool_id(tool_id=tool_id)
        tool_with_tool_tag = ToolDto.WithAdditionalInfo(
            **tool.dict(),
            tools=tools,
            tags=tags,
        )
        return tool_with_tool_tag

    async def create_tool(self, tool_upsert: ToolDto.Upsert):
        tools = (
            None if not tool_upsert.tool_names else await self.tool_service.get_by_names(names=tool_upsert.tool_names)
        )
        tags = None if not tool_upsert.tag_names else await self.tag_service.get_by_names(names=tool_upsert.tag_names)
        tool_ids = [tool.id for tool in tools] if tools else []
        tag_ids = [tag.id for tag in tags] if tags else []
        created_tool = await self.tool_service.add(dto=tool_upsert)
        if len(tool_ids) > 0:
            for tool_id in tool_ids:
                await self.tool_tool_relation_service.create_with_source_tool_id_reference_tool_id(
                    source_tool_id=created_tool.id, reference_tool_id=tool_id
                )
        if len(tag_ids) > 0:
            for tag_id in tag_ids:
                await self.tool_tag_relation_service.create_with_tool_id_tag_id(tool_id=created_tool.id, tag_id=tag_id)
        tool_with_tool_tag = ToolDto.WithAdditionalInfo(
            **created_tool.dict(),
            tools=tools,
            tags=tags,
        )
        return tool_with_tool_tag

    async def patch_tool_by_id(self, tool_id: int, tool_upsert: ToolDto.Upsert):
        tool_names = tool_upsert.pop("tool_names")
        tag_names = tool_upsert.pop("tag_names")
        tools = tool_names if tool_names is None else await self.tool_service.get_by_names(names=tool_names)
        tags = tag_names if tag_names is None else await self.tag_service.get_by_names(names=tag_names)
        tool_ids = [tool.id for tool in tools] if tools else []
        tag_ids = [tag.id for tag in tags] if tags else []
        patched_tool = await self.tool_service.patch_by_id(model_id=tool_id, dto=tool_upsert)
        await self.renew_tool_by_tool_id(source_tool_id=tool_id, reference_tool_ids=tool_ids)
        await self.renew_tags_by_tool_id(tool_id=tool_id, tag_ids=tag_ids)
        tool_with_tool_tag = ToolDto.WithAdditionalInfo(
            **patched_tool.dict(),
            tools=tools,
            tags=tags,
        )
        return tool_with_tool_tag

    async def renew_tool_by_tool_id(self, source_tool_id: int, reference_tool_ids: list[int]):
        already_related_tools = await self.tool_tool_relation_service.get_reference_tool_ids_by_source_tool_id(
            source_tool_id=source_tool_id
        )
        already_related_tool_ids = [tool.reference_tool_id for tool in already_related_tools]
        for tool_id in already_related_tool_ids:
            if tool_id not in reference_tool_ids:
                await self.tool_tool_relation_service.remove_by_source_tool_id_reference_tool_id(
                    source_tool_id=source_tool_id, reference_tool_id=tool_id
                )
        for tool_id in reference_tool_ids:
            if tool_id not in already_related_tool_ids:
                await self.tool_tool_relation_service.create_with_source_tool_id_reference_tool_id(
                    source_tool_id=tool_id, reference_tool_id=tool_id
                )

    async def renew_tags_by_tool_id(self, tool_id: int, tag_ids: list):
        already_related_tag = await self.tool_tag_relation_service.get_tag_ids_by_tool_id(tool_id=tool_id)
        already_related_tag_ids = [tag.tag_id for tag in already_related_tag]
        for tag_id in already_related_tag_ids:
            if tag_id not in tag_ids:
                await self.tool_tag_relation_service.remove_by_tool_id_tag_id(tool_id=tool_id, tag_id=tag_id)
        for tag_id in tag_ids:
            if tag_id not in already_related_tag_ids:
                await self.tool_tag_relation_service.create_with_tool_id_tag_id(tool_id=tool_id, tag_id=tag_id)

    async def remove_tool_by_id(self, tool_id: int):
        return await self.tool_service.remove_by_id(model_id=tool_id)
