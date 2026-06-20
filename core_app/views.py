from django.shortcuts import render, redirect
import joblib
import os

# Load model (make sure model.pkl is in project root)
model = joblib.load('model.pkl')

def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard') # dashboard-kku redirect panna 'dashboard' nu kudunga
    return render(request, 'core_app/login.html')

def dashboard_view(request):
    prediction = None
    if request.method == 'POST':
        try:
            cgpa = float(request.POST.get('cgpa'))
            attendance = int(request.POST.get('attendance'))
            # Model prediction
            result = model.predict([[cgpa, attendance]])
            prediction = "Placed" if result[0] == 1 else "Not Placed"
        except (ValueError, TypeError):
            prediction = "Invalid Input"
            
    return render(request, 'core_app/dashboard.html', {'prediction': prediction})
    # Mela irukura ellam code-ukkum appuram, kadasila ithai copy panni paste pannunga

from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core_app/register.html', {'form': form})