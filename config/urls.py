from django.contrib import admin
from django.urls import path

from core.views import index, get_total, get_categories

urlpatterns = [
    path('', index, name='graphics'),
    path('api/categories/<str:graphic>', get_categories),
    path('api/total/<str:graphic>', get_total),
    path('admin/', admin.site.urls),
]
