from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]+$',
    message='Name must contain only alphabetic characters.'
)

def validateEmail(value):
    allowed_domains=['esprit.tn', 'univ.tn', 'mit.edu']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Email domain must be one of the following: {", ".join(allowed_domains)}')
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES= [
        ("participant","Participant"),
        ("committee","Organizing Committee"),
        ("member","Member"),
    ]
    user_id=models.CharField(max_length=20, unique=True, primary_key=True)
    first_name=models.CharField(max_length=30, validators=[name_validator])
    last_name=models.CharField(max_length=30, validators=[name_validator])
    email=models.EmailField(unique=True, validators=[validateEmail])
    role=models.CharField(max_length=50, choices=ROLE_CHOICES)
    nationality=models.CharField(max_length=50)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)