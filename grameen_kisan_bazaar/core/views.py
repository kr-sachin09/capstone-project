from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm # Django का डिफ़ॉल्ट लॉगिन फ़ॉर्म
from django.contrib.auth.decorators import login_required, user_passes_test # प्रमाणीकरण के लिए
from .forms import RegistrationForm # हमने अभी जो फ़ॉर्म बनाया है उसे आयात करें
from .models import CustomUser # CustomUser मॉडल को आयात करें
from products.models import Product # Product मॉडल को आयात करें

def home_view(request):
    # मुख्य पेज, जहाँ प्रोडक्ट लिस्ट होंगे
    # हम सभी प्रोडक्ट्स को प्राप्त करेंगे और उन्हें टेम्प्लेट को पास करेंगे
    featured_products = Product.objects.all()
    return render(request, 'core/index.html', {'products': featured_products})

def login_view(request):
    # यदि उपयोगकर्ता पहले से लॉग इन है, तो होम पेज पर रीडायरेक्ट करें
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) # उपयोगकर्ता को लॉग इन करें
                return redirect('home') # सफल लॉगिन के बाद होम पेज पर रीडायरेक्ट करें
            else:
                # अमान्य क्रेडेंशियल
                return render(request, 'core/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
        else:
            # फ़ॉर्म वैलिडेशन एरर (जैसे खाली फ़ील्ड)
            return render(request, 'core/login.html', {'form': form, 'error_message': 'Please enter valid credentials.'})
    else:
        form = AuthenticationForm() # GET अनुरोध के लिए एक खाली फ़ॉर्म
    return render(request, 'core/login.html', {'form': form})

def register_view(request):
    # यदि उपयोगकर्ता पहले से लॉग इन है, तो होम पेज पर रीडायरेक्ट करें
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() # उपयोगकर्ता को सहेजें
            login(request, user) # रजिस्ट्रेशन के बाद सीधे लॉग इन करें
            return redirect('home') # सफल रजिस्ट्रेशन के बाद होम पेज पर रीडायरेक्ट करें
        else:
            # फ़ॉर्म वैलिडेशन एरर
            return render(request, 'core/registration.html', {'form': form})
    else:
        form = RegistrationForm() # GET अनुरोध के लिए एक खाली फ़ॉर्म
    return render(request, 'core/registration.html', {'form': form})

@login_required # यह सुनिश्चित करता है कि केवल लॉग इन उपयोगकर्ता ही इस पेज तक पहुँच सकें
def profile_view(request):
    # लॉग इन उपयोगकर्ता की प्रोफ़ाइल दिखाएँ
    return render(request, 'core/profile.html', {'user_profile': request.user})

@login_required # यह सुनिश्चित करता है कि केवल लॉग इन उपयोगकर्ता ही इस पेज तक पहुँच सकें
def message_view(request):
    # चैट/मैसेज पेज
    # अभी के लिए, यह केवल टेम्प्लेट को रेंडर करेगा.
    # रियल-टाइम चैट के लिए Django Channels जैसे उन्नत सेटअप की आवश्यकता होगी.
    return render(request, 'core/massage.html')

def logout_view(request):
    logout(request) # उपयोगकर्ता को लॉग आउट करें
    return redirect('login') # लॉगआउट के बाद लॉगिन पेज पर रीडायरेक्ट करें

# यह फ़ंक्शन जांचता है कि उपयोगकर्ता किसान है या नहीं
def is_farmer(user):
    return user.is_authenticated and user.role == 'farmer'

@login_required # यह सुनिश्चित करता है कि केवल लॉग इन उपयोगकर्ता ही इस पेज तक पहुँच सकें
@user_passes_test(is_farmer) # यह सुनिश्चित करता है कि केवल किसान ही इस पेज तक पहुँच सकें
def farmer_dashboard_view(request):
    # यह वह पेज होगा जहाँ किसान प्रोडक्ट अपलोड करेगा
    # आपके वर्कफ़्लो के अनुसार, हम अभी के लिए इसे सीधे Django एडमिन पर रीडायरेक्ट करेंगे
    # बाद में, आप यहाँ एक कस्टम फ़ॉर्म और UI बना सकते हैं
    return redirect('/admin/products/product/add/') # Django एडमिन में प्रोडक्ट जोड़ने का URL