from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('register.urls', namespace='register')),
    path('school-profile/', include('schProfile.urls', namespace='profile')),
    path('school-detail/', include('schoolDetail.urls', namespace="sch-detail")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
