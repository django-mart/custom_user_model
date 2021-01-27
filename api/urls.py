from django.conf.urls import url
from .views import Register

urlpatterns = [
    url(r'^register$', Register.as_view())
]