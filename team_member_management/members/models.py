from django.db import models
from django.core.validators import RegexValidator

# Create TeamMember model.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    ]

    phone_number_regex = RegexValidator(
        regex=r'^\+?\d+(-\d+)*$',
        message="Enter the correct phone number."
    )
    
    first_name = models.CharField("First Name", max_length=100, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=100, blank=False, null=False)
    phone_number = models.CharField("Phone Number", max_length=15, blank=False, null=False, validators=[phone_number_regex])
    email = models.EmailField("Email", max_length=200, unique=True, blank=False, null=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
