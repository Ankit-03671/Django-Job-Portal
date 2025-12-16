from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    USER_TYPES = [
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='seeker')
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, help_text="Comma-separated skills")
    experience = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()