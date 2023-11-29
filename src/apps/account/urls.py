from django.urls import path
from .views import UserRegistrationView, UserUpdateView, ChangePasswordView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view=get_schema_view(
    openapi.Info(
        title='Scrooge_McDuck',
        default_version='v1',
        description='Scrooge_McDuck API',
        contact=openapi.Contact(email='palumna.f@gmail.com'),
        license=openapi.License(name='BSD License'),
        
    ),
    public=True,
)

urlpatterns=[
    path('docs/', schema_view.with_ui('swagger')),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]