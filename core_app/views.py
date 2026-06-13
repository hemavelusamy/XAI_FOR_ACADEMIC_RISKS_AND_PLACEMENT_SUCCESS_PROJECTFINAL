from django.shortcuts import render,redirect
import joblib
import os
model = joblib.load('model.pkl')
def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request,'core_app/login.html')
def dashboard_view(request):
    prediction = "Pending..." # Start-la ethuvum illana ithu theriyum
    if request.method == 'POST':
        cgpa = float(request.POST.get('cgpa'))
        attendance = int(request.POST.get('attendance'))
        
        # Model prediction
        result = model.predict([[cgpa, attendance]])
        prediction = "Placed" if result[0] == 1 else "Not Placed"
    
    return render(request, 'core_app/dashboard.html', {'prediction': prediction})