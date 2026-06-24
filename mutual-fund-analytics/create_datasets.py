import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

fund_master = pd.DataFrame({
    "scheme_code":[125497,119551,120503,118632,119092,120841],
    "fund_name":[
        "HDFC Top 100",
        "SBI Bluechip",
        "ICICI Bluechip",
        "Nippon Large Cap",
        "Axis Bluechip",
        "Kotak Bluechip"
    ],
    "fund_house":[
        "HDFC MF",
        "SBI MF",
        "ICICI Prudential MF",
        "Nippon MF",
        "Axis MF",
        "Kotak MF"
    ],
    "category":["Equity"]*6,
    "subcategory":["Large Cap"]*6,
    "risk_grade":["High"]*6
})

fund_master.to_csv("data/raw/fund_master.csv", index=False)

print("fund_master.csv created")

fund_categories = pd.DataFrame({
    "scheme_code":[125497,119551,120503,118632,119092,120841],
    "category":["Equity"]*6
})

fund_categories.to_csv(
    "data/raw/fund_categories.csv",
    index=False
)

print("fund_categories.csv created")

expense_ratio = pd.DataFrame({
    "scheme_code":[125497,119551,120503,118632,119092,120841],
    "expense_ratio":[1.2,1.1,1.0,1.3,1.4,1.2]
})

expense_ratio.to_csv(
    "data/raw/expense_ratio.csv",
    index=False
)

print("expense_ratio.csv created")

benchmark = pd.DataFrame({
    "scheme_code":[125497,119551,120503,118632,119092,120841],
    "benchmark":["Nifty 100 TRI"]*6
})

benchmark.to_csv(
    "data/raw/benchmark.csv",
    index=False
)

print("benchmark.csv created")