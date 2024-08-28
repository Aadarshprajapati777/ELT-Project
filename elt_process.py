import pandas as pd

def extract_data(payment_report_csv, mtr_excel):
    payment_df = pd.read_csv(payment_report_csv)
    mtr_df = pd.read_excel(mtr_excel)
    return payment_df, mtr_df

payment_report_csv = "data/payment_report.csv"
mtr_excel = "data/merchant_tax_report.xlsx"

payment_df, mtr_df = extract_data(payment_report_csv, mtr_excel)
print("Data extracted successfully!")
