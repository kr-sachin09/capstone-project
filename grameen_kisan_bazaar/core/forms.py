from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
   
    role = forms.ChoiceField(choices=CustomUser.USER_ROLES, label="Registration Type")
   
    phone_number = forms.CharField(max_length=15, required=False, help_text="Optional")
    village = forms.CharField(max_length=100, required=False, help_text="Optional")
    crops_grown = forms.CharField(widget=forms.Textarea, required=False, help_text="Only for Farmers (e.g., Wheat, Rice, Tomato)")
    bio = forms.CharField(widget=forms.Textarea, required=False, help_text="Only for Farmers")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
       
        fields = UserCreationForm.Meta.fields + ('role', 'phone_number', 'village', 'crops_grown', 'bio',)

   
    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        user.phone_number = self.cleaned_data['phone_number']
        user.village = self.cleaned_data['village']
       
        if user.role == 'farmer':
            user.crops_grown = self.cleaned_data['crops_grown']
            user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user