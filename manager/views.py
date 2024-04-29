# views.py
from django.shortcuts import render
from kasa.models import Sale

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the URL specified in the 'next' parameter, or to a default URL
            return HttpResponseRedirect(request.GET.get('next', '/'))
    return render(request, 'login.html')

@login_required
def manager(request):
    items = Sale.objects.all()
    return render(request, 'manager.html', {'items': items, 'euro':settings.EURO, 'dollar':settings.DOLLAR})


