# Bank Customer Churn Prediction

Este projeto consiste em uma solução de Machine Learning para identificar padrões de comportamento de clientes bancários que antecedem o cancelamento (churn), permitindo ações preventivas de retenção.
O foco é analisar o impacto de **fatores financeiros** (Saldo, Salário, Score de Crédito) e **demográficos** na retenção de clientes.

## Status do Projeto: Fase de Análise Exploratória (EDA)

Atualmente, o projeto encontra-se na etapa de **Data Understanding**. 
Foi realizada a limpeza dos dados brutos e análises estatísticas para levantar hipóteses de negócio.

### Principais Descobertas (Até Agora)

Durante a análise exploratória, descobrimos que o perfil de quem sai do banco é bem específico:

1.  **O Fator "Reclamação" (`Complain`):** Identificada uma correlação fortíssima (quase regra) entre clientes que reclamam e o cancelamento. Isso sugere uma falha grave na resolução de problemas no primeiro contato.
2.  **Fator Idade (`Age`):** Ao contrário do esperado, clientes mais velhos tendem a sair mais do que os jovens, indicando possível perda de atratividade para clientes financeiramente maduros.
3.  **Engajamento Retém:** Clientes marcados como "Membros Ativos" (`IsActiveMember`) têm taxas de evasão significativamente menores.
