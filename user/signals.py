from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import timezone
from .models import CustomUser

def generate_user_id(user_type):

    current_year = timezone.now().strftime('%Y')

    prefix_map ={
        'student' : 'STU',
        'teacher' : 'TRE',
        'admin' : 'ADM',
    }

    prefix = prefix_map.get(user_type, 'USE')

    last_user = (CustomUser.objects.filter(user_type = user_type, user_id__startswith = f"{prefix}{current_year}")
                 .order_by('-user_id').first())
    
    if last_user :
        last_sequence = int(last_user.user_id[-4:])
        new_sequence = last_sequence + 1
    else:
        new_sequence = 1

    return f"{prefix}{current_year}{new_sequence:04d}"


@receiver(pre_save, sender=CustomUser)
def User_id_Signal(sender, instance, **kwargs):
    if not instance.user_id and instance.user_type:
        instance.user_id = generate_user_id(instance.user_type)

    if not instance.username:
        instance.username = instance.user_id

    if instance._state.adding and not instance.password:
        instance.set_password("welcome@123")
