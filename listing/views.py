from django.shortcuts import render

# Create your views here.
def index(request):
    # Display 5 most recent additions
    return render(request, 'index.html')