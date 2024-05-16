from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Community, Posting, PostType, PostTypeField

class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ('name', 'is_public', 'description')
        labels = {
            'name': '',
            'is_public': '',
            'description': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Community Name'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class PostingForm(ModelForm):
    class Meta:
        model = Posting
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        post_type = kwargs.pop('post_type', None)
        super(PostingForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}), required=True)
        self.fields['description'] = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}), required=True)

        if post_type:
            for field in PostTypeField.objects.filter(post_type=post_type):
                if field.field_name in ['post title', 'description']:
                    continue  # Skip adding 'post title' and 'description' again
                if field.field_type == 'text':
                    self.fields[field.field_name] = forms.CharField(
                        widget=forms.Textarea(attrs={'class': 'form-control'}), required=field.is_fixed)
                elif field.field_type == 'number':
                    self.fields[field.field_name] = forms.IntegerField(
                        widget=forms.NumberInput(attrs={'class': 'form-control'}), required=field.is_fixed)
                elif field.field_type == 'date':
                    self.fields[field.field_name] = forms.DateField(
                        widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), required=field.is_fixed)
                elif field.field_type == 'boolean':
                    self.fields[field.field_name] = forms.BooleanField(
                        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=field.is_fixed)

class PostTypeForm(ModelForm):
    class Meta:
        model = PostType
        fields = ('post_type_name',)
        widgets = {
            'post_type_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

PostTypeFieldFormSet = inlineformset_factory(PostType, PostTypeField, fields=('field_name', 'field_type'), extra=1, can_delete=True)