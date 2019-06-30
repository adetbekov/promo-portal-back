from allauth.account.adapter import DefaultAccountAdapter
from cities_light.models import City


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        # user_field(user, 'city', request.data.get('city', ''))
        user_field(user, 'first_name', request.data.get('first_name', ''))
        user_field(user, 'last_name', request.data.get('last_name', ''))
        user.save()
        profile = user.profile
        profile.city = City.objects.get(name__iexact = request.data.get('city', '').lower())
        profile.save()
        return user, profile