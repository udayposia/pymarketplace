from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput



class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'username',
                'class':'input100',
                'autocomplete':'off',
                'style': 'border-color: blue;',

            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name':'password',
        'class':'input100',
        'autocomplete':'off',
        'style': 'border-color: blue;',

    }))



class AddUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'username',
                'class':'input100',
                'autocomplete':'off',
                'style': 'border-color: blue;',

            }
        )
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'first_name',
                'class':'input100',
                'autocomplete':'off',
                'style': 'border-color: blue;',

            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'last_name',
                'class':'input100',
                'autocomplete':'off',
                'style': 'border-color: blue;',

            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name':'password',
        'class':'input100',
        'autocomplete':'off',
        'style': 'border-color: blue;',

    }))

    avatar = forms.ImageField(
                widget=forms.FileInput(
                    attrs={
                    'type':"file",
                    'name':'avatar',
                    'accept':'image/png,image/jpg,image/jpeg',
                    'enctype':'multipart/form-data',
                    'id':'customFile',
                    'class':'custom-file-input',
                    'placeholder':'Upload Store Logo',
                    'required':'True',

                    }
                )
            )
    about = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'about',
                'class':'input100',

                'style': 'border-color: blue;',

            }
        )
    )
    slogan = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'name':'last_name',
                'class':'input100',

                'style': 'border-color: blue;',

            }
        )
    )
    class Meta:
        model = UserDetails
        fields = ['username', 'first_name', 'last_name', 'password', 'avatar', 'about', 'slogan']


class CreateJob(forms.ModelForm):

    title = forms.CharField(
            max_length=500,
            widget=forms.TextInput(
                attrs={
                    'name':'title',
                    'class':'form-control',
                    'style': 'border-color: green;',
                }
            )
        )
    # job_author = forms.ModelChoiceField(queryset=UserDetails.objects.all(),widget=forms.Select(attrs={'class':'form-control',}))
    CATEGORY_CHOICES = (
            ("GD", "Graphics & Design"),
            ("DM", "Digital & Marketing"),
            ("VA", "Video & Animation"),
            ("MA", "Music & Audio"),
            ("PT", "Programming & Tech")
        )
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,
                widget=forms.Select(
                    attrs={
                    'name':'company_type',
                    'class':'form-control',
                    'id':"category",
                    'required':'True',
                    'style': 'border-color: green;',


                    }
                )
            )
    description = forms.CharField(
            max_length=1000,
            widget=forms.Textarea(
                attrs={
                    'name':'description',
                    'class':'form-control',
                    'style': 'border-color: green;',
                }
            )
        )
    price = forms.IntegerField(
            widget=forms.NumberInput(
                attrs={
                    'name':'price',
                    'class':'form-control',
                    'style': 'border-color: green;',

                }
            )
        )
    photo = forms.ImageField(
                widget=forms.FileInput(
                attrs={
                    'name':'photo',
                    'class':'form-control',
                    'accept':'image/png,image/jpg,image/jpeg',
                    'enctype':'multipart/form-data',
                    'placeholder':'Upload Job Thumbnail',
                    'style': 'border-color: green;',
                }
            )
        )
    active_status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name':'active_status',
                    'class':'form-control',
                    'style': 'border-color: green; width:20px;height:20px;',
                }
            )
            )

    class Meta:
        model  = Jobs
        fields = ['title','category','description','price','photo', 'active_status']



class CreateOrderForm(forms.ModelForm):
    order_deadline = forms.DateField( widget=forms.SelectDateWidget(attrs={
                'name':'order_deadline',

                'style': 'border-color: green;',

            }
        )
    )
    order_budget = forms.IntegerField(
            widget=forms.NumberInput(
                attrs={
                    'name':'price',
                    'class':'form-control',
                    'style': 'border-color: green;',

                }
            )
        )
    author_offer = forms.CharField(
            max_length=1000,
            widget=forms.Textarea(
                attrs={
                    'name':'author_offer',
                    'class':'form-control',
                    'style': 'border-color: green;',
                }
            )
        )
    class Meta:
        model  = Orders
        fields = [ 'author_offer','order_deadline', 'order_budget']
