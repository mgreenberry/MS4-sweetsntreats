from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket',{})
    if not basket:
        message.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KQWFHAfu6MnYyGQ1Z3nIm2QfSs8cwAYjb5aprKVaw1k3sPZDgPM8oCGjCYk4cwO5ajwtBa8bjc4XqaejjG3o5bR00gqFYRWuK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
