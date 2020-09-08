from rest_framework import routers
from .views import HrView, Bulk, Search, Empty, Sort, Searching, Fire
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register('emp/<int:id>/', EmpView.as_view())

urlpatterns = [
    path('api/hr/<int:id>/', HrView.as_view()),
    path('api/fire/<int:id>', Fire.as_view()),
    path('api/hr/', HrView.as_view()),
    path('api/bulk/', Bulk.as_view()),
    path('api/search/', Search.as_view()),
    path('', Empty.as_view()),
    path('api/sort/', Searching.as_view()),
    # path('api/searching/', Searching.as_view()),
    # path('api/sort/<string:>/<string:filters>', Filter.as_view()),
]
