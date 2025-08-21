from abc import ABCMeta, abstractmethod
from user.domain.user import User

# 이 인터페이스의 실제 구현체는 인프라 계층에 존재한다. (인터페이스여서 I를 앞에 붙였다.)
# 도메인 계층에 존재하는 이 모듈은 어느 계층에서나 사용할 수 있으며, 인프라 계층보다 고수준의 계층에서 사용할 때는 그 의존성이 역전되어 있다.
class IUserRepository(metaclass=ABCMeta):

    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError # 구현이 필요함을 기술한다.
