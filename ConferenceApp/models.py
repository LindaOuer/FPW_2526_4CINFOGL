from django.db import models
from UserApp.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Conference(models.Model):
    THEME_CHOICES = [
        ("AI","Artificial Intelligence"),
        ("ML","Machine Learning"),
        ("DS","Data Science"),
        ("WD","Web Development"),
        ("CY","Cybersecurity"),
    ]
    name = models.CharField(max_length=200, validators=[MinLengthValidator(5, "at least 5 characters required")])
    theme = models.CharField(max_length=200, choices=THEME_CHOICES)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(validators=[MinLengthValidator(20, "at least 20 characters required"), MaxLengthValidator(300, "at most 300 characters allowed")])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if self.end_date and self.start_date:
            if self.end_date < self.start_date:
                raise ValidationError("End date cannot be earlier than start date.")
    
class Submission(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    paper = models.FileField(upload_to='submissions/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    submission_date = models.DateTimeField(auto_now_add=True)
    keywords= models.CharField(max_length=200)
    payed=models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="pending")
    
class OrganizingCommittee(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    date_joined= models.DateTimeField(auto_now_add=True)
