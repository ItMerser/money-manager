from random import choice, randint
from datetime import date, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import (
    Account,
    IncomeCategory,
    ExpenseCategory,
    Income,
    Expense,
)


class Command(BaseCommand):
    help = 'Generate random incomes and expense in database'

    accounts = list(Account.objects.all())
    income_categories = list(IncomeCategory.objects.all())
    expense_categories = list(ExpenseCategory.objects.all())

    def handle(self, *args, **options):
        self.fill_random_incomes()
        self.fill_random_expenses()

    def generate_notes(self, model, categories, accounts, count: int = 1000):
        from_day = settings.DAYS_RANGE[0]
        to_day = settings.DAYS_RANGE[1]
        days_range = [day for day in range(from_day, to_day)]

        def get_note():
            random_date = date.today() + timedelta(days=choice(days_range))
            note = model(
                category=choice(categories),
                count=randint(settings.COUNT_RANGE[0], settings.COUNT_RANGE[1]),
                account=choice(accounts),
                date=random_date
            )
            return note

        return [get_note() for _ in range(count)]

    def fill_random_incomes(self):
        notes = self.generate_notes(
            model=Income,
            categories=self.income_categories,
            accounts=self.accounts,
            count=settings.INCOME_NOTES_COUNT,
        )
        Income.objects.bulk_create(notes)

    def fill_random_expenses(self):
        notes = self.generate_notes(
            model=Expense,
            categories=self.expense_categories,
            accounts=self.accounts,
            count=settings.EXPENSE_NOTES_COUNT,
        )
        Expense.objects.bulk_create(notes)
