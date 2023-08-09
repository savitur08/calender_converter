from django.urls import path
from . import views



urlpatterns = [
    path('',views.convert_gregorian_to_islamic_view,name="islamic"),
    path('hebrew/',views.convert_gregorian_to_hebrew_view,name="hebrew")
]