from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	"""docstring for CartAddPrduct"forms.Formf __init__(self, arg):
		super(CartAddPrduct,forms.Form.__init__()
		self.arg = arg
	"""
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, 
		coerce=int)
	update = forms.BooleanField(required=False,
		initial=False,
		widget=forms.HiddenInput)

		