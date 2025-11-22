# Bank Customer Churn Prediction

Este projeto consiste em uma solução de Machine Learning para identificar padrões de comportamento de clientes bancários que antecedem o cancelamento (churn), permitindo ações preventivas de retenção.
O foco é analisar o impacto de **fatores financeiros** (Saldo, Salário, Score de Crédito) e **demográficos** na retenção de clientes.

## Status do Projeto:

Atualmente, encontra-se na etapa de construção e validação do pipeline completo, incluindo:

- Processamento automático dos dados (ETL)
- Preparação de features (One-Hot Encoding)
- Treinamento do modelo (Random Forest)
- Salvamento e versionamento do modelo
- Implementação do script de inferência para uso real

### Principais Descobertas

Durante a análise exploratória, descobrimos que o perfil de quem sai do banco é bem específico:

1.  **O Fator "Reclamação" (`Complain`):** Identificada uma correlação fortíssima (quase regra) entre clientes que reclamam e o cancelamento. Isso sugere uma falha grave na resolução de problemas no primeiro contato.
2.  **Fator Idade (`Age`):** Ao contrário do esperado, clientes mais velhos tendem a sair mais do que os jovens, indicando possível perda de atratividade para clientes financeiramente maduros.
3.  **Engajamento Retém:** Clientes marcados como "Membros Ativos" (`IsActiveMember`) têm taxas de evasão significativamente menores.

## Estrutura do Projeto

A organização foi evoluída para suportar o fluxo completo de processamento, treinamento e inferência:

- **src/**: scripts principais (processamento, treinamento, inferência)  
- **data/**: dados brutos e tratados  
- **models/**: modelos treinados (arquivos .pkl)

---

## Pipeline de ETL

O módulo `src/process_data.py` executa:

- Limpeza, padronização e validação dos dados.  
- Implementação de One-Hot Encoding para transformar variáveis categóricas (como país e gênero) em variáveis numéricas compatíveis com modelos supervisionados.  
- Geração de um dataset final pronto para modelagem.

---

## Pipeline de Treinamento do Modelo

O módulo `src/train_model.py` inclui:

- Treinamento de um **Random Forest Classifier**.  
- Acurácia superior a 99%, impactada majoritariamente pelo fator de reclamação.  
- Salvamento automático do modelo final usando `joblib`, armazenado em `models/`.

---

## Fase de Inferência (Uso Real)

O módulo `src/predict.py` fornece:

- Um simulador de previsão para novos clientes.  
- Tratamento automático de variáveis categóricas, garantindo que entradas como “Germany” sejam convertidas para seus respectivos indicadores (`Geography_Germany = 1`).  
- Uma camada adicional de análise financeira, onde o script não apenas informa a probabilidade de churn, mas também estima o valor financeiro em risco com base no saldo do cliente.