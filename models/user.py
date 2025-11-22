class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # In real system, this would be hashed
        self.email = email

class UserManager:
    def __init__(self):
        self.users = {}
    
    def register_user(self, username, password, email):
        self.users[username] = User(username, password, email)
    
    def validate_user(self, username, password):
        if username in self.users:
            return self.users[username].password == password
        return False

class LoginSystem:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.current_user = None
    
    def login(self, username, password):
        if self.user_manager.validate_user(username, password):
            self.current_user = username
            return True
        return False
    
    def logout(self):
        self.current_user = None
    
    def is_logged_in(self):
        return self.current_user is not None
    
    def get_current_user(self):
        return self.current_user