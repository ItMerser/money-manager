from django.contrib import admin
from django.conf import settings

class AdminDisplayMixin:
    @admin.display
    def added_date(self, obj):
        return obj.date.strftime('%d %B %Y')

    @admin.display
    def total(self, obj):
        total = obj._total
        if total:
            return total.quantize(settings.ROUND_TO)
        return total

    total.admin_order_field = '_total'

    @admin.display
    def category__name(self, obj):
        return obj.category.name
