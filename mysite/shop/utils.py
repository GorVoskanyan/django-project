def add_two_numbers(a, b):
    return a + b

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"mulitple": True})
    )