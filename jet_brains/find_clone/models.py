from django.db import models

# Create your models here.


class New_File(models.Model):
    file = models.FileField(upload_to='downloaded')

    def __str__(self):
        return self.title