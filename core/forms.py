from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
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
        fields = [
            'nome', 'teorAlc', 'tempAmbServ', 'data', 'local', 'safra',
            'produtor', 'paisRegiao', 'degustador', 'rotulo', 'uva_id'
        ]

    def __init__(self, *args, **kwargs):
        super(VinhoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-4 mb-0'),
                Column('teorAlc', css_class='form-group col-md-4 mb-0'),
                Column('tempAmbServ', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('data', css_class='form-group col-md-4 mb-0'),
                Column('local', css_class='form-group col-md-4 mb-0'),
                Column('safra', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('produtor', css_class='form-group col-md-4 mb-0'),
                Column('paisRegiao', css_class='form-group col-md-4 mb-0'),
                Column('degustador', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('rotulo', css_class='form-group col-md-6 mb-0'),
                Column('uva_id', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        ) 
             
        
                        