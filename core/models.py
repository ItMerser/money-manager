from django.db import models
from django.db.models import Q
from django.utils import timezone


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.FloatField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(balance__gte=0),
                name='balance__gte__0',
                violation_error_message='balance must be greater or equal than 0',
            )
        ]

    def __str__(self):
        return self.name


class IncomeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.PROTECT)
    count = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    date = models.DateField(blank=True, default=timezone.now)
    comment = models.TextField(blank=True, default='')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(count__gt=0),
                name='income__count__gt__0',
                violation_error_message='count must be greater than 0',
            )
        ]

    def save(self, *args, **kwargs):
        account = Account.objects.get(pk=self.account.pk)
        account.balance += self.count
        account.save()
        print(f'{account.balance=}')
        super().save(*args, **kwargs)


class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT)
    count = models.FloatField()
    date = models.DateField(blank=True, default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    comment = models.TextField(blank=True, default='')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(count__gt=0),
                name='expense__count__gt__0',
                violation_error_message='count must be greater than 0',
            )
        ]

    def save(self, *args, **kwargs):
        account = Account.objects.get(pk=self.account.pk)
        account.balance -= self.count
        account.save()
        print(f'{account.balance=}')
        super().save(*args, **kwargs)
