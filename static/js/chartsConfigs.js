import {
    CHART_COLORS,
    getIncomeByCategories,
    getExpenseByCategories,
    getTotalIncomeForYear,
    getTotalExpenseForYear
} from "./const.js"

const colors = Object.values(CHART_COLORS)

const incomeCategories = await getIncomeByCategories()
const expenseCategories = await getExpenseByCategories()
const totalIncome = await getTotalIncomeForYear()
const totalExpenses = await getTotalExpenseForYear()

const currentMonths = Object.keys(totalIncome).map(month => month)

export const incomeByCategoriesConfig = {
    type: 'pie',
    data: {
        labels: incomeCategories.map(cat => cat.name),
        datasets: [{
            data: incomeCategories.map(cat => cat.total),
            backgroundColor: colors,
            borderColor: colors
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
}

export const expenseByCategoriesConfig = {
    type: 'pie',
    data: {
        labels: expenseCategories.map(cat => cat.name),
        datasets: [{
            data: expenseCategories.map(cat => cat.total),
            backgroundColor: colors,
            borderColor: colors
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
}

export const totalForYearConfig = {
    type: 'bar',
    data: {
        labels: currentMonths,
        datasets: [
            {
                label: 'Incomes',
                data: Object.values(totalIncome).map(value => value),
                backgroundColor: CHART_COLORS.navy,
                stack: 'stack 0'
            },
            {
                label: 'Expenses',
                data: Object.values(totalExpenses).map(value => value * -1),
                backgroundColor: CHART_COLORS.red,
                stack: 'stack 0'
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true
            }
        }
    }
}