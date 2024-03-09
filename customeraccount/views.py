from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer

def unauthorised(request):
    return render(request, 'customeraccount/register-fail.html', status=401)

# Create your views here.
def register(request):   
    if request.method == 'POST':
        if request.POST['password-one'] != '' and request.POST['password-two'] != '':
            if request.POST['password-one'] == request.POST['password-two']:
                try:
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

                except Exception:
                    return render(request, 'customeraccount/register-username-fail.html', status=401)

                return render(request, 'customeraccount/register-sucess.html', status=201)

            else:
                return unauthorised(request)
        else:
            return unauthorised(request)

    return render(request, 'customeraccount/register.html')
