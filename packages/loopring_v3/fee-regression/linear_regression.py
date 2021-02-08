import pandas as pd

dataset = pd.read_csv('block_stats.csv')
dataset.head()

# select data
X = dataset.iloc[:,2:].values
y = dataset.iloc[:,1].values

#print(X)
#print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting the model
from sklearn.linear_model import Lasso
regressor = Lasso(positive=True,max_iter=10000000)
regressor.fit(X_train, y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)

#print(regressor.coef_)

print("- noop_cost:           " + str(regressor.coef_[0]))
print("- deposit_cost:        " + str(regressor.coef_[1]))
print("- withdrawal_cost:     " + str(regressor.coef_[2]))
print("- transfer_cost:       " + str(regressor.coef_[3]))
print("- trade_cost:          " + str(regressor.coef_[4]))
print("- account_update_cost: " + str(regressor.coef_[5]))
print("- amm_update_cost:     " + str(regressor.coef_[6]))
print("- signature_cost:      " + str(regressor.coef_[7]))