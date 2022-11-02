export const CHART_COLORS = {
    red: 'rgb(255, 0, 0)',
    green: 'rgb(0, 255, 0)',
    blue: 'rgb(0, 0, 255)',
    cyan: 'rgb(0, 255, 255)',
    yellow: 'rgb(255, 255, 0)',
    indigo: 'rgb(75, 0, 130)',
    darkOrange: 'rgb(255, 140, 0)',
    springGreen: 'rgb(0, 255, 127)',
    lightBlue: 'rgb(173, 216, 230)',
    chocolate: 'rgb(210, 105, 30)',
    antiqueWhite: 'rgb(250, 235, 215)',
    darkSlateGray: 'rgb(47, 79, 79)',
    BurlyWood: 'rgb(222, 184, 135)',
    navy: 'rgb(0, 0, 128)',
    lime: 'rgb(0, 255, 0)',
}

const BASE_API_URL = 'http://localhost:8000/api/'

const ENDPOINTS = {
    incomeByCategory: BASE_API_URL + 'categories/income',
    expenseByCategory: BASE_API_URL + 'categories/expense',
    totalIncomeByMonths: BASE_API_URL + 'total/income',
    totalExpensesByMonth: BASE_API_URL + 'total/expense',
}

const getRequest = async (url) => {
    const response = await fetch(url)
    return await response.json()
}

export const getIncomeByCategories = async () => {
    return await getRequest(ENDPOINTS.incomeByCategory)
}

export const getExpenseByCategories = async () => {
    return await getRequest(ENDPOINTS.expenseByCategory)
}

export const getTotalIncomeForYear = async () => {
    return await getRequest(ENDPOINTS.totalIncomeByMonths)
}

export const getTotalExpenseForYear = async () => {
    return await getRequest(ENDPOINTS.totalExpensesByMonth)
}
