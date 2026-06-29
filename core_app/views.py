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
    reason= None
    if request.method == 'POST':
        try:
            cgpa = float(request.POST.get('cgpa')or 0)
            attendance = int(request.POST.get('attendance')or 0)
            projects = int(request.POST.get('projects')or 0)
            internship = int(request.POST.get('internship')or 0)
            comm_score = int(request.POST.get('comm_score')or 0)
            result = model.predict([[cgpa, attendance]])

            if result[0]==1:
                prediction="Placed"
                reason = "Strong profile with academic excellence and practical experience."
            else:
                prediction="Not placed"
                reason = "Reason: "
                if cgpa <6.0: reason +="need to improve cgpa."
                if projects ==0: reason +="Start working on technical projects."
                if internship ==0: reason +="Try to do an internship."
                if comm_score<6: reason +="Improve your communication skill"
        
        except Exception as e:
            print("Error:",e)
            prediction = "Processing Error"
            reason = "Ensure all inputs are numbers"
            
    return render(request, 'core_app/dashboard.html', {'prediction': prediction,'reason': reason})
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