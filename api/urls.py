from django.conf.urls import url
from . import views 


urlpatterns = [url(r'^$',views.SomeItemList.as_view()),]



