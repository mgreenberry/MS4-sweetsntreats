from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """
    A view to return the index page
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of a product to the shopping basket
    """

    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    return redirect_url(redirect_url)

