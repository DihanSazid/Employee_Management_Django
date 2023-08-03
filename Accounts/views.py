from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register_view(request):
    msg=None
    if request.method == "POST":
        form=Signup(request.POST)
        if form.is_valid():
            user=form.save()
            msg='user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form=Signup()

    return render(request,'register.html', {'form': form, 'msg': msg})
    
def login_view(request):
    form=Loginform(request.POST or None)
    msg=None
    if request.method == "POST":
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('admin_panel')
            elif user is not None and user.is_employee:
                login(request,user)
                return redirect('employee')
            else:
                msg="Invalid"
        else:
            msg="Error in validation form"

    return render(request, 'login.html',{'form': form, 'msg': msg})

def employee(request):
    if request.method == "POST":
        form=SaleForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.employee=request.user
            instance.save()
            return redirect('employee')
    else:
        form=SaleForm()    

    price=Sale.objects.filter(employee=request.user).aggregate(total_sale=Sum('sale'))
    bonus_user=AddBonus.objects.filter(employee=request.user).aggregate(total_bonus=Sum('Bonus'))
    context={
        'price': price,
        'bonus_user': bonus_user,
        'saleform': form
    }
   
    return render(request, 'home.html',context)

def admin(request):
    employeeinfo=User.objects.all()
    employee_sale=User.objects.values('username').annotate(total_sale=Sum('sale__sale')).order_by('username')
    context={
        'employee': employeeinfo,
        'employee_sale': employee_sale
    }
    return render(request, 'admin.html' ,context)

def addbonus(request):
    if request.method == "POST":
        form = Addbonusform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addbonus')
    else:
            form=Addbonusform()    
    
    bonus=AddBonus.objects.all().order_by('-id')
    context={
        'bonus': bonus,
        'form': form
    }
    return render(request,'addbonus.html',context)


        
