from django.shortcuts import render, redirect
from .models import Person, Address, Email, Phone, Group
from .forms import PersonForm, AddressForm, EmailForm, PhoneForm, GroupForm
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.forms.formsets import formset_factory
from django.db import transaction
from django.contrib import messages

def add_person(request):
    form = PersonForm()
    form_group = GroupForm()
    if request.method == "POST":
        person = Person()
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")

        person.first_name = first_name
        person.last_name = last_name
        person.description = description
        person.save()

        group = Group()
        group_name = request.POST.get("group_name")
        group.group_name = group_name
        group.save()

        return redirect('/{}/addAddress/'.format(person.id))
    return render(request, 'new.html', {
        'PersonForm': form,
        'GroupForm': form_group,
    })


def edit_person(request, id):
    person = get_object_or_404(Person, id=id)
    address = Address.objects.get(id=person.address_id)
    phones = Phone.objects.filter(person_id=id)
    Email.objects.filter(person_id=id)

    PhoneFormSet = formset_factory(PhoneForm)
    data = {
        'form-TOTAL_FORMS': '3',
        'form-INITIAL_FORMS': '0',
    }
    if request.method == 'POST':
        form_person = PersonForm(request.POST)
        form_address = AddressForm(request.POST)
        form_email = EmailForm(request.POST)

        phone_formset = PhoneFormSet(data, request.POST)

        if phone_formset.is_valid():
            new_phones = []
            for phone_form in phone_formset:
                number = phone_form.cleaned_data.get('number')
                type = phone_form.cleaned_data.get('type')
                if number and type:
                    # new_phones.append(Phone(number=number, type=type))
                    new_phones.append(Phone(number=number, type=type, person_id=id))
            with transaction.atomic():
                Phone.objects.bulk_create(new_phones)
        if form_person.is_valid() and form_address.is_valid() and form_email.is_valid():
            person = form_person.save(commit=False)
            address = form_address.save(commit=False)
            email = form_email.save(commit=False)
            person.save()
            address.save()
            email.save()
            return HttpResponse("/thanks/")
    else:
        form_person = PersonForm(instance=person)
        form_address = AddressForm(instance=address)
        form_email = EmailForm()

    phone_data = [{'number': phone.number, 'type': phone.type} for phone in phones]
    phone_formset = PhoneFormSet(initial=phone_data)

    return render(request, 'modify.html', {
            'PersonForm': form_person,
            'AddressForm': form_address,
            'PhoneForms': phone_formset,
            'EmailForm': form_email,
            })


def delete_person(request, id):
    pass


def person_details(request, id):
    person = Person.objects.get(id=id)
    phone = Phone.objects.filter(person_id=id)
    mails = Email.objects.filter(person_id=id)
    groups = Group.objects.filter(id=id)
    return render(request, 'show.html', {
        'person': person, 'phone': phone, 'email': mails, 'group': groups
    })


def all_persons(request):
    persons = Person.objects.all().order_by('last_name')
    return render(request, '.html', {
        'persons': persons
    })


def addAddress(request, id):
    person = Person.objects.get(id=id)
    address_id = person.address_id
    if address_id:
        if request.method == "POST":
            #address_id = person.address.id
            address = Address.objects.get(id=address_id)
            address.city = request.POST.get("city")
            address.street = request.POST.get("street")
            address.house_nr = request.POST.get("house_nr")
            address.flat_nr = request.POST.get("flat_nr")
            address.save()

            return redirect('/modify/{}/'.format(id))

        form = AddressForm(
            initial={
                'city': person.address.city,
                'street': person.address.street,
                'house_nr': person.address.house_nr,
                'flat_nr': person.address.flat_nr,
            })
        return render(request, 'addAddress.html', {
            'AddressForm': form
        })
    else:
        if request.method == "POST":
            address = Address()
            address.city = request.POST.get("city")
            address.street = request.POST.get("street")
            address.house_nr = request.POST.get("house_nr")
            address.flat_nr = request.POST.get("flat_nr")
            address.save()

            #person = Person.objects.get(id=id)
            person.address_id = address.id
            person.save()
            return redirect('/{}/addPhone/'.format(id))
        else:
            form = AddressForm()
            return render(request, 'addAddress.html', {
            'AddressForm': form
        })



def addPhone(request, id):
    form = PhoneForm()
    if request.method == "POST":
        phone = Phone()
        phone.number = request.POST.get("number")
        phone.type = request.POST.get("type")
        phone.save()

        person = Person.objects.get(id=id)
        phone.person_id = id
        phone.save()
        return redirect('/{}/addEmail/'.format(id))
    return render(request, 'addPhone.html', {
        'PhoneForm': form
    })


def addEmail(request, id):
    form = EmailForm()
    if request.method == "POST":
        email = Email()
        email.mail = request.POST.get("mail")
        email.type = request.POST.get("type")
        email.save()
        Person.objects.get(id=id)
        email.person_id = id
        email.save()
        return redirect('/')
    return render(request, 'addEmail.html', {
        'EmailForm': form
    })



def add_group(request):
    form = GroupForm()
    # person = Person.objects.all()
    if request.method == "POST":
        group = Group()
        group_name = request.POST.get("group_name")
        group.group_name = group_name
        group.save()

        # group = Group.objects.get(id=id)
        groups = request.POST.getlist('group')

        for i in groups:
            person.group.add(i)

        # person = Person.objects.get(id=id)
        # group.person_id = id
        # group.save()

        return redirect('/')
    else:
        return render(request, 'add_group.html', {
         'GroupForm': form
    })












