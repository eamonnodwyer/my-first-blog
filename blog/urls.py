from django.conf.urls import url
from . import views # see views.


urlpatterns = [
    url(r'^$', views.post_list, name = "post_list"),

]