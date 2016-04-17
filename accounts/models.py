from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from owner.models import Institution, ServiceOwner




class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email, password, **kwargs):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):


    # Avoid forgotten usernames and simplify authentication
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    username = models.CharField(max_length=50, default=None, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(unique=True)

    # A regular user does not have to be related to an Institution probably...
    id_institution = models.ForeignKey(Institution,  blank=True, null=True, default=None,)

    # A regular user does not have to be a Service owner...
    id_owner = models.ForeignKey(ServiceOwner, blank=True, null=True, default=None)

    is_active = models.BooleanField(default=False)

    # Is the user a manager?
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def get_full_name(self):
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        return self.email
