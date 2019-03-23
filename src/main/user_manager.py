from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, commit=True,  **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)

        if commit:
            user.save(using=self._db)

        return user

    def create_user(self, email, password, commit=True, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, commit, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)
