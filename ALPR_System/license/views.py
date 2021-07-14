from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.decorators import unauthenticated_user

# Create your views here.
@login_required(login_url='login')
def testFn(request):
    return render(request, 'license/testPage.html')