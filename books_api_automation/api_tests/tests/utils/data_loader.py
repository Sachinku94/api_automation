import pandas as pd

def load_csv_data(file_path):
    df = pd.read_csv("/Users/sachin/Desktop/qa_Automations/API_Automation_Template/books_api_automation/data/orders.csv")
    return df.to_dict(orient="records")