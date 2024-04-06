from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        
        errors = []
        if User.objects.filter(username=username).exists():
            errors.append('Username is already taken.')
        if '@' not in email:
            errors.append('Email must contain an @ symbol.')
        if password != confirm_password:
            errors.append('Password and Confirm Password do not match.')
        
        if errors:
            # Pass errors to the template
            return render(request, 'signup.html', {'errors': errors})
        else:
            # Process the valid form (e.g., create user, login, redirect)
            user = User.objects.create_user(username=username, email=email, password=password)
            # Redirect to a new URL:
            return redirect('some-success-url')

    # GET request or no form submission
    return render(request, 'signup.html')