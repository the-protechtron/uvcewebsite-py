from django import forms
from .models import Grievance, Suggestion
from .models import Announcement, Circular, Broadcast
from .models import Contribution

class ContributeForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['name', 'email', 'phone', 'contribution_type', 'contribution_description', 'contact_preference']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class CircularForm(forms.ModelForm):
    class Meta:
        model = Circular
        fields = ['title', 'content']

class BroadcastForm(forms.ModelForm):
    class Meta:
        model = Broadcast
        fields = ['title', 'content']

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['title', 'description', 'user_name']  # Include user_name field

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'description', 'user_name']  # Include user_name field


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'date']  # Remove 'description' field
