from django.urls import path, re_path
from .views import dental_list

from . import views

urlpatterns = [
    path('apdental/dental_list', views.dental_list, name='dental_list'),
    path('apdental/dental_chart_search', views.dental_chart_search, name="dental_chart_search"),
    path('apdental/dental_date_search', views.dental_date_search, name="dental_date_search"),
    path('apdental/dental_photo', views.dental_photo, name='dental_photo'),
    path('apdental/jquery_test', views.jquery_test, name='jquery_test'),
    path('apdental/resve_list', views.resve_list, name='resve_list'),
    path('apdental/imp_patient_info', views.imp_patient_info, name='imp_patient_info'),
    path('apdental/dlay_update', views.dlay_update, name='dlay_update'),
    path('apdental/arvl_update', views.arvl_update, name='arvl_update'),
    path('apdental/end_update', views.end_update, name='end_update'),
    path('apdental/clnic_epct_list', views.clnic_epct_list, name='clnic_epct_list'),
]
