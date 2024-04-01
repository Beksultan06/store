from django.urls import  path

from  apps.settings.views import  index, about, coming, gellary, contact_view, where, blog, contact

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name='about'),
    path("coming", coming, name='coming'),
    path("gellary", gellary, name='gellary'),
    path('contacts', contact_view, name='contacts'),
    path('where', where, name='where'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
]