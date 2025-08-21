from dataclasses import dataclass
from datetime import datetime

@dataclass
class Profile: # 데이터만 가지고 있는 도메인 객체를 값 객체라고 한다. (Value Object, VO)
    name: str
    email: str

# 프로필을 별도의 도메인으로 분리했다고 해서, 데이터베이스도 분리하여 Profile 테이블을 만들 필요는 없다.
# User 테이블에 모든 데이터를 포함하고, 데이터베이스에서 데이터를 불러와서 도메인 객체를 만들 때, Profile 도메인 객체와 User 도메인 객체로 만들 수도 있다.
@dataclass
class User:
    id: str
    profile: Profile
    password: str
    created_at: datetime
    updated_at: datetime
