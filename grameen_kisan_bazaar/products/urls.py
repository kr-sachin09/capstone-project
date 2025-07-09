from django.urls import path
from . import views # products ऐप के views को आयात करें

urlpatterns = [
    # <int:product_id> एक URL पैरामीटर है जो एक पूर्णांक (integer) प्रोडक्ट ID को कैप्चर करेगा
    path('<int:product_id>/', views.product_detail_view, name='product_detail'),
]
