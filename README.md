# INF1038
## PUC-Rio 2023.2

João Pedro Cunha 1910626    
Bruno Ramos 1911499

Neste relatório, exploraremos a base do Keggle chamada Adult Income, que tenta descrever os salários
de diversas pessoas a partir de sua idade, nível de escolaridade, gênero, ocupação etc. O código em 
Python adult.py realiza diversos estudos que serão explicados a seguir. Para rodá-lo, basta instalar 
as devidas bibliotecas como exemplificado abaixo:

```bash
    pip install pandas
    pip install matplotlib
    pip install seaborn
    pip install scipy
```

e executar através de 

```bash
    python adult.py
```


Este é um dataset muito utilizado para KNN, entretanto vamos focar apenas na análise exploratória 
deste conjunto de dados.

Primeiramente, tentamos identificar quais colunas apresentam a maior quantidade de dados nulos.
Criamos um gráfico de barras para nos mostrar as quantidades de nulos em cada coluna e identificamos
que as colunas workclass, ocupation e native-country são as únicas possuem dados faltantes, com destaque
às duas primeiras.

A seguir, tentamos fazer um gráfico de caixa para descrever as variações dos dados numericamente observáveis.
A análise estava severamente prejudicada pela coluna fn/wgt em razão das suas altas quantidades e outliers. A partir disso, normalizamos a coluna (dividimos cada valor pelo máximo valor da coluna) e os analisamos.
Pudemos concluir que as colunas de idade e nível educacional são bem mais esparsas, enquanto ganho/perda de capital
e horas por semana são bem mais concentradas.

A análise de idade e nível educacional nos trouxe insights interessantes. A distribuição de educação nos mostra
indivíduos com níveis bem maiores que outros, enquanto a distribuição etária nos mostra uma concentração de 
indivíduos em idades de trabalho.

Adicionalmente, realizamos uma análise para entender a relação entre nível educacional e salário, que revela 
uma alta correlação: indivíduos com um alto nível educacionam tendem a ter salários maiores.

Tentamos também tirar alguns insights através da criação de um Heatmap, que visualiza a relação entre
educação, idade e porcentagem de altos salários. A análise confirma que indivíduos com um alto nível educacional
possuem uma porcentagem maior de pessoas em classes mais altas.



