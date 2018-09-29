
from django.contrib import admin
from django.urls import path
from contacts.views import add_person, edit_person, delete_person, person_details, all_persons, addAddress, addPhone, addEmail, add_group



urlpatterns = [
    path('admin/', admin.site.urls),

    path('new/', add_person),
    path('modify/<id>/', edit_person),
    path('delete/<id>/', delete_person),
    path('show/<id>/', person_details),
    path('', all_persons, name='persons'),

    path('<id>/addAddress/', addAddress),
    path('<id>/addPhone/', addPhone),
    path('<id>/addEmail/', addEmail),
    path('add_group/', add_group),


]
