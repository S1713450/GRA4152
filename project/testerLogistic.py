
# Import classes
from classesMidterm import LM, LinearRegression, LogisticRegression, diagnosticPlot, DataSet, csvDataSet
# Import statsmodels.api as sm used to load the spector dataset
import statsmodels.api as sm

# Load the spector dataset
spector_data = sm.datasets.spector.load()
# Assign x and y
x = spector_data.exog # rows=32 x columns=3
y = spector_data.endog # rows=32 x columns=1

# Instantiate three models as LogisticRegression objects feeding x and y, no scaling, and dataset is not transposed
model1 = LogisticRegression(x, y, scale_x = False, transposed = False)
model2 = LogisticRegression(x, y, scale_x = False, transposed = False)
model3 = LogisticRegression(x, y, scale_x = False, transposed = False)

# Add constant by using .add_constant() method
model1.add_constant()
model2.add_constant()
model3.add_constant()

# Specifying the three models as a string using .linearModel() method
model1.linearModel("y ~ b0 + b1*x1")
model2.linearModel("y ~ b0 + b1*x1 + b2*x2")
model3.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3")

# Split into a training and testing set using 70/30 for training/testing
model1.train_test(seed_value = 12345, train_size = 0.70)
model2.train_test(seed_value = 12345, train_size = 0.70)
model3.train_test(seed_value = 12345, train_size = 0.70)

# Fitting the three models using .fit() method
model1.fit(train = True)
model2.fit(train = True)
model3.fit(train = True)

# Get summary of all models using .summary method (accessor with decorator/@property)
model1.summary
model2.summary
model3.summary

# Plotting
plot1 = diagnosticPlot(model1)
plot1.plot(model1.y_te, model1.predict(test = "test"))

plot2 = diagnosticPlot(model2)
plot2.plot(model2.y_te, model2.predict(test = "test"))

plot3 = diagnosticPlot(model3)
plot3.plot(model3.y_te, model3.predict(test = "test"))