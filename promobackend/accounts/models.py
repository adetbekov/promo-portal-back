from django.db import models
from django.contrib.auth.models import User

import cities_light 
from cities_light.settings import ICity
from cities_light.models import City
def set_city_fields(sender, instance, items, **kwargs):
    instance.timezone = items[ICity.timezone]
cities_light.signals.city_items_post_import.connect(set_city_fields)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    # phone = models.CharField(max_length=12, null=True)
    # location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
