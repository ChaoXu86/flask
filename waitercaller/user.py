class User:
    def __init__(self, email):
        self.email = email

    def get_id(self):
        return self.email

    def is_active(self):
        return True

    def is_anonymouse(self):
        return False

    def is_authenticated(self):
        return True

