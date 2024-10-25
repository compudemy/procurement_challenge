# views.py
from decimal import Decimal
from django.shortcuts import render
from .models import Product

def evaluate_products():
    products = Product.objects.all()
    best_product = None
    best_score = -1  # Initialize with a low score

    for product in products:
        # Convert Decimal fields to float for calculations
        price = float(product.price)  # Convert to float
        past_performance = float(product.past_performance)  # Convert to float if needed

        # Weights for each factor (these can be adjusted based on importance)
        price_weight = 0.4
        quality_weight = 0.3
        compliance_weight = 0.2
        history_weight = 0.1

        # Score calculation (the lower the price, the better)
        score = (
            (1 / price * price_weight) +
            (past_performance * quality_weight) +
            (product.compliance * compliance_weight) +
            (past_performance * history_weight)
        )

        # Check if this product has the best score so far
        if score > best_score:
            best_score = score
            best_product = product

    return best_product
