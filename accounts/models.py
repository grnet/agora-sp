from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from owner.models import Institution, ServiceOwner

class User(AbstractBaseUser, PermissionsMixin):


    # Avoid forgotten usernames and simplify authentication
    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=255, default=None, blank=True)
    last_name = models.CharField(max_length=255, default=None, blank=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(unique=True)

    # A regular user does not have to be related to an Institution probably...
    id_institution = models.ForeignKey(Institution,  blank=True, null=True)

    # A regular user does not have to be a Service owner...
    id_owner = models.ForeignKey(ServiceOwner, blank=True, null=True)

    is_active = models.BooleanField(default=False)

    # Is the user a manager?
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name +" "+self.last_name

    def get_short_name(self):
        return self.email

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user