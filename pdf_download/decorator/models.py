from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.
class UserAccountManager(BaseUserManager):
    def decoratoruser(self,email,username,password=None):
        if not email:
            raise ValueError('Email Field is Requires')
        if not username:
            raise ValueError('username field is required')
        if not password:
            raise ValueError('password field is required')
        user=self.model(email=email,
                        username=username)
        user.set_password(password)  # set_password is inbuilt function  to set passwrd programatically
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.decoratoruser(
            email=email,username=username,password=password
        )
        user.is_superuser=True  # superuser is permission to create,read,update and delete
        user.is_staff=True  # define a normal users fom admin  
        user.is_active=True   # define a active users
        user.save()
        return user 
    

    def create_student(self,email,username,password):
        user=self.decoratoruser(email=email,username=username,paswword=password)
        user.is_student=True
        user.save()
        return user
    def create_teacher(self,email,username,password):
        user=self.decoratoruser(email=email,username=username,password=password)
        user.is_teacher=True
        user.save()
        return user
    def create_principal(self,email,username,password):
        user=self.decoratoruser(email=email,username=username,password=password)
        user.save()
        return user
    
class UserAccount(AbstractBaseUser):
    username=models.CharField(max_length=60,null=False,unique=True)
    email=models.EmailField(null=False,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_principal=models.BooleanField(default=False)


    objects=UserAccountManager()
    USERNAME_FIELD="email"

    def __unicode__(self): #retrives data from database in string
        return str(self.username)
    

    def has_perm(self,perm,obj=None):   #has_perm return true if user has a specified permisiion when the perm in format "<app label>.<permisiioncodename>",,has_perm returns false if the is inactive
        return self.is_admin
    
    def has_module_perms(self,app_label):  # Returns True if the user has any permissions in the given package . If the user is inactive, this method will always return False. For an active superuser, this method will always return True.
        return True 


        