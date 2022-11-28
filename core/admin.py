from django.contrib import admin
from django.db.models import Sum, F

from core.models  import (
    Account,
    IncomeCategory,
    ExpenseCategory,
    Income,
    Expense,
)
from core.mixins import AdminDisplayMixin


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance',)


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(AdminDisplayMixin, admin.ModelAdmin):
    list_display = ('name', 'total',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_total=Sum(F('income__count')))
        return queryset


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(AdminDisplayMixin, admin.ModelAdmin):
    list_display = ('name', 'total',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_total=Sum(F('expense__count')))
        return queryset


@admin.register(Income)
class IncomeAdmin(AdminDisplayMixin, admin.ModelAdmin):
    list_display = ('category__name', 'count', 'added_date',)

@admin.register(Expense)
class ExpenseAdmin(AdminDisplayMixin, admin.ModelAdmin):
    list_display = ('category__name', 'count', 'added_date',)
