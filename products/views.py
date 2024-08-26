from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm


def home(request):
    context = {}
    customers_set = Customer.objects.all()
    form = CustomerForm()

    if request.method == 'POST':
        if 'submit' in request.POST:
            pk = request.POST.get('submit')

            if not pk:
                form = CustomerForm(request.POST)
            else:
                customer = Customer.objects.get(id=pk)
                form = CustomerForm(request.POST, instance=customer)

            form.save()
            form = CustomerForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            customer = Customer.objects.get(id = pk)
            customer.delete()
            return redirect("home")
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            customer = Customer.objects.get(id = pk)
            form = CustomerForm(instance=customer)

    context['form'] = form
    context['customers'] = customers_set

    return render(request, "home.html", context)
