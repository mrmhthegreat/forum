
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/postdata/',include('ask.urls')),
    path('api/v1/noticedata/',include('notice.urls')),
    path('api/v1/faqdata/',include('faq.urls')),
    path('api/v1/userdata/',include('user.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/user/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/user/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/user/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        
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