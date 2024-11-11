from django.urls import path
from . import views
# ====== home下的url ========
urlpatterns = [
    path("", views.hello),
]