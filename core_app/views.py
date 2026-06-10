from django.shortcuts import render,redirect
def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request,'core_app/login.html')
def dashboard_view(request):
    return render(request,'core_app/dashboard.html')