from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EnquiryCreationForm




def index_form(request):
	if request.method == 'POST':
		form = EnquiryCreationForm(request.POST)
		if form.is_valid():
			
			form.save()
			return HttpResponseRedirect('/')                      
			
		else:

			return HttpResponse('PLEASE FILL THE ENQUIRY FORM AGAIN')
    
		
	form = EnquiryCreationForm()
		
	return render(request, 'enquiry/index_form.html', {'form': form})
	  

	
