#urls.py
from django.urls import path
from .views import index, construction, bnalpha, entobn, bntoen, enalpha, custom_401, custom_403, custom_404, custom_405

urlpatterns = [
    path('', index, name='index'),
    path('construction/', construction, name='construction'),
    path('bnalpha/', bnalpha, name='bnalpha'),
    path('entobn/', entobn, name='entobn'),
    path('bntoen/', bntoen, name='bntoen'),
    path('enalpha/', enalpha, name='enalpha'),
]

# Add custom error handlers
handler401 = custom_401
handler403 = custom_403
handler404 = custom_404
handler405 = custom_405
