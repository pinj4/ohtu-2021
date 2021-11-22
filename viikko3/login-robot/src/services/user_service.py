from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        #user = self._user_repository.find_by_username(username)

        if self._user_repository.find_by_username(username) and password:
            raise UserInputError("Username already taken")

        if len(username) < 3 and password:
            raise UserInputError("Username too short")

        if username and len(password) < 8:
            raise UserInputError("Password too short")
        
        if username and password.isalpha():
            raise UserInputError("Password should contain both letters and numbers")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa