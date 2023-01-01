from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository.like_repository import LikeRepository
from app.repository.tool_repository import ToolRepository
from app.repository.comment_repository import CommentRepository
from app.repository.category_repository import CategoryRepository
from app.repository.user_repository import UserRepository
from app.service.integrated_service.auth_service import AuthService
from app.service.category_service import CategoryService
from app.service.comment_service import CommentService
from app.service.like_service import LikeService
from app.service.tool_service import ToolService
from app.service.user_service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.auth",
            "app.api.v1.endpoint.user",
            "app.core.security",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DB_URL)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session_factory)
    like_repository = providers.Factory(LikeRepository, session_factory=db.provided.session_factory)
    tool_repository = providers.Factory(ToolRepository, session_factory=db.provided.session_factory)
    comment_repository = providers.Factory(CommentRepository, session_factory=db.provided.session_factory)
    category_repository = providers.Factory(CategoryRepository, session_factory=db.provided.session_factory)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    like_service = providers.Factory(LikeService, like_repository=like_repository)
    tool_service = providers.Factory(ToolService, tool_repository=tool_repository)
    comment_service = providers.Factory(CommentService, comment_repository=comment_repository)
    category_service = providers.Factory(CategoryService, category_repository=category_repository)
