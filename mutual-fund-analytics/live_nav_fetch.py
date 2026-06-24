import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

scheme_ids = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_ids.items():
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        data = response.json()

        df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{name}_nav.csv"

        df.to_csv(file_name, index=False)

        print(f"Saved {file_name}")

    except Exception as e:
        print(f"Error fetching {name}: {e}")