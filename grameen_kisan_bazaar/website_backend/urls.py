# website_backend/urls.py
from django.contrib import admin
from django.urls import path, include # 'include' को आयात करना सुनिश्चित करें
from django.conf import settings # सेटिंग्स को आयात करें
from django.conf.urls.static import static # स्टैटिक फ़ाइलों को सर्व करने के लिए

urlpatterns = [
    path('admin/', admin.site.urls), # Django एडमिन पैनल के लिए URL
    path('', include('core.urls')), # मुख्य ऐप के URL को रूट पर शामिल करें
    path('product/', include('products.urls')), # 'product/' प्रीफ़िक्स के तहत प्रोडक्ट ऐप के URL शामिल करें
]

# डेवलपमेंट के दौरान मीडिया फ़ाइलों (जैसे प्रोडक्ट इमेज) को सर्व करने के लिए
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
