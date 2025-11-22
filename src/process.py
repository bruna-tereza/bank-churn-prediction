import pandas as pd
import os

def process_bank_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(project_root, 'data', 'Customer-Churn-Records.csv')
    output_file = os.path.join(project_root, 'data', 'churn_processed.csv')

    if not os.path.exists(input_file):
        print(f"Erro: Arquivo {input_file} não encontrado.")
        return
    
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return

    cols_to_drop = ['RowNumber', 'CustomerId', 'Surname']
    df_clean = df.drop(columns=cols_to_drop)

    df_processed = pd.get_dummies(df_clean, columns=['Geography', 'Gender', 'Card Type'], drop_first=True)
    
    bool_cols = df_processed.select_dtypes(include=['bool']).columns
    df_processed[bool_cols] = df_processed[bool_cols].astype(int)

    df_processed.to_csv(output_file, index=False)

if __name__ == "__main__":
    process_bank_data()