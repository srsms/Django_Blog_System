from django import forms
from .models import Post, Tag
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    tag_input = forms.CharField(
        label='Tags',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Comma-separated tags', 'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tag_input'].initial = ', '.join([tag.name for tag in self.instance.tags.all()])

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self._save_tags()
        return instance

    def _save_tags(self):
        # First, clear existing tags to avoid duplicates
        self.instance.tags.clear()
        
        # Process new tags
        tag_names = [name.strip() for name in self.cleaned_data['tag_input'].split(',') if name.strip()]
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            self.instance.tags.add(tag)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})