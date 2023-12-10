from django.urls import path


from catalog.views import index, contacts

urlpatterns = [
    path('home/', index),
    path('contacts/', contacts),
]
