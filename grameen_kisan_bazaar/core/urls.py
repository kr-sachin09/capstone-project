from django.urls import path
from . import views # core ऐप के views को आयात करें

urlpatterns = [
    path('', views.home_view, name='home'), # होम पेज (index.html)
    path('login/', views.login_view, name='login'), # लॉगिन पेज (login.html)
    path('register/', views.register_view, name='register'), # रजिस्ट्रेशन पेज (registration.html)
    path('profile/', views.profile_view, name='profile'), # प्रोफ़ाइल पेज (profile.html)
    path('messages/', views.message_view, name='messages'), # मैसेज पेज (massage.html)
    path('logout/', views.logout_view, name='logout'), # लॉगआउट URL
    path('farmer-dashboard/', views.farmer_dashboard_view, name='farmer_dashboard'), # किसान के लिए प्रोडक्ट अपलोड पेज
]
