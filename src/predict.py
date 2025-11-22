import pandas as pd
import joblib
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def predict_churn():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    model_path = os.path.join(project_root, 'models', 'bank_churn_model.pkl')

    if not os.path.exists(model_path):
        logger.error("Modelo não encontrado. Treine primeiro!")
        return
    
    model = joblib.load(model_path)
    logger.info("Modelo bancário carregado com sucesso!")

    new_customer = {
        'CreditScore': 600,
        'Age': 40,
        'Tenure': 3,
        'Balance': 60000.0,
        'NumOfProducts': 2,
        'HasCrCard': 1,
        'IsActiveMember': 1,
        'EstimatedSalary': 50000.0,
        'Complain': 1,
        'Satisfaction Score': 3,
        'Point Earned': 500,
        
        'Geography': 'Germany',
        'Gender': 'Male',
        'Card Type': 'GOLD'
    }

    
    df_input = pd.DataFrame([new_customer])

    df_final = pd.DataFrame()
    
    numeric_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                    'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Complain', 
                    'Satisfaction Score', 'Point Earned']
    
    for col in numeric_cols:
        df_final[col] = df_input[col]

    df_final['Geography_Germany'] = 1 if new_customer['Geography'] == 'Germany' else 0
    df_final['Geography_Spain'] = 1 if new_customer['Geography'] == 'Spain' else 0
    
    df_final['Gender_Male'] = 1 if new_customer['Gender'] == 'Male' else 0
    
    df_final['Card Type_GOLD'] = 1 if new_customer['Card Type'] == 'GOLD' else 0
    df_final['Card Type_PLATINUM'] = 1 if new_customer['Card Type'] == 'PLATINUM' else 0
    df_final['Card Type_SILVER'] = 1 if new_customer['Card Type'] == 'SILVER' else 0

    prediction = model.predict(df_final)[0]
    probability = model.predict_proba(df_final)[0][1]

    logger.info("\n" + "="*40)
    logger.info("      RELATÓRIO DE RISCO BANCÁRIO      ")
    logger.info("="*40)
    
    if prediction == 1:
        logger.info("STATUS: ALTO RISCO DE CHURN")
        logger.info(f"Probabilidade de Saída: {probability:.1%}")
        logger.info(f"Capital em Risco (Saldo): ${new_customer['Balance']:,.2f}")
        logger.info("Ação Sugerida: Ligar imediatamente e resolver reclamações.")
    else:
        logger.info("STATUS: CLIENTE SEGURO")
        logger.info(f"Probabilidade de Saída: {probability:.1%}")
        logger.info("Ação Sugerida: Oferecer produtos de investimento.")
    
    logger.info("="*40 + "\n")

if __name__ == "__main__":
    predict_churn()