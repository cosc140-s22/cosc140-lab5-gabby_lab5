from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductFilterForm, ReviewForm

def index(request):
    products = Product.objects.all().order_by('name')
    form = ProductFilterForm(request.GET)
    name_search = request.GET.get('name_search')
    if name_search:
        products = products.filter(name__icontains=name_search)

    context = {'products': products, 'form': form}
    return render(request, 'products/index.html', context)

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    context = { 'product':p }
    return render(request, 'products/show.html', context)

@login_required
def create_review(request, product_id):
  p = get_object_or_404(Product, pk=product_id)
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      p.review_set.create(stars=form.cleaned_data['stars'], review=form.cleaned_data['review'], user=request.user)
      return redirect('show', p.id)
    else:
      # JS: just use the form object from above since it has error info
      # from validation.  And avoid looking up p in database again since
      # it was already done above.
      # form = ReviewForm()
      # p = get_object_or_404(Product, pk=product_id)
      context = { 'product':p, 'form': form }
      return render(request, 'products/review.html', context)
  else:
    form = ReviewForm()
    # JS: duplicated lookup
    # p = get_object_or_404(Product, pk=product_id)
    context = { 'product':p, 'form': form }
    return render(request, 'products/review.html', context)
