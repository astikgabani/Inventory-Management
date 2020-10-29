from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class EmployeeType(models.Choices):

    INVENTORY_MANAGER = "Inventory Manager"
    QUALITY_CHECK_PERSON = "Quality Check Person"
    SALES_MANAGER = "Sales Manager"
    IT_ADMIN = "IT Admin"


class EmployeeManager(BaseUserManager):

    def create_user(self, email, name, password=None, *args, **kwargs):
        """
        Creating a new user
        """
        if not email:
            raise ValueError("Email should be specified.")
        employee_type = {'type': kwargs.get('type') or EmployeeType.INVENTORY_MANAGER}
        kwargs.update(employee_type)
        email = self.normalize_email(email)
        employee = self.model(email=email, name=name, *args, **kwargs)
        if employee.type == EmployeeType.IT_ADMIN:
            employee.is_superuser = True
            employee.is_staff = True
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, email, name, password, *args, **kwargs):
        """
        Create a admin user
        """
        kwargs.update({'type': EmployeeType.IT_ADMIN})
        employee = self.create_user(email, name, password, *args, **kwargs)
        employee.is_superuser = True
        employee.is_staff = True
        employee.save(using=self._db)
        return employee


class EmployeeModel(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model created for managing the user
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    type = models.CharField(max_length=120, choices=EmployeeType.choices, default=EmployeeType.INVENTORY_MANAGER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = EmployeeManager()

    def __repr__(self):
        return f"<EmployeeModel {self.email}>"
