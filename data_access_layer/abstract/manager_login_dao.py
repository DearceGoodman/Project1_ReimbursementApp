from abc import ABC, abstractmethod


class ManagerLoginDAO(ABC):
    @abstractmethod
    def get_manager_login_by_credentials(self, username: str, password: str):
        pass
