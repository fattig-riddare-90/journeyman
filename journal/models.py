from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date} ({'Public' if self.is_public else 'Private'})"
    
    class Meta:
        verbose_name_plural = "Diary Entries"