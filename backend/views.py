# views.py
from django.shortcuts import render, redirect
from .models import Product
from .evaluate_product import evaluate_products

def manual_entry(request):
    if request.method == 'POST':
        product_type = request.POST.get('product_type')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        compliance = request.POST.get('compliance')
        past_performance = request.POST.get('past_performance')

        # Create a new Product instance and save it
        product = Product(
            product_type=product_type,
            product_name=product_name,
            price=price,
            compliance=compliance,
            past_performance=past_performance
        )
        product.save()

        # Redirect or render a success page
        return redirect('frontend:success_url')  # Replace with your success URL

    return render(request, 'error.html')  # Render your template here

# views.py
def best_product_view(request):
    best_product = evaluate_products()  # Call the evaluation function
    return render(request, 'frontend/best_product.html', {'best_product': best_product})

