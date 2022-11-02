from django.conf import settings


def fill_accounts(apps, schema):
    Account = apps.get_model('core', 'Account')
    accounts = settings.DEFAULT_ACCOUNTS.items()
    Account.objects.bulk_create([Account(name=name, balance=balance) for name, balance in accounts])


def fill_income_categories(apps, schema):
    IncomeCategory = apps.get_model('core', 'IncomeCategory')
    income_categories = settings.DEFAULT_INCOME_CATEGORIES
    IncomeCategory.objects.bulk_create([IncomeCategory(name=name) for name in income_categories])


def fill_expense_categories(apps, schema):
    ExpenseCategory = apps.get_model('core', 'ExpenseCategory')
    expense_categories = settings.DEFAULT_EXPENSE_CATEGORIES
    ExpenseCategory.objects.bulk_create([ExpenseCategory(name=name) for name in expense_categories])
