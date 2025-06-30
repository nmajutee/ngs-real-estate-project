from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('agent', 'Agent'),
        ('tenant', 'Tenant'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return self.username
    
class AgentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='agent_profile')
    agency_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    # Add more agent-specific fields as needed

    def __str__(self):
        return f"{self.user.username} - {self.agency_name}"