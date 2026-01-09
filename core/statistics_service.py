import pandas as pd


def to_dataframe(transactions):
    cols = ["id", "description", "amount", "category", "type", "date"]
    return pd.DataFrame(transactions, columns=cols)


def monthly_average_expense(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["type"] == "expense"]
    return df.groupby(df["date"].dt.month)["amount"].mean()


def category_distribution(df):
    df = df[df["type"] == "expense"]
    return df.groupby("category")["amount"].sum()
