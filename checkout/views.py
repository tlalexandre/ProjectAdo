from django.shortcuts import render,redirect,reverse
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template= 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OfITvIjZUE8b8QfqiqeO9n519V4er3WFFmSUDi0UHoOUevhIASSG1KLqDYYzXdz4VxPh539TtCaEk6H4aoj28wO00BfylN21c',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)