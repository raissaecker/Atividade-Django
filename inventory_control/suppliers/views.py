from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages 
from .models import Supplier
from .forms import SupplierForm

# Create your views here.
def index(request):
    suppliers = Supplier.objects.order_by("-id")

    # Aplicando a paginação
    paginator = Paginator(suppliers, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { "suppliers": page_obj }

    return render(request, "suppliers/index.html", context)

def search(request):
    # Obtendo o valor da requisição
    search_value = request.GET.get("q").strip()

    # Verificando se algo foi digitado
    if not search_value:
        return redirect("suppliers:index")
    
    # Filtrando os fornecedores
    # O Q é usado para combinar filtros
    suppliers = Supplier.objects \
        .filter(Q(fantasy_name__icontains=search_value) | 
                Q(company_name__icontains=search_value)) \
                .order_by("-id")

    paginator = Paginator(suppliers, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { "suppliers": page_obj }

    return render(request, "suppliers/index.html", context)

def create(request):
    # POST
    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "O fornecedor foi cadastrado com sucesso!")

            return redirect("suppliers:index")
        
        messages.error(request, "Falha ao cadastar o fornecedor. Verifique o preenchimento dos campos.")
        
        context = { "form": form }

        return render(request, "suppliers/create.html", context)

    # GET
    form = SupplierForm()

    context = { "form": form }

    return render(request, "suppliers/create.html", context)
    

@require_POST
def delete(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    supplier.delete()

    return redirect("suppliers:index")

@require_POST
def toggle_enabled(request, id):
    supplier = get_object_or_404(Supplier, pk=id)

    supplier.enabled = not supplier.enabled
    supplier.save()

    return JsonResponse({ "message": "success" })