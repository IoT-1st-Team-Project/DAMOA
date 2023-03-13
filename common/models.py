from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# Create your models here.

class CustomUserManager(UserManager) :
    def create_user(self, username, name, password, email, age, ad):
        if not username :
            raise ValueError("아이디는 필수항목입니다.")
        
        if not name :
            raise ValueError("이름은 필수항목입니다.")
        
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email, age=age, ad=ad)
        user.set_password(password)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, name, password, email, age, ad):
        user = self.create_user(
            username=username,
            name=name,
            password=password,
            email=email,
            age=age,
            ad=ad,
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin) :
    email = models.EmailField(blank=True, unique=True, default='')
    username = models.CharField(max_length = 15, unique=True)
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    ad = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['name']

    class Meta :
        ordering = ['-date_joined']
        verbose_name = 'User'
        verbose_name_plural = 'User'