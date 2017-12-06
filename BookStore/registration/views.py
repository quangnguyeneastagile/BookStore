from django.shortcuts import render
from django.utils import timezone
from .models import User
# Create your views here.

def signIn(request):
    users = User.objects.filter(accountCreatedDate__lte=timezone.now()).order_by('accountCreatedDate')
    return render(request, 'registration/index.html', {'users':users})
