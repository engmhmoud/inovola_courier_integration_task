from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

phone_number_validator = RegexValidator(
    regex=r'^[0-9]*$', message=_('Should only contain numbers'))


class UserManager(BaseUserManager):

    """
    class manager for providing a User(AbstractBaseUser) full control
    on this objects to create all types of User and this roles.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        pass data  to '_create_user' for creating normal_user .
        """
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        pass data to '_create_user' for creating super_user .
        """
        if email is None:
            raise TypeError("Users must have an email address.")
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    MALE, SHIPPER = 1, 1
    FEMALE, DELEGATE = 2, 2

    GENDER_CHOICES = [(MALE, "male"), (FEMALE, "female")]

    ROLE_CHOICES = [(SHIPPER, _("manager")), (DELEGATE, _("delegate"))]

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        default=SHIPPER,
        verbose_name=_("role"),
    )
    username = models.CharField(_("username"), max_length=50, unique=True, error_messages={
                                "unique": _("This user already registered.")})
    email = models.EmailField(_("email"), unique=True, error_messages={
                              "unique": _("This email already registered.")})
    phone = models.CharField(_("phone"), max_length=15, blank=True,
                             null=True, validators=[phone_number_validator])
    name = models.CharField(max_length=30, blank=True,
                            null=True, verbose_name=_("full_name"))
    address = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("address"))

    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=MALE, verbose_name=_("gender"))
    nationality_id_image = models.ImageField(
        upload_to="accounts/", blank=True, null=True, verbose_name=_("nationality ID image"))

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "phone", "address"]
    # customer data for delegate user only
    # if we need more custome data for manager or delegate we should seperate them into different models
    created_by = models.ForeignKey("User", verbose_name=_(
        "created_by"), on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.is_staff = True
        return super(User, self).save()


class Courier (models.Model):
    SHIPOX_NAME_CHOICE = "0"
    COURIER_NAME_CHOICES = [
        (SHIPOX_NAME_CHOICE, "SHIPOX"),

    ]
    user = models.OneToOneField(User)
    name = models.CharField(max_length=2, choices=COURIER_NAME_CHOICES)

    json, soap = "1", "2"
    email_password, token = '1', '2'
    TYPE = {
        (json, "JSON"),
        (soap, "SOAP"),
    }

    AUTH = {
        (email_password, 'EMAIL_PASSWORD'),
        (token, 'TOKEN'),
    }

    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255)
    password = models.CharField(_("Password"), max_length=255),
    api_type = models.CharField(_("Api Type"), max_length=5, choices=TYPE)
    auth_type = models.CharField(_("Auth Type"), max_length=20, choices=AUTH)
    domain = models.URLField(_("Domain"), max_length=200)


class Sender(models.Model):
    user = models.OneToOneField(User)


class Receiver(models.Model):
    user = models.OneToOneField(User)
