from abc import ABC, abstractmethod


class LoginService(ABC):
    @abstractmethod
    def validate_login(self, username, password):
        pass
