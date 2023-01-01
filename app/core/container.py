from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.auth",
            "app.api.v1.endpoint.user",
            "app.core.dependency.authentication",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DB_URL)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    like_repository = providers.Factory(LikeRepository, session_factory=db.provided.session)
    tool_repository = providers.Factory(ToolRepository, session_factory=db.provided.session)
    comment_repository = providers.Factory(CommentRepository, session_factory=db.provided.session)
    category_repository = providers.Factory(CategoryRepository, session_factory=db.provided.session)
