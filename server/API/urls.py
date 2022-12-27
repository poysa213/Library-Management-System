from rest_framework_nested import routers
from django.urls import path, include 

from . import views
# from django.conf import settings
# from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register('Books', views.BookViewSet, basename='books')
router.register('Categories', views.BookViewSet, basename='categories')
router.register('Borrowers', views.BorrowerViewSet, basename='borrower')
router.register('BorrowerdBooks', views.BorrwedBookViewSet, basename='borrowedbooks')
# router.register('Categories', views.CategorySerializer, basename='categories')

urlpatterns = router.urls

