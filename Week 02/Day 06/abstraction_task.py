from abc import ABC, abstractmethod

class BankingApp(ABC):
    @abstractmethod
    def database(self):
        print("Connect to database successfully")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankingApp):
    def login_app(self):
        print("Login to Banking App Successful")

    def security(self):
        print("Security of Mobile App")

    def database(self):
        print("Database connection in Mobile App")

if __name__ == "__main__":
    bank = MobileApp()  # Create an instance of MobileApp (as it inherits from BankingApp)
    bank.database()     # Output: Database connection in Mobile App
    bank.login_app()    # Output: Login to Banking App Successful
    bank.security()     # Output: Security of Mobile App
