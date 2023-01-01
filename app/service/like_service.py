from app.repository.like_repository import LikeRepository
from app.service.base_service import BaseService


class LikeService(BaseService):
    def __init__(self, like_repository: LikeRepository):
        self.like_repository = like_repository
        super().__init__(like_repository)
