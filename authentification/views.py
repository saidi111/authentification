from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return  render(request,'contact.html')
def blog(request):
    return  render(request,'blog.html')
def blogd(request):
    return  render(request,'blog-details.html')
def feat(request):
    return  render(request,'feature.html')
def price(request):
    return  render(request,'pricing.html')