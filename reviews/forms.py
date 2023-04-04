from django import forms

from .models import Review

# METHOD 1
# class ReviewForm(forms.Form):
#   user_name = forms.CharField(
#     label="Your Name",
#     max_length=100,          
#     error_messages={      
#       "required": "Please enter your name!",
#       "max_length": "Please enter a shorter name!"
#     },
#     # widget=forms.TextInput(attrs={
#     #   "required": False, # it didn't work            
#     #   })
#   )
#   review_text = forms.CharField(
#     label="Your Feedback",
#     widget=forms.Textarea, max_length=200
#   )
#   rating = forms.IntegerField(
#     label="Your Rating",
#     min_value=1,
#     max_value=5
#   )

# METHOD 2 (sounds better to me)
class ReviewForm(forms.ModelForm):    
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
              "required": "Please enter your name!",
              "max_length": "Please enter a shorter name!"
            }
        }