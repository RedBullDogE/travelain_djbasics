from django import forms
from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда',
                                       queryset=City.objects.all(),  # pylint: disable=maybe-no-member
                                       widget=forms.Select(
                                           attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='Куда',
                                     queryset=City.objects.all(),  # pylint: disable=maybe-no-member
                                     widget=forms.Select(
                                           attrs={'class': 'form-control js-example-basic-single'}))

    actross_cities = forms.ModelMultipleChoiceField(label='Через города',
                                                    queryset=City.objects.all(),  # pylint: disable=maybe-no-member
                                                    required=False,
                                                    widget=forms.SelectMultiple(
                                                        attrs={'class': 'form-control js-example-basic-multiple'}))

    travel_time = forms.CharField(label='Время в пути',
                                  widget=forms.NumberInput(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Время в пути'}))