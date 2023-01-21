from app.repository.bucket_repository import BucketRepository
from app.service.base_service import BaseService


class BucketService(BaseService):
    def __init__(self, bucket_repository: BucketRepository):
        self.bucket_repository = bucket_repository
        super().__init__(bucket_repository)
