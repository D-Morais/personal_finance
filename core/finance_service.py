def calculate_totals(transactions):
    income = sum(t[2] for t in transactions if t[4] == "income")
    expense = sum(t[2] for t in transactions if t[4] == "expense")
    return income, expense, income - expense
