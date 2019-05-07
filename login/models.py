from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class LogInInfo(models.Model):
    # user = models.ForeignKey(User)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    netid = models.CharField(max_length=200, default="princeton")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")

    # phone_number = models.BigIntegerField()
    # img = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name, self.phone_number, str(self.image))
