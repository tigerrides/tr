from django.forms import ModelForm
from . import models


# Create your models here.
class CreateProfile(ModelForm):
    class Meta:
        model = models.LogInInfo
        fields = [
            # 'user',
            'first_name',
            'last_name',
            'phone_number',
            'image',
        ]

    # validate image properties 
    # https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django 
    # def clean_image(self):
    #     image = self.cleaned_data['image']

    #     try:
    #         w, h = get_image_dimensions(image)

    #         #validate dimensions
    #         max_width = max_height = 1280
    #         if w > max_width or h > max_height:
    #             raise ValidationError(
    #                 u'Please use an image that is '
    #                  '%s x %s pixels or smaller.' % (max_width, max_height))

    #         #validate content type
    #         main, sub = image.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise ValidationError(u'Please use a JPEG, '
    #                 'GIF or PNG image.')

    #         #validate file size
    #         if len(image) > (20 * 1024):
    #             raise ValidationError(
    #                 u'Avatar file size may not exceed 20k.')

    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass

    #     return image