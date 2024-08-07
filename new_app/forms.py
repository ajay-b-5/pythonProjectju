import form import forms
from new_app.models import


class food_form(form.modelForm):
    class Meta:
        model = food
        fields = ("__all__")

