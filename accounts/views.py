# accounts/views.py

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Account
from .forms import AccountForm

def account_list(request):
    account_type = request.GET.get('account_type')  # Get the selected account type from the query parameters
    accounts = Account.objects.all()

    if account_type:  # Apply filter if an account type is selected
        accounts = accounts.filter(account_type=account_type)

    return render(request, 'accounts/account_list.html', {'accounts': accounts})


def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'accounts/account_form.html', {'form': form})

def account_update(request, pk):
    account = Account.objects.get(pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'accounts/account_form.html', {'form': form})

def account_delete(request, pk):
    account = Account.objects.get(pk=pk)
    account.delete()
    return redirect('account_list')

class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/account_detail.html'
    context_object_name = 'account'
