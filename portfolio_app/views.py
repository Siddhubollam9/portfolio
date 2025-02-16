from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(
            f"Message from {name}",
            message,
            email,
            ["your-email@example.com"],  # Replace with your email
        )
    return render(request, "contact.html")