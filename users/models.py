from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from dateutil.relativedelta import relativedelta
from django.utils import timezone
# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('É obrigatório um email válido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user



class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    createdat = models.DateTimeField(db_column='createdAt', auto_now_add=True, verbose_name='Criado em')
    updatedat = models.DateTimeField(db_column='updatedAt', auto_now=True, verbose_name='Atualizado em')
    phonenumber = models.CharField(db_column='phoneNumber', max_length=30, blank=True,null=True, verbose_name='Telefone')
    birthday = models.DateField(db_column='birthday', max_length=255, blank=True,null=True, verbose_name='Aniversário')
    CHOICES = (
        ('Mas', 'Masculino'),
        ('Fem', 'Feminino'),
    )
    gender = models.CharField(choices=CHOICES, max_length=255, blank=True,
                                 null=True)
    
    # SETA O CAMPO UTILIZADO NO LOGIN
    USERNAME_FIELD = 'email'
    # SETAR O CAMPOS OBRIGATÓRIOS: so add na array
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = UserAccountManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name
    
    def get_age(self):
        return relativedelta(timezone.now().date(), self.birthday).years

    def __str__(self):
        return self.email

    def can_see_obj(self, user):
        if self == user:
            return True
        else:
            return False
    
    def delete_user(self):

        self.delete()
        return True

        
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

