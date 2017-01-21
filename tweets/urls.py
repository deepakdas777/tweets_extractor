from django.conf.urls import url
#from django.conf.urls.static import static
#from django.conf import settings
from . import views
urlpatterns = [
   
    url(r'^$', views.home, name='home'),
     
     url(r'^results$', views.results, name='results'),
 ]
