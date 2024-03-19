from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

from django.contrib.auth.models import Group
from django.core import validators

from shop.models import Product


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=100000)
#     description = forms.CharField(
#         label='Product description',
#         widget=forms.Textarea(attrs={"rows": 5, "cols": '33'}),
#         validators=[validators.RegexValidator(
#             regex=r'great',
#             message='Field must contain word great'
#         )],
#     )

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "name", "price", "description", "discount"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class MultipleClearableFileInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []

        final_attrs = self.build_attrs(attrs, {'type': 'file', 'name': name, 'multiple': 'multiple'})
        input_html = '<input{} />'.format(flatatt(final_attrs))

        return mark_safe(input_html)

    def value_from_datadict(self, data, files, name):
        if isinstance(files.get(name), list):
            return files.getlist(name)
        return files.get(name, None)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "discount", "preview", "images"]

    images = forms.ImageField(widget=MultipleClearableFileInput)




# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "name", "price", "description", "discount", "preview"
#
#     images = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}),
#     )