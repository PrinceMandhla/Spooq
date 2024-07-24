from django.contrib.auth import authenticate,login
from django.shortcuts import redirect ,render
from django.contrib import messages
from .forms import RegForm
# Create your views here.

def reg_view(request):
    if request.method=='POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('success_page')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegForm()
    return render(request,'reg.html', {'form': form})

def my_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success_page')  # Redirect to the success page
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login_page')  # Redirect back to the login page with an error message

    return render(request, 'login.html')  # Render the login page if the request is not POST

def success_view(request):
    return render(request, 'success.html')

