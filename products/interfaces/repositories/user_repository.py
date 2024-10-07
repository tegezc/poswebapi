from domain.models import User

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()
