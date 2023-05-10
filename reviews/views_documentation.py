from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# in Django docs, you can find dedicated View classes, like ListView, FormView
# and etc, test this in future.
class ReviewView(FormView): # ListView, FormView and etc
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, 'reviews/review.html', {
    #         "form": form
    #     })        

    # def post(self, request):
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():            
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, 'reviews/review.html', {
    #         "form": form
    #     })        

class ThankYouView(TemplateView):    
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review # exposed as "object_list"
    context_object_name = "reviews" # change "object_list" to "reviews"

    # def get_queryset(self): # if you want to fetch all, you can omit this method
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data


    # METHOD WITH TemplateView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # and will need to change "urls.py" parameter to PK
    # you can use "object" or the "model name in lowercase" in the view to access the exposed data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context

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

