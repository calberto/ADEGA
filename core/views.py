from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cor, Uva, Vinho
from django.db.models import Q 
from .forms import CorForm, UvaForm, VinhoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import imghdr
from django.http import HttpResponse
from django.core.paginator import Paginator



def home(request):
    context = {'mensagem' : 'Olá Ninho!'}
    return render(request, 'core/index.html', context)

def lista_cores(request):
    """ data = {}
    
     
    search = request.GET.get('search', '').strip()  # Verifica se existe o termo de busca
    orderby = request.GET.get('orderby', 'nome')  # Campo para ordenação, 'nome' por padrão
    direction = request.GET.get('direction', 'asc')  # Direção de ordenação, 'asc' por padrão

    if search:
        resultados = Cor.objects.filter(nome__icontains=search)
    else:
        resultados = Cor.objects.all()

    if direction == 'desc':
        resultados = resultados.order_by(f'-{orderby}')
    else:
        resultados = resultados.order_by(orderby)

    paginator = Paginator(resultados, 3)  # Paginação de 5 itens por página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    cores = paginator.get_page(page_obj)

    data['page_obj'] = page_obj
    data['cores'] = cores
    data['search'] = search
    data['ordery'] = orderby
    data['direction'] = direction
    """
    
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


