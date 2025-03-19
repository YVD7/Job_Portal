from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Applied', 'Applied'), ('Interviewd', 'Interviewd'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.seeker.username} applied for {self.job.title}"