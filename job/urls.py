
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.job_list), # bach trbt had urls generale b urls dyal app
    path('<int:id>', views.detail_job)
]