from django.urls import path
from . import views 
#from .views import contact_view, contact_success_view
#from .views import BlogDetailView# Import the views from the current directory (app-level URLs)

urlpatterns = [
    path('', views.home, name='home'),
    

]

