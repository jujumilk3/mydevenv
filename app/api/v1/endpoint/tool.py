from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.core.container import Container
from app.core.dependency import get_current_user_token_no_exception
from app.model.tool import ToolDto
from app.service.integrated_service.tool_integrated_service import ToolIntegratedService

router = APIRouter(
    prefix="/tool",
    tags=["tool"],
)


@router.get("/{tool_id}", response_model=ToolDto.WithAdditionalInfo, status_code=status.HTTP_200_OK)
@inject
async def get_tool(
    tool_id: int,
    *,
    tool_integrated_service: ToolIntegratedService = Depends(Provide[Container.tool_integrated_service]),
    user_token: str = Depends(get_current_user_token_no_exception),
):
    return await tool_integrated_service.get_tool_by_id_with_tools_tags(tool_id=tool_id)
