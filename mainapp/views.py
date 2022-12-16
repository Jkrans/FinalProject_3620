from django.shortcuts import render, redirect
from .models import gift as Gift, Recipient
from .forms import ItemForm, RecipientForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.


def index(request):
    gift_list = Gift.objects.filter(
        user=request.user.id)
    paginator = Paginator(gift_list, 8)
    page = request.GET.get('page')
    gift_list = paginator.get_page(page)
    context = {
        'gift_list': gift_list
    }
    return render(request, 'mainapp/index.html', context)


def distinct_recipients(request):
    recipients = Recipient.objects.filter(user=request.user.id)
    context = {'recipients': recipients}
    return render(request, 'mainapp/recipients.html', context)


@login_required
def details(request, id):
    try:
        item = Gift.objects.get(pk=id)
        context = {'item': item}

        return render(request, "mainapp/details.html", context)
    except Gift.DoesNotExist:
        return redirect('mainapp:no_page')


@login_required
def create_item(request):
    form = ItemForm(request.POST or None, request=request)
    recipient = RecipientForm(request.POST or None)

    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        if 'submit-create-item' in request.POST:
            messages.success(
                request, f'{profile} added successfully')
            return redirect('mainapp:create_item')
        return redirect('mainapp:index')

    elif recipient.is_valid():
        rec = recipient.save(commit=False)
        rec.user = request.user
        rec.save()
        messages.success(
            request, f'{rec} added successfully')
        return redirect('mainapp:create_item')

    return render(request, "mainapp/item-form.html", {'form': form, 'recipient': recipient})


@login_required
def update_item(request, id):
    try:
        item = Gift.objects.get(id=id)
    except Gift.DoesNotExist:
        return redirect('mainapp:no_page')

    form = ItemForm(request.POST or None, instance=item, request=request)
    if form.is_valid():
        form.save()
        return redirect('mainapp:index')

    return render(request, "mainapp/item-update.html", {'form': form, 'item': item})


@login_required
def delete_item(request, id):
    try:
        item = Gift.objects.get(id=id)
    except Gift.DoesNotExist:
        return redirect('mainapp:no_page')

    if request.method == 'POST':
        item.delete()
        return redirect('mainapp:index')

    return render(request, "mainapp/item-delete.html", {'item': item})


def page_does_not_exist(request):
    return render(request, "mainapp/doesnotexist.html")
