from django.db import models

# Create your models here.


class New_File(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='downloaded')
    check_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title