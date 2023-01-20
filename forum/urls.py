
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Forum API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/postdata/',include('ask.urls')),
    path('api/v1/noticedata/',include('notice.urls')),
    path('api/v1/faqdata/',include('faq.urls')),
  
    path('auth/', include('authentication.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
                                  path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)




    
    # path('reset/',
    #     auth_views.PasswordResetView.as_view(
    #         template_name='password_reset.html',
    #         email_template_name='password_reset_email.html',
    #         subject_template_name='password_reset_subject.txt'
    #     ),
    #     name='password_reset'),
    # path('reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    #     name='password_reset_done'),
    # path('reset/',
    #     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #     name='password_reset_confirm'),
    # path('reset/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    #     name='password_reset_complete'),
    # path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    #     name='password_change'),
    # path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    #     name='password_change_done'),