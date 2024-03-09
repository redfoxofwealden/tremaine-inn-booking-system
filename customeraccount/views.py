from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer

# Create your views here.
def register(request):
    if request.method=='POST':
        user = User.objects.create_user(
            request.POST['emailaddress'],
            request.POST['emailaddress'],
            request.POST['password-one']
        )

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()

        customer = Customer(
            user=user,
            mobile_number=request.POST['mobilenumber'],
            telephone_number=request.POST['telnumber']
        )
        customer.save()

        print('post received')

    return render(request, 'customeraccount/register.html')
