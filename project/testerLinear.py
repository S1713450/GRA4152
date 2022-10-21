
# Import classes
from classesMidterm import LM, LinearRegression, LogisticRegression, diagnosticPlot, DataSet, csvDataSet

# Instantiate the csvDataSet object
csv = csvDataSet()
# Read the csv file from the same local folder
csv = csv.read("real_estate.csv")
# Get x and y from the csv
x = csv[:, 1:csv.shape[0]] # row 1 to end
y = csv[:, 0] # row 0

# Instantiate three models as LinearRegression objects feeding x and y, with scaling, and dataset is not transposed
model1 = LinearRegression(x, y, scale_x = True, transposed = False)
model2 = LinearRegression(x, y, scale_x = True, transposed = False)
model3 = LinearRegression(x, y, scale_x = True, transposed = False)

# Add constant by using .add_constant() method
model1.add_constant()
model2.add_constant()
model3.add_constant()

# Specifying the three models as a string using .linearModel() method
model1.linearModel("y ~ b0 + b1*x2 + b2*x3 + b3*x4")
model2.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5")
model3.linearModel("y ~ b1*x1")

# Fitting the three models using .fit() method
model1.fit()
model2.fit()
model3.fit()

# Get summary of all models using .summary method (accessor with decorator/@property)
# Importing sm for checking results
import statsmodels.api as sm
model1.summary
sm.OLS(model1.y, model1.x[(0,2,3,4),:].T).fit()._results.params
sm.OLS(model1.y, model1.x[(0,2,3,4),:].T).fit()._results.rsquared
model2.summary
sm.OLS(model2.y, model2.x[(0,1,2,3,4,5),:].T).fit()._results.params
sm.OLS(model2.y, model2.x[(0,1,2,3,4,5),:].T).fit()._results.rsquared
model3.summary
sm.OLS(model3.y, model3.x[(1),:].T).fit()._results.params
sm.OLS(model3.y, model3.x[(1),:].T).fit()._results.rsquared

# Plotting
plot1 = diagnosticPlot(model1)
plot1.plot(model1.y, model1.predict())

plot2 = diagnosticPlot(model2)
plot2.plot(model2.y, model2.predict())

plot3 = diagnosticPlot(model3)
plot3.plot(model3.y, model3.predict())