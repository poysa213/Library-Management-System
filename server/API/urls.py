from rest_framework_nested import routers
from django.urls import path, include 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register('Books', views.BookViewSet, basename='books')
router.register('Categories', views.BookViewSet, basename='categories')
router.register('Borrowers', views.BorrowerViewSet, basename='borrower')
router.register('BorrowerdBooks', views.BorrwedBookViewSet, basename='borrowedbooks')
# router.register('Categories', views.CategorySerializer, basename='categories')
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += router.urls

