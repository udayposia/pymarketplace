from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core import serializers
from django.core.cache import cache
import json
import random
import string
from django.db import transaction
# import haikunator


# Create your views here.
def home(request):
    jobs = Jobs.objects.filter(active_status=True, job_status=False)
    return render(request, 'home.html',{'jobs':jobs})

def add_user(request):
    form = AddUserForm()
    if request.method =='POST':
        form = AddUserForm(request.POST, request.FILES)
        print('post')

        if form.is_valid():
            print('validate')
            form.save()
            print('save')

            return redirect('user_login')
    print(form.errors)
    return render(request, 'user_signup_page.html', {'form':form})


def user_login(request):
    user_loginform = UserLoginForm()
    if request.method=='POST':
        user_loginform = UserLoginForm(request.POST)
        username  = request.POST['username']
        password = request.POST['password']

        user_qs = UserDetails.objects.filter(username=username, password=password)
        if user_qs :
            user_rs = UserDetails.objects.get(username=username)
            request.session['user_id']=user_rs.id
            user_json = json.loads(serializers.serialize('json', user_qs))
            # print(type(user_json))
            # print(user_json[0])
            # print(user_json[0]['fields'])

            request.session['user_obj']=user_json[0]['fields']
            print(request.session['user_obj'])
            request.session['role']='user'
            return redirect('home')

        else:
            messages.success(request, 'Invalid!.Either username or password is incorrect!!! ', extra_tags='alert alert-danger alert-dismissible')
            return redirect('user_login')

    return render(request, 'user_login_page.html',{'form':user_loginform})

def user_logout(request):
    try:
       del request.session['user_id'];
       messages.success(request, 'Account Logged out Succesfully', extra_tags='alert alert-info alert-dismissible')
       del request.session['user_obj'];
       del request.session['role'];
    except KeyError:
        pass

    return redirect('user_login')

def view_profile(request, username):
    profile = UserDetails.objects.get(username=username)

    # job_author = UserDetails.objects.get(id=id)
    jobs =Jobs.objects.filter(job_author=profile)
    return render(request, 'profile.html',{'profile':profile, 'jobs':jobs })

def view_job(request, id):
    jobs =Jobs.objects.get(id=id)
    print(jobs)
    orders = Orders.objects.filter(job_details=jobs)
    print(orders)
    return render(request, 'job_detail.html',{'jobs':jobs,'orders':orders})

def create_job(request):
    form = CreateJob()
    if request.POST.get('cjob'):
        form = CreateJob(request.POST, request.FILES)
        if form.is_valid():
            id = request.session['user_id']
            job_author = UserDetails.objects.get(id=id)
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            # job_author = request.session.user_obj
            price = form.cleaned_data['price']
            photo = form.cleaned_data['photo']
            active_status = form.cleaned_data['active_status']

            jobs = Jobs.objects.create(title=title,
                        job_author=job_author,
                        category=category,
                        description=description,
                        price=price,
                        photo=photo,
                        active_status=active_status)
            jobs.save()
            return redirect('home')
        else:
            return redirect('create_job')



    return render(request, 'create_jobs.html',{'form':form})

def my_jobs(request):
    if request.session['user_obj'] :
        id = request.session['user_id']
        job_author = UserDetails.objects.get(id=id)
        jobs = Jobs.objects.filter(job_author=job_author)
        return render(request, 'my_jobs.html', {'jobs':jobs})

def create_order(request, id):
    form = CreateOrderForm()
    user_id = request.session['user_id']
    order_author = UserDetails.objects.get(id=user_id)
    jobs= Jobs.objects.get(id=id)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order_deadline = form.cleaned_data['order_deadline']
            order_budget   = form.cleaned_data['order_budget']
            author_offer   = form.cleaned_data['author_offer']
            order = Orders.objects.create(order_author=order_author,
                                          job_details=jobs,
                                          author_offer=author_offer,
                                          order_deadline=order_deadline,
                                          order_budget = order_budget,
                                          )
            order.save()
            return redirect('/')







    return render(request, 'create_order.html', {'form':form, 'jobs':jobs})

def jobs_request(request):
    if request.POST.get('status') :
        print('post')
        job_author_id = request.POST.get('job_author_id')

        print(request.session['user_id'])
        print(job_author_id)
        print(int(request.session['user_id']) == int(job_author_id))
        if int(request.session['user_id']) == int(job_author_id):
            print(request.session['user_id'] == job_author_id)
            order_id = request.POST.get('order_id')
            job_id   = request.POST.get('job_id')
            job = Jobs.objects.get(id=job_id)
            job_author = UserDetails.objects.get(id = request.session['user_id'])
            print(job_author)
            order = Orders.objects.get(id = order_id)
            order.order_status = True
            # print(order_qs)
            job.active_status = False
            job.job_status = True
            # print(yes)
            order.save()
            print('order true')
            job.save()
            order_qs = Orders.objects.filter(order_status=False, job_details__job_author=job_author,job_details__id=job_id)
            order_qs.delete()

            return redirect('jobs_request')
        else:
            error='Authentication Failed!!!'
            context ={'error':error}
    user_id = request.session['user_id']
    job_author = UserDetails.objects.filter(id=user_id)
    # jobs = Jobs.objects.get(job_author=job_author)
    print(job_author[0])
    try:
        orders = Orders.objects.filter(job_details__job_author=job_author[0])
    except Orders.DoesNotExist:
        orders = None
    if orders :
        context={'orders':orders}

    else:
        context ={}


    return render(request, 'my_jobs_request.html',context)
