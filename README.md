# Mutual Fund Analytics

## Project Overview

Mutual Fund Analytics is a data analytics project focused on collecting, processing, and analyzing Indian mutual fund data. The project uses Python, Pandas, and financial APIs to perform data ingestion, validation, preprocessing, and visualization.

## Objectives

* Collect mutual fund NAV data from public APIs.
* Store and manage historical NAV datasets.
* Perform data quality validation and preprocessing.
* Analyze fund performance and risk metrics.
* Build dashboards and reports for investment insights.

---

## Project Structure

```text
mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Jupyter Notebook

---

## Datasets

### API-Based NAV Data

* HDFC Top 100
* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

### Supporting Datasets

* fund_master.csv
* fund_categories.csv
* benchmark.csv
* expense_ratio.csv

---

## Day 1 Deliverables

* Project folder structure created
* Python environment configured
* Dependencies installed
* Live NAV data fetched from mfapi.in
* 10 datasets stored in data/raw
* Data ingestion completed
* Data quality checks performed
* AMFI scheme code validation completed
* Git repository initialized

---

## Installation

```bash
git clone <repository-url>
cd mutual-fund-analytics

pip install -r requirements.txt
```

---

## Run Data Ingestion

```bash
python3 data_ingestion.py
```

---

## Fetch Latest NAV Data

```bash
python3 live_nav_fetch.py
```

---

## Author

Riddhiman Dutta

B.Tech CSE Core
SRM Institute of Science and Technology
