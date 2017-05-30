from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import etf, account, accountBreakdown
from .forms import etf_form, account_form, addETFtoAccount_form

# Import for Google Finance API Query
import requests, urllib, json

def index(request):
    """The home page for your Application"""
    return render(request, 'investapp/index.html')


@login_required
def etf_list(request):
    """Show list of all ETFs"""
    etf_list = etf.objects.filter(owner=request.user).order_by('symbol')
    context = {'etf_list': etf_list}
    return render(request, 'investapp/etf_list.html', context)


@login_required
def etf_details(request, etf_id):
    """Show a single ETF and its attributes"""
    e = get_object_or_404(etf, id=etf_id)
    if e.owner != request.user:
        raise Http404
    context = {'etf': e}
    return render(request, 'investapp/etf_details.html', context)


@login_required
def new_etf(request):
    """ Add a new ETF"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = etf_form()
    else:
        # POST data submitted; process data
        form = etf_form(request.POST)
        if form.is_valid():
            new_etf = form.save(commit=False)
            new_etf.owner = request.user
            new_etf.save()
            return HttpResponseRedirect(reverse('investapp:etf_list'))

    context = {'form': form}
    return render(request, 'investapp/new_etf.html', context)


@login_required
def edit_etf(request, etf_id):
    """ Edit existing ETF"""
    etf_to_edit = get_object_or_404(etf, id=etf_id)
    if etf_to_edit.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = etf_form(instance=etf_to_edit)
    else:
        # POST data submitted; process data
        form = etf_form(instance=etf_to_edit, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('investapp:etf_details',
                                                args=[etf_id]))
    context = {'etf': etf_to_edit, 'form': form}
    return render(request, 'investapp/edit_etf.html', context)


@login_required
def delete_etf(request, etf_id):
    """ Delete existing ETF """
    etf_to_delete = get_object_or_404(etf, id=etf_id)
    etf_to_delete.delete()
    return HttpResponseRedirect(reverse('investapp:etf_list'))


@login_required
def update_etf_price(request, etf_id):
    etf_to_update = get_object_or_404(etf, id=etf_id)

    # Make an API call and store the response.
    url = 'http://finance.google.com/finance/info?client=ig&q=NYSEARCA:' + etf_to_update.symbol
    res = urllib.request.urlopen(url)
    content = urllib.request.urlopen(url).read()
    content = str(content)
    contentClean = content.replace("//", "").replace('\\n', '').replace("b'", "").replace("[", "").replace("]", "").replace(" ", "")
    contentClean = contentClean[:-1]
    jsonRes = json.loads(contentClean)
    new_Price = (jsonRes['l_cur'])

    etf_to_update.currentPrice = new_Price
    etf_to_update.save()
    return HttpResponseRedirect(reverse('investapp:etf_details', args=[etf_id]))


@login_required
def refresh_etf_prices(request):

    # For loop to iterate over etf_list
    for etf_to_update in etf.objects.all():
        # Make an API call and store the response.
        url = 'http://finance.google.com/finance/info?client=ig&q=NYSEARCA:' + etf_to_update.symbol
        res = urllib.request.urlopen(url)
        content = urllib.request.urlopen(url).read()
        content = str(content)
        contentClean = content.replace("//", "").replace('\\n', '').replace("b'", "").replace("[", "").replace("]", "").replace(" ", "")
        contentClean = contentClean[:-1]
        jsonRes = json.loads(contentClean)
        new_Price = (jsonRes['l_cur'])

        etf_to_update.currentPrice = new_Price
        etf_to_update.save()

    return HttpResponseRedirect(reverse('investapp:etf_list'))


@login_required
def accounts_list(request):
    """Show list of all Accounts"""
    accounts_list = account.objects.filter(owner=request.user).order_by('id')
    context = {'accounts_list': accounts_list}
    return render(request, 'investapp/accounts_list.html', context)


@login_required
def new_account(request):
    """ Add a new Account"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = account_form()
    else:
        # POST data submitted; process data
        form = account_form(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.owner = request.user
            new_account.save()
            return HttpResponseRedirect(reverse('investapp:accounts_list'))
    context = {'form': form}
    return render(request, 'investapp/new_account.html', context)


@login_required
def account_details(request, account_id):
    """Show a single Account and its attributes"""
    acc = get_object_or_404(account, id=account_id)
    stock_list = accountBreakdown.objects.filter(owner=request.user, accountID=account_id).order_by('id')
    #stock_list = get_object_or_404(accountBreakdown, accountID=account_id)
    if acc.owner != request.user:
        raise Http404
    context = {'acc': acc, 'stock_list': stock_list}
    return render(request, 'investapp/account_details.html', context)


@login_required
def delete_account(request, account_id):
    """ Delete existing Account """
    account_to_delete = get_object_or_404(account, id=account_id)
    account_to_delete.delete()
    return HttpResponseRedirect(reverse('investapp:accounts_list'))


@login_required
def edit_account(request, account_id):
    """ Edit existing ETF"""
    account_to_edit = get_object_or_404(account, id=account_id)
    if account_to_edit.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = account_form(instance=account_to_edit)
    else:
        # POST data submitted; process data
        form = account_form(instance=account_to_edit, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('investapp:account_details',
                                                args=[account_id]))
    context = {'account': account_to_edit, 'form': form}
    return render(request, 'investapp/edit_account.html', context)


@login_required
def addETFtoAccount(request, account_id):
    """ Add an ETF to Account"""
    account_to_edit = get_object_or_404(account, id=account_id)
    if account_to_edit.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = addETFtoAccount_form()
    else:
        # POST data submitted; process data
        form = addETFtoAccount_form(request.POST)
        if form.is_valid():
            addedETF = form.save(commit=False)
            addedETF.owner = request.user
            addedETF.save()
            return HttpResponseRedirect(reverse('investapp:account_details', args=[account_id]))
    context = {'account': account_to_edit, 'form': form}
    return render(request, 'investapp/addETFtoAccount.html', context)
