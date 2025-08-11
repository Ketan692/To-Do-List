from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import uuid
import traceback

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            UserProfile.objects.create(user=instance, email_token=email_token)
            email = instance.email
            print(f"Sending verification email to {email} with token {email_token}")
            subject = "Your account needs to be verified"
            email_from = settings.EMAIL_HOST_USER
            message = (
    f"Dear {instance.first_name},\n\n"
    "Thank you for registering with us.\n\n"
    "To complete your registration, please verify your email address by clicking the link below:\n\n"
    f"http://127.0.0.1:5000/accounts/verify/{email_token}\n\n"
    "If you did not sign up for this account, you can safely ignore this email.\n\n"
    "Best regards,\n"
    "GetItDone Team"
)
            send_mail(subject, message, email_from, [email])
    except Exception as e:
        print(f"Error creating user profile: {e}")
        traceback.print_exc()

        
