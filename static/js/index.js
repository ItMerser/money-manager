import {
    incomeByCategoriesConfig,
    expenseByCategoriesConfig,
    totalForYearConfig
} from "./chartsConfigs.js"

const incomeByCategoriesCtx = document.getElementById('incomes-by-categories')
                               .getContext('2d')

const expenseByCategoriesCtx = document.getElementById('expenses-by-categories')
                                .getContext('2d')

const totalForYearCtx = document.getElementById('total-for-year')
                                .getContext('2d')

const totalIncomeGraphic = new Chart(incomeByCategoriesCtx, incomeByCategoriesConfig)
const totalExpenseGraphic = new Chart(expenseByCategoriesCtx, expenseByCategoriesConfig)
const totalForYearGraphic = new Chart(totalForYearCtx, totalForYearConfig)
