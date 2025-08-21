from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository

from fastapi import HTTPException

# UserService → UserRepository (나쁜 의존성 방향)
# UserService → IUserRepository ← UserRepository (올바른 의존성 방향)
# 실제 구현체인 UserRepository는 IUserRepository라는 "약속"을 지켜서 만들어집니다.
# serService와 UserRepository는 분리되고, 나중에 UserRepository를 다른 데이터베이스 구현체(예: MongoUserRepository)로 바꾸고 싶을 때 UserService 코드는 단 한 줄도 바꿀 필요가 없게 됩니다. 이것이 의존성 역전의 힘입니다.
# 의존성 역전 원칙: 구체적인 구현체에 의존하지 말고, 추상적인 약속에 의존하라.
class UserService:
    def __init__(self):
        self.user_repo = IUserRepository = UserRepository() # 위배된 상황
        self.ulid = ULID()

    def create_user(self, name: str, email: str, password: str):
        _user = None

        try:
            _user = self.user_repo.find_by_email(email)
        except HTTPException as e:

        
        
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=password,
            created_at=now,
            updated_at=now
        )
        self.user_repo.save(user)


        return user
    