from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from  .models import Cor, Uva, Vinho

class CorForm(forms.ModelForm):
    class Meta:
        model = Cor
        fields = ['categoria', 'created_at', 'descricao', 'id', 'imagem', 'nome', 'updated_at']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))    
    
        
class UvaForm(forms.ModelForm):
    class Meta:
        model = Uva
        fields = '__all__'
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))    
            
class VinhoForm(forms.ModelForm):
    class Meta:
        model = Vinho
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))        
        
                        