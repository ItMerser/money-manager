from datetime import date

from django.db.models import Sum, F, Q, Model
from django.db.models.functions import Round
from django.shortcuts import render
from django.http.response import JsonResponse

from core.models import (
    IncomeCategory,
    ExpenseCategory,
    Income,
    Expense,
)

MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}


def align_months(current_month: int) -> list[int]:
    months = []
    current_month += 1
    for _ in range(12):
        if current_month == 13:
            current_month = 1
        months.append(current_month)
        current_month += 1
    return months


def income_by_categories(request):
    queryset = IncomeCategory.objects.values('name') \
                                     .annotate(total=Round(Sum(F('income__count')), precision=2))
    return JsonResponse(data=list(queryset), safe=False)


def total_by_categories(model: Model, lookup: str) -> JsonResponse:
    queryset = model.objects.values('name').annotate(total=Round(Sum(F(lookup)), precision=2))
    return JsonResponse(data=list(queryset), safe=False)


def total_by_months(model: Model) -> JsonResponse:
    current_date = date.today()
    one_year_old = date(current_date.year - 1, current_date.month, current_date.day + 1)
    queryset = model.objects.filter(date__gte=one_year_old)
    aggregations = {
        MONTHS[month]: Round(Sum('count', filter=Q(date__month=month)), precision=2)
        for month in align_months(current_date.month)
    }
    return JsonResponse(data=queryset.aggregate(**aggregations))


def index(request):
    return render(request, 'index.html')


def get_categories(request, graphic: str) -> JsonResponse:
    exist_graphics = {
        'income': {'model': IncomeCategory, 'lookup': 'income__count'},
        'expense': {'model': ExpenseCategory, 'lookup': 'expense__count'},
    }
    if exist_graphics.get(graphic) is None:
        return JsonResponse(data=None, status=404)
    return total_by_categories(**exist_graphics[graphic])


def get_total(request, graphic: str) -> JsonResponse:
    exist_graphics = {
        'income': {'model': Income},
        'expense': {'model': Expense},
    }
    if exist_graphics.get(graphic) is None:
        return JsonResponse(data=None, status=404)
    return total_by_months(**exist_graphics[graphic])
