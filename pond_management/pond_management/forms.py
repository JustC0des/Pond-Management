from django import forms
from .models import PondFish

class PondFishForm(forms.ModelForm):
    class Meta:
        model = PondFish
        fields = ['pond', 'Fish', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Quantity input styles
        self.fields['quantity'].widget.attrs.update({
            'class': 'quantity-input border bg-white font-medium min-w-20 placeholder-base-400 rounded shadow-sm '
                    'text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 '
                    'focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 '
                    'dark:bg-base-900 dark:border-base-700 dark:text-font-default-dark dark:focus:border-primary-600 '
                    'dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 '
                    'dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl',
            'style': 'margin-right: 10px;',
            'min': '0'
        })
        
        # Button styles
        self.fields['quantity'].widget.attrs['data-button-class'] = (
            'border '
            'border-base-200 items-center h-9.5 '
            'justify-center rounded shadow-sm shrink-0 '
            'w-9.5 hover:text-base-700 dark:bg-base-900 '
            'dark:border-base-700 dark:hover:text-base-200'
        )