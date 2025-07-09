from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail_view(request, product_id):
    # डेटाबेस से विशिष्ट प्रोडक्ट प्राप्त करें, या यदि नहीं मिला तो 404 एरर दें
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product}) # product.html का उपयोग करें
