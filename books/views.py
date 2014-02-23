from django.shortcuts import render_to_response
from models import Author, Book, Publisher

# Create your views here.

def list(request):
	return render_to_response('list.html')
