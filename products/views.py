from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Reviews
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm
    reviews = product.reviews.filter(active=True)  # doesn't allow drafts
    new_review = None

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=True)
            new_review.product = product
            new_review.save()
        else:
            form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        'new_review': new_review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review of a product - With help from Suzy Bee """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.author = request.user
                review.save()
                messages.success(
                    request, 'Thank you for your review. \
                        This will now be added to this product')
                return redirect(reverse('product_detail', args=[product_id]))
            else:
                messages.error(
                    request,
                    'Sorry your review failed. Please try again')
    context = {
        'form': form
    }

    return render(request, context)


@login_required
def edit_review(request, product_id, review_id):
    """ Add a review and rating to the product """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Reviews, pk=review_id)
    if not request.user == review.author:
        messages.error(request, 'Sorry you are not allowed to do this')
        return redirect(reverse('product_detail', args=[product_id]))
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            messages.success(
                request,
                'Successfully updated product review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update review')
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    return render(request, 'products/edit_review.html', context)


@login_required
def delete_review(request, product_id, review_id):
    """
    Delete a review from the store
    """
    review = Reviews.objects.get(id=review_id)
    if review.author == request.user:
        review.delete()
        messages.success(
            request,
            f'You have deleted your review {review.review_title}')
        return redirect(reverse('product_detail', args=[product_id]))

    else:
        messages.error(request, "You are not allowed to do that.")

    return redirect(reverse('product_detail', args=[product_id]))
