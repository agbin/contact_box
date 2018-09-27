from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=64, null=True)
    street = models.CharField(max_length=64, null=True)
    house_nr = models.IntegerField(blank=True, null=True)
    flat_nr = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}, {} {} {}".format(self.city, self.street, self.house_nr, self.flat_nr)


class Group(models.Model):
    group_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return "{}".format(self.group_name)


class Person(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    description = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='address', blank=True)
    group = models.ManyToManyField(Group, blank=True)


    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)


TYPES = (
    ('HOME', 'home'),
    ('BUSINESS', 'business')
)


class Phone(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=8, choices=TYPES, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="phones", blank=True)

    def __str__(self):
        return "{}".format(self.number)


class Email(models.Model):
    mail = models.CharField(max_length=64)
    type = models.CharField(max_length=8, choices=TYPES, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='emails', blank=True)

    def __str__(self):
        return "{}".format(self.mail)


