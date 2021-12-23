from abc import ABC, abstractmethod


class ManagerLoginService(ABC):
    @abstractmethod
    def validate_manager_login(self, username, password):
        pass
