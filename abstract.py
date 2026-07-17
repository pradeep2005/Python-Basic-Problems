from abc import ABC, abstractmethod
class Featureplan(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
    
    def checkout(self):
        pass
class webapp(Featureplan):
    def login(self):
        print("Login to webapp")
    def logout(self):
        print("Logout from webapp")
app=webapp()
app.login()
app.logout()
app.checkout()
