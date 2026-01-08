from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('student' , 'student'),
        ('teacher' , 'teacher'),
        ('admin' , 'admin')
    )
    
    id = models.UUIDField(default=uuid4, primary_key=True, null=False, blank=False, unique=True, editable=False)
    user_type = models.CharField(max_length=20,choices=USER_TYPE, default='student')
    phone = models.CharField(max_length=20, null=True, blank=True)
    user_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user_id} - {self.get_full_name()} )"
    
    def generate_user_id(user_type, instance):

        current_year = timezone.now().strftime('%y')

        prefix = {
            'student' : 'STU',
                                                                                                                                                        
        }

    





