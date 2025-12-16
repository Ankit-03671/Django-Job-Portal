from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Block all job creation except through admin by superusers
        if self.posted_by and not self.posted_by.is_superuser:
            raise PermissionDenied("Only superusers can create jobs")
        super().save(*args, **kwargs)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"