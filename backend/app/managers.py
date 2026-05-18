from django.contrib.auth.models import BaseUserManager
class UserProfileManager(BaseUserManager):
    
    
    def create_user(self, email, phone, name, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user