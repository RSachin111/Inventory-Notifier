from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token creation
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    path('api/', include('stockalertapp.urls')),  # Include your app's API endpoints
]
