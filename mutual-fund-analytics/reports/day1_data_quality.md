# Day 1 Data Quality Summary

## Datasets Loaded

Total datasets loaded: 10

## Observations

### Data Types

* scheme_code stored as integer.
* NAV values stored as float64.
* Date values stored as string and require conversion to datetime format.

### Missing Values

* No missing values observed in generated datasets.

### Dataset Sizes

* HDFC_Top100_nav.csv: 3107 records
* SBI_Bluechip_nav.csv: 3324 records
* ICICI_Bluechip_nav.csv: 3323 records
* Nippon_LargeCap_nav.csv: 3314 records
* Axis_Bluechip_nav.csv: 3581 records
* Kotak_Bluechip_nav.csv: 3317 records

### Data Quality Issues

* Date columns should be converted to datetime.
* Category datasets are manually generated and contain limited categories.
* Benchmark and expense ratio datasets contain placeholder values.

## Conclusion

Data ingestion completed successfully and datasets are ready for preprocessing.
