from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class LogInInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    # phone_number = models.BigIntegerField()
    # img = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.phone_number)
