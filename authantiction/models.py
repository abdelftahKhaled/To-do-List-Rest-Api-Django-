from django.db import models
import jwt

from helper.models import Trickingmodel
from django.contrib.auth.models import (AbstractBaseUser,UserManager,PermissionsMixin)
# Create your models here.
from django.apps import apps
from django.contrib.auth.hashers import make_password
from datetime import datetime ,timedelta
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import  gettext_lazy as _
class MyUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError("The given username must be set")
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        if username:
            GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
            )
            username = GlobalUserModel.normalize_username(username)
            user = self.model(username=username, email=email, **extra_fields)
        else:
            
         user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

        
    def create_superuser(self,  email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        username=None
        return self._create_user(username, email, password, **extra_fields)


    
class User(Trickingmodel,PermissionsMixin,AbstractBaseUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    # username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        # validators=[username_validator],
        # error_messages={
        #     "unique": _("A user with that username already exists."),
        # },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"),unique=True ,blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    @property
    def token(self):
    


        token=jwt.encode({'username':self.username
                          ,'email':self.email
                          ,'exp':datetime.utcnow() + timedelta(hours=24)}
                          , settings.SECRET_KEY
                          ,'HS256')
      
        return token
    
