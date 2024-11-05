from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cor, Uva, Vinho
from django.db.models import Q 
from .forms import CorForm, UvaForm, VinhoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import imghdr
from django.http import HttpResponse
import qrcode
import base64
from io import BytesIO
from django.core.paginator import Paginator



def home(request):
    context = {'mensagem' : 'Olá Ninho!'}
    return render(request, 'core/index.html', context)

def lista_cores(request):
    
    data = {}
    
    search = request.GET.get('search')
    
    if search:
        all = Cor.objects.filter(nome__icontains=search)
    else:
        all = Cor.objects.all()  
    
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    
    form = CorForm()
    data['form'] = form
    return render(request, 'core/listar_cores.html', data)


def detalhar_cor(request, cor_id):
    cor = get_object_or_404(Cor, pk=cor_id)
    data = {
        'nome': cor.nome,
        'descricao': cor.descricao,
        'categoria': cor.categoria,
        'imagem': cor.imagem.url if cor.imagem else None,
        'created_at': cor.created_at,
        'updated_at': cor.updated_at
    }
    return JsonResponse(data)

def cor_delete_confirm(request, cor_pk):
    cor = Cor.objects.get(pk=cor_pk)
    cor.delete()
    return redirect('core_listar_cores')	

def salvar_cor(request):
    
    if request.method == 'POST':
        cor_id = request.POST.get('cor_id')
        if cor_id:  # Edição de categoria existente
            cor = get_object_or_404(Cor, pk=cor_id)
            form = CorForm(request.POST, request.FILES, instance=cor)
        else:  # Novo livro
            form = CorForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_cores')  # Redireciona após salvar
    else:
        form = CorForm()

    return render(request, 'cor_form.html', {'form': form})

def gerar_qr_code(request, cor_id):
    cor = get_object_or_404(Cor, id=cor_id)
    
    # Dados que serão incorporados no QR Code
    dados_qr = f'Nome: {cor.nome}\nDescrição: {cor.descricao}\nCategoria: {cor.categoria}'

    # Gera o QR Code
    qr = qrcode.make(dados_qr)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    
    # Codifica a imagem como base64
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Renderiza a template com a imagem em base64
    return render(request, 'core/exibir_qrcode_cor.html', {'qr_code_base64': qr_code_base64})

#  Uvas
def listar_uvas(request):
    data = {}
    
    search = request.GET.get('search')
    
    if search:
        all = Uva.objects.filter(nome__icontains=search)
    else:
        all = Uva.objects.all()  
    
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    
    form = UvaForm()
    data['form'] = form
    return render(request, 'core/listar_uvas.html', data)


def salvar_uva(request):
    if request.method == 'POST':
        uva_id = request.POST.get('uva_id')
        if uva_id:  # Edição de autor existente
            uva = get_object_or_404(Uva, pk=uva_id)
            form = UvaForm(request.POST, request.FILES, instance=uva)
        else:  # Novo autor
            form = UvaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_uvas')  # Redireciona após salvar
    else:
        form = UvaForm()

    return render(request, 'uva_form.html', {'form': form})

def detalhar_uva(request, uva_id):
    uva = get_object_or_404(Uva, pk=uva_id)
    data = {
        'nome': uva.nome,
        'descricao': uva.descricao,
        'imagem': uva.imagem.url if uva.imagem else None,
        
    }
    return JsonResponse(data)

def uva_delete_confirm(request, uva_pk):
    uva = Uva.objects.get(pk=uva_pk)
    uva.delete()
    return redirect('core_listar_uvas')	

def gerar_qr_codeUva(request, uva_id):
    uva = get_object_or_404(Uva, id=uva_id)
    
    # Dados que serão incorporados no QR Code
    dados_qr = f'Nome: {uva.nome}\nDescrição: {uva.descricao}\nImagem: {uva.imagem}'

     # Gera o QR Code
    qr = qrcode.make(dados_qr)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    
    # Codifica a imagem como base64
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Renderiza a template com a imagem em base64
    return render(request, 'core/exibir_qrcode_uva.html', {'qr_code_base64': qr_code_base64})


# Vinhos
def listar_vinhos(request):
    data = {}
    
    search = request.GET.get('search')
    
    if search:
        all = Vinho.objects.filter(nome__icontains=search)
    else:
        all = Vinho.objects.all()  
    
    paginator = Paginator(all, 4)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)        
    form = VinhoForm()
    data['form'] = form

    return render(request, 'core/listar_vinhos.html', data)

def detalhar_vinho(request, vinho_id):
    vinho = get_object_or_404(Vinho, pk=vinho_id)
    data = {
        'nome': vinho.nome,
        'teorAlc':vinho.teorAlc,
        'tempAmbServ': vinho.tempAmbServ,
        'data': vinho.data,
        'local':vinho.local,
        'safra': vinho.safra,
        'produtor': vinho.produtor,
        'paisRegiao': vinho.paisRegiao,
        'degustador': vinho.degustador,
        'rotulo': vinho.rotulo,
        'uva_id': vinho.uva_id_id if vinho.uva_id_id     else None,
        
    }
    return JsonResponse(data)

def salvar_vinho(request):
    if request.method == 'POST':
        vinho_id = request.POST.get('vinho_id')
        if vinho_id:  # Edição de autor existente
            vinho = get_object_or_404(Vinho, pk=vinho_id)
            form = VinhoForm(request.POST, request.FILES, instance=vinho)
        else:  # Novo estado
            form = VinhoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('core_listar_vinhos')  # Redireciona após salvar
    else:
        form = VinhoForm()
    print("Tentando renderizar: vinho_form.html")

    return render(request, 'vinho_form.html', {'form': form})


def vinho_delete_confirm(request, vinho_pk):
    vinho = Vinho.objects.get(pk=vinho_pk)
    Vinho.delete()
    return redirect('core_listar_vinhos')	

def gerar_qr_codeVinho(request, vinho_id):
    vinho = get_object_or_404(Vinho, id=vinho_id)
    
    # Dados que serão incorporados no QR Code
    dados_qr = f'Nome: {vinho.nome}\nTeor: {vinho.teorAlc}\nSafra: {vinho.safra}\nProdutor: {vinho.produtor}\nPaís: {vinho.paisRegiao}\nDegustador: {vinho.degustador}\nUva: {vinho.uva_id}'

     # Gera o QR Code
    qr = qrcode.make(dados_qr)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    
    # Codifica a imagem como base64
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Renderiza a template com a imagem em base64
    return render(request, 'core/exibir_qrcode_vinho.html', {'qr_code_base64': qr_code_base64})
