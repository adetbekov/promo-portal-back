from django.conf.urls import url
from .views import CurrentUserView

app_name = "accounts"

urlpatterns = [
	url(r'^current$', CurrentUserView.as_view(), name="current")
]