from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def Index(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    else:
        return render(request, 'analisis/resultados.html',  {})
