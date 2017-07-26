from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#from .views import add_update_dropdown,field_add,field_update,field_delete,field_update_view,test_view,field_add,Add_Holiday_Type,Add_Holiday
from .views import (
    LoginView,
    LogoutView,
    GetOtpView,
    OtpConfirmationView,
    ChangePasswordView
    )
urlpatterns = [
	url(r'^$',LoginView.as_view()),  
    url(r'^logout/$',LogoutView.as_view()),
    url(r'^otp/$',GetOtpView.as_view()),
    url(r'^otpConfirmation/$',OtpConfirmationView.as_view()),  
    url(r'^changePassword/$',ChangePasswordView.as_view()),  
]
