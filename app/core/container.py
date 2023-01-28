from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository.bucket_repository import BucketRepository
from app.repository.category_repository import CategoryRepository
from app.repository.comment_repository import CommentRepository
from app.repository.like_repository import LikeRepository
from app.repository.tag_repository import TagRepository
from app.repository.tool_repository import ToolRepository, ToolTagRelationRepository, ToolToolRelationRepository
from app.repository.user_repository import UserRepository
from app.service.auth_service import AuthService
from app.service.bucket_service import BucketService
from app.service.category_service import CategoryService
from app.service.comment_service import CommentService
from app.service.integrated_service.tool_integrated_service import ToolIntegratedService
from app.service.like_service import LikeService
from app.service.tag_service import TagService
from app.service.tool_service import ToolService, ToolTagRelationService, ToolToolRelationService
from app.service.user_service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.admin",
            "app.api.v1.endpoint.auth",
            "app.api.v1.endpoint.bucket",
            "app.api.v1.endpoint.tag",
            "app.api.v1.endpoint.user",
            "app.core.security",
            "app.core.dependency",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DB_URL, sync_db_url=configs.SYNC_DB_URL)

    # Base repositories
    bucket_repository = providers.Factory(BucketRepository, session_factory=db.provided.session_factory)
    category_repository = providers.Factory(CategoryRepository, session_factory=db.provided.session_factory)
    comment_repository = providers.Factory(CommentRepository, session_factory=db.provided.session_factory)
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session_factory)
    like_repository = providers.Factory(LikeRepository, session_factory=db.provided.session_factory)
    tag_repository = providers.Factory(TagRepository, session_factory=db.provided.session_factory)
    tool_repository = providers.Factory(ToolRepository, session_factory=db.provided.session_factory)
    tool_tool_relation_repository = providers.Factory(
        ToolToolRelationRepository, session_factory=db.provided.session_factory
    )
    tool_tag_relation_repository = providers.Factory(
        ToolTagRelationRepository, session_factory=db.provided.session_factory
    )

    # Base service
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    bucket_service = providers.Factory(BucketService, bucket_repository=bucket_repository)
    category_service = providers.Factory(CategoryService, category_repository=category_repository)
    comment_service = providers.Factory(CommentService, comment_repository=comment_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    like_service = providers.Factory(LikeService, like_repository=like_repository)
    tag_service = providers.Factory(TagService, tag_repository=tag_repository)
    tool_service = providers.Factory(ToolService, tool_repository=tool_repository)
    tool_tool_relation_service = providers.Factory(
        ToolToolRelationService, tool_tool_relation_repository=tool_tool_relation_repository
    )
    tool_tag_relation_service = providers.Factory(
        ToolTagRelationService, tool_tag_relation_repository=tool_tag_relation_repository
    )

    # Integrated Service
    tool_integrated_service = providers.Factory(
        ToolIntegratedService,
        tag_service=tag_service,
        tool_service=tool_service,
        tool_tool_relation_service=tool_tool_relation_service,
        tool_tag_relation_service=tool_tag_relation_service,
    )
