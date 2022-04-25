# Recession Predictor - Phase 3 Project


## Navigating this Repo
The project is broken up into three main notebooks, in chronological order:

1. Data cleaning: This notebook makes the necessary API calls to the Nasdaq Datalink and imports local data. It then performs the necessary joins and saves the prepared DataFrame as a .csv file to be used in the model tuning notebook.

2. Model tuning: This notebook focuses on testing the different models against each other and determining a winner. It also creates visualizations to better understand model performance and

3. Simulation: This notebook takes the probability outputs of recession from 1963-2022 and uses it to simulate a basic portfolio strategy. The simulation takes that probability and "purchases" Dow Jones shares according to the probability that there will not be a recession, and purchases gold according to the probability that there will be a recession. This portfolio is updated quartely, as that is when new economic leading indicators come in to update the next model.



## Overview
The overall goal of the project was to see if we could predict future recessions using reliable, long-term economic metrics. We scoped the problem to ask specifically whether we could predict a recession in the next fiscal quarter.

## Business Problem
There are many reasons to attempt to predict a recession, as recessions generally are accompanied by unemployment, inflation, downturn in markets, and generally poor economic conditions for the country experiencing it. Therefore, if a recession can be predicted, preparations can be made to lessen the impact, thereby increasing profits in the long run for investors, or increasing job retention for governments.

## Methods
We considered several different models for this problem, but determined that the random forest classifier created the most robust model for predicting recessions at various lengths of time into the future. The Receiver-Operator Characteristic curve, a key metric for classification models, is displayed below for our top three models. Note that XGBoost performed better on this metric than the random forest, but tended to over-fit the data in other metrics.

![](/figures/ROC.png)

Using the random forest model, the simulation results are shown below which compare using our model to invest in an aggressive asset (in this case the Dow) versus a more conservative asset (in this case gold, which typically performs relatively well during recessions). The ratio of aggressive to conservative assets is determined by the prediction probability of a recession, and is updated quarterly. The image on the bottom shows the logarithmic of the same graph, which highlights the fact that most of the increase in performance of the predictor versus only investing in the Dow comes from the fact that the predictor correctly predicted the 2008 recession and the associated market downturn associated with it.

![](/figures/StockSim.png)

![](/figures/StockSimLog.png)

