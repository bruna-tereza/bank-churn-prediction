import pandas as pd
import os
import joblib
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def train_bank_model():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(project_root, 'data', 'churn_processed.csv')
    model_output = os.path.join(project_root, 'models', 'bank_churn_model.pkl')

    os.makedirs(os.path.dirname(model_output), exist_ok=True)

    if not os.path.exists(input_file):
        logger.error(f"Arquivo {input_file} não encontrado. Execute src/process_data.py antes.")
        return

    try:
        df = pd.read_csv(input_file)
        logger.info(f"Dados carregados. Shape: {df.shape}")
    except Exception as e:
        logger.error(f"Erro ao ler o CSV: {e}")
        return

    X = df.drop('Exited', axis=1)
    y = df['Exited']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logger.info(f"Divisão concluída: {X_train.shape[0]} treino, {X_test.shape[0]} teste.")

    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    logger.info(f"ACURÁCIA FINAL: {acc:.2%}")
    
    print("\n--- Relatório de Classificação ---")
    print(classification_report(y_test, y_pred))
    
    print("--- Matriz de Confusão ---")
    print(confusion_matrix(y_test, y_pred))
    print("\n")

    try:
        joblib.dump(rf_model, model_output)
        logger.info(f"Modelo salvo em: {model_output}")
    except Exception as e:
        logger.error(f"Erro ao salvar o modelo: {e}")

if __name__ == "__main__":
    train_bank_model()