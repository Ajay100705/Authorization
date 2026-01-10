from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def Signup_view(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render (request, 'signup.html', {'form' : form})

def Login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('dashboard')
            form.add_error(None, "Invalid credentials")

    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


@login_required
def dashboard_redirect_view(request):
    user = request.user

    if user.user_type == 'student':
        return redirect('student_dashboard')
    
    elif user.user_type == 'teacher':
        return redirect('teacher_dashboard')
    
    elif user.user_type == 'admin':
        return redirect('admin_dashboard')
    
    else:
        return redirect('student_dashboard')
    
@login_required
def student_dashboard(request):
    return render(request, 'dashboard/student.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin.html')

    
