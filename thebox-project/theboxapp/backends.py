from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.conf import settings
from .models import Account
from django.contrib.auth.hashers import check_password

from theboxapp.models import Account

class AccountBackend(ModelBackend):

    def authenticate(username, password):
        accounts = Account.objects.all() 
        for account in accounts:
            if account.user.username == username and account.password == password:
                return account.user, account.who
        
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None