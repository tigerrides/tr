from django.db import models

# Create your models here.
class LogInInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #phone_number = models.CharField(max_length=20)
    # img = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name) #, self.phone_number)
