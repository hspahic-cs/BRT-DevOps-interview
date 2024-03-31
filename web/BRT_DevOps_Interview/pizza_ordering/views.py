from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

# Create your views here.
def order_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_page')
    else:
        form = OrderForm()    
    return render(request, 'order_pizza_template.html', {'form': form})

def order_history(request):
    orders = Order.objects.all()
    return render(request, 'order_history.html', {'orders': orders})