from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# in Django docs, you can find dedicated View classes, like ListView, FormView
# and etc, test this in future.
class ReviewView(View): # ListView, FormView and etc
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            "form": form
        })        

    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():            
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'reviews/review.html', {
            "form": form
        })        

class ThankYouView(TemplateView):    
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context
    
class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context

# not using anymore, because now I'm using classes
def review_function(request):    
    if request.method == 'POST':
        # updating data
            # existing_model = Review.objects.get()
            # form = ReviewForm(request.POST, instance=existing_model)
        # creating data
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # review = Review(
            #     user_name = form.cleaned_data['user_name'],
            #     review_text = form.cleaned_data['review_text'],
            #     rating = form.cleaned_data['rating'],
            # )
            form.save()
            
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form
    })

