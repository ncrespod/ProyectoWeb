from django.urls import path

from com import views

app_name = 'com'

urlpatterns = [ 
    path('fetch_sensor_values_ajax', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),
    path('fetch_sensor_values_ajax2', views.fetch_sensor_values_ajax2, name='fetch_sensor_values_ajax2'),
    path('fetch_sensor_values_ajax3', views.fetch_sensor_values_ajax3, name='fetch_sensor_values_ajax3'),
    path('fetch_sensor_values_ajax4', views.fetch_sensor_values_ajax4, name='fetch_sensor_values_ajax4'),

]