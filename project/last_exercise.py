
# Import classes
from classesMidterm import LM, LinearRegression, LogisticRegression, diagnosticPlot, DataSet, csvDataSet
# Import statsmodels.api as sm used to load the spector dataset
import statsmodels.api as sm

import argparse as arg

parser = arg.ArgumentParser(
                    prog = 'LogisticRegression',
                    description = 'Computes a logistic regression',
                    epilog = 'End of program')

parser.add_argument('-t','--trainSize', type=float, default=0.7, metavar='', help=' Between 0 and 1, specifies train size, default is 0.7, type: float')
parser.add_argument('-r','--randomSeed',type=int, default=12345, metavar='', help='Specifies random seed, 12345 is default. Type: integer')
parser.add_argument('-m', '--make_plot', action = 'store_true', help= 'type -m to make a plot')
parser.add_argument('-c','--Covariates', required=True, nargs='*', default=[], metavar='', help='Example: b0 + b1*x1 +b2*x2')

test = parser.parse_args()


# Load the spector dataset
spector_data = sm.datasets.spector.load()
# Assign x and y
x = spector_data.exog # rows=32 x columns=3
y = spector_data.endog # rows=32 x columns=1

# Instantiate three models as LogisticRegression objects feeding x and y, no scaling, and dataset is not transposed
model = LogisticRegression(x, y, scale_x = False, transposed = False)


# Add constant by using .add_constant() method
model.add_constant()


# Specifying the models as a string using .linearModel() method
model.linearModel("y~" + " ".join(test.Covariates))

# Split into a training and testing set 
model.train_test(seed_value = test.randomSeed , train_size = test.trainSize )

# Fitting  models using .fit() method
model.fit(train = True)


# Get summary of all models using .summary method (accessor with decorator/@property)
model.summary


if test.make_plot:
    plot = diagnosticPlot(model)
    plot.plot(model.y_te, model.predict(test = "test"))
