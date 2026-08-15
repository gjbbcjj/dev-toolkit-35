import re

class InputValidator:
    def __init__(self):
        self.patterns = {
            'username': re.compile(r'^[a-zA-Z0-9_]{3,15}$'),
            'email': re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$'),
            'password': re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
        }

    def validate_username(self, username):
        return bool(self.patterns['username'].match(username))

    def validate_email(self, email):
        return bool(self.patterns['email'].match(email))

    def validate_password(self, password):
        return bool(self.patterns['password'].match(password))

    def validate_all(self, username, email, password):
        return (self.validate_username(username) and
                self.validate_email(email) and
                self.validate_password(password))

# Usage Example:
# validator = InputValidator()
# print(validator.validate_all('user_123', 'user@example.com', 'password1'))  # True
