from django.urls import path
from .views import ListaMotosView

app_name = 'moto'

urlpatterns=[
	path('', ListaMotosView.as_view(), name="home")

]