from django.contrib import admin
from django.db.models import Sum, F

from .models import (
    Account,
    IncomeCategory,
    ExpenseCategory,
    Income,
    Expense,
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance',)


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total',)

    @admin.display
    def total(self, obj):
        return obj._total

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_total=Sum(F('income__count')))
        return queryset


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total',)

    @admin.display
    def total(self, obj):
        return obj._total

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_total=Sum(F('expense__count')))
        return queryset


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category__name', 'count', 'date',)

    @admin.display
    def category__name(self, obj):
        return obj.category.name


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category__name', 'count', 'date',)

    @admin.display
    def category__name(self, obj):
        return obj.category.name
