from django.urls import path

from .views import (
    home,
    lista_cores,
    detalhar_cor,
    salvar_cor,
    cor_delete_confirm,
    listar_uvas,
    detalhar_uva,
    uva_delete_confirm,
    salvar_uva,
    listar_vinhos,
    detalhar_vinho,
    salvar_vinho,
    vinho_delete_confirm,
    gerar_qr_code,
    gerar_qr_codeUva,
    gerar_qr_codeVinho
    
)

urlpatterns = [
    path('', home, name='core_home'),
    path('cor/', lista_cores, name='core_listar_cores'),
    path('detalhar_cor/<int:cor_id>/', detalhar_cor, name='sistema_detalhar_cor'),
    path('salvar_cor/', salvar_cor, name='core_salvar_cor'),
    path('cor_delete/<int:cor_pk>/', cor_delete_confirm, name='core_cor_delete_confirm'),
    path('qr-code/<int:cor_id>/', gerar_qr_code, name='gerar_qr_code'),

 
    path('uva/', listar_uvas, name='core_listar_uvas'),
    path('detalhar_uva/<int:uva_id>/', detalhar_uva, name='sistema_detalhar_uva'),
    path('salvar_uva/', salvar_uva, name='core_salvar_uva'),
    path('uva_delete/<int:uva_pk>/', uva_delete_confirm, name='core_uva_delete_confirm'),
    path('qr-codeUva/<int:uva_id>/', gerar_qr_codeUva, name='gerar_qr_codeUva'),
    
    path('vinho/', listar_vinhos, name='core_listar_vinhos'),
    path('detalhar_vinho/<int:vinho_id>/', detalhar_vinho, name='sistema_detalhar_vinho'),
    path('salvar_vinho/', salvar_vinho, name='core_salvar_vinho'),
    path('vinho_delete/<int:vinho_pk>/', vinho_delete_confirm, name='core_vinho_delete_confirm'),
    path('qr-codeVinho/<int:vinho_id>/', gerar_qr_codeVinho, name='gerar_qr_codeVinho'),
    
]