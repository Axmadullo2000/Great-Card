from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
# Create your views here.


def _cart_id(request):
    card = request.session.session_key
    if not card:
        card = request.session.create()
    return card


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        card = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        card = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    card.save()

    try:
        card_item = CartItem.objects.get(product=product, cart=card)
        card_item.quantity += 1
        card_item.save()
    except CartItem.DoesNotExist:
        card_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=card,
        )
        card_item.save()
    return redirect('cart')


def remove_cart(request, product_id):
    card = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CartItem.objects.get(product=product, cart=card)
    if card_item.quantity > 1:
        card_item.quantity -= 1
        card_item.save()
    else:
        card_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    card = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CartItem.objects.get(product=product, cart=card)
    card_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, card_items=None):
    color = request.GET['color']
    size = request.GET['size']
    return HttpResponse(color + ' ' + size)
    exit()
    try:
        card = Cart.objects.get(cart_id=_cart_id(request))
        card_items = CartItem.objects.filter(cart=card, is_active=True)
        for cart_item in card_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        taxi = (2 * total) / 100
        grand_total = taxi + total
    except Exception as e:
        raise e
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': card_items,
        'taxi': taxi,
        'grand_total': grand_total,
    }
    return render(request, 'stores/cart.html', context)
