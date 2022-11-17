from django.contrib import admin

class AdminDisplayMixin:
    @admin.display
    def added_date(self, obj):
        return obj.date.strftime('%d %B %Y')

    @admin.display
    def total(self, obj):
        return obj._total

    @admin.display
    def category__name(self, obj):
        return obj.category.name
