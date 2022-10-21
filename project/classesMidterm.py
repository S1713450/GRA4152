##########
### Import libraries
import numpy as np
import csv
from sklearn import preprocessing as pp
from random import sample, seed
from scipy.optimize import minimize
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn import metrics

##########
### DataSet class (superclass)
### Takes data as numpy arrays
### Option to do MinMaxScaling on x
### @param x the explanatory variables
### @param y the dependent variable
### @param scale_x the scaling option, default is False
### @param transposed if data transposed or not, default is False
class DataSet:
    ### Constructor
    def __init__(self, x: np.ndarray, y: np.ndarray, scale_x = False, transposed = False) -> None:
        # Verify that x and y are numpy arrays
        # Raises Exception if they are not
        # Otherwise, proceed
        if not isinstance(x, np.ndarray):
            raise Exception("x must be numpy array")
        if not isinstance(y, np.ndarray):
            raise Exception("y must be numpy array")
    
        # Protected instance variables
        self._x = x
        self._y = y
        self._xtrain = None
        self._xtest = None
        self._ytrain = None
        self._ytest = None
        
        # Transposed: if rows are covariates and columns observations
        # Not transposed: if rows observations and columns covariates
        if transposed is False:
            # Scale x if scale_x is True
            if scale_x is True:
                # Apply MinMaxScaler
                self._x = pp.MinMaxScaler().fit_transform(self._x)
            # Transpose x and y
            self._x = self._x.T
            self._y = self._y.T
        # User enters "y" (a yes)
        if transposed is True:
            # Scale x if scale_x is True
            if scale_x is True:
                # Transpose x before applying MinMaxScaler, then apply MinMaxScaler and transpose it back again
                self._x = pp.MinMaxScaler().fit_transform(self._x.T).T

    ### Add a constant to the x data
    def add_constant(self) -> None:
        # If the x data does not have a vector of ones
        if not np.mean(self._x[0,:]) == 1 and not np.std(self._x[0,:]) == 0:
            # Create a transposed array of ones
            ones = np.ones(self._x.shape[1], dtype = "float32").T
            # Stack ones with the x data
            self._x = np.vstack([ones, self._x])
        # If the x data does have a vector of ones
        else:
            raise Exception("The dataset already has a constant added")

    ### Train-test splitting
    def train_test(self, seed_value = None, train_size = 0.70) -> None:
        if train_size > 1 or train_size < 0:
            raise Exception("Training size must be >0 and <1!")
        seed(seed_value)
        l = self._model.shape[1] # get the length of the stacked data
        tr = round(l * train_size) # we want ~70% as training data
        indices_train = sample(range(l), tr) # get random indices for traning data
        train_data = self._model[:, indices_train] # extract random training data
        indices_test = [i for i in range(l) if i not in indices_train] # indices not for training
        test_data = self._model[:, indices_test] # exctract random testing data
        self._xtrain = train_data[1:len(train_data), :] # training data for x is row 1 to last row
        self._xtest  = test_data[1:len(train_data), :] # testing data for x is row 1 to last row
        self._ytrain = train_data[0, :] # training data for y is row 0
        self._ytest  = test_data[0, :] # testing data for y is row 0

    ### Get x data
    @property
    def x(self) -> np.ndarray:
        return self._x
    
    ### Get y data
    @property
    def y(self) -> np.ndarray:
        return self._y
    
    ### Get x training data
    @property
    def x_tr(self) -> np.ndarray:
        return self._xtrain

    ### Get y training data
    @property
    def y_tr(self) -> np.ndarray:
        return self._ytrain

    ### Get x testing data
    @property
    def x_te(self) -> np.ndarray:
        return self._xtest

    ### Get y testing data
    @property
    def y_te(self) -> np.ndarray:
        return self._ytest

##########
### csvDataSet class (a subclass of DataSet)
### Reads a csv and returns a numpy array
class csvDataSet(DataSet):
    ### Constructor
    def __init__(self):
        pass

    ### Read a csv file
    ### @param file the location of the file
    def read(self, file: str) -> np.ndarray:
        # Check if string
        if not isinstance(file, str):
            raise Exception("file must be a string!")
        # Open, read, convert to list, and finally numpy array
        raw = open(file, "rt")
        reader = csv.reader(raw, delimiter=",", quoting=csv.QUOTE_NONE)
        x = list(reader)
        data = np.array(x).astype("float32")
        return data

##########
### LM class (superclass)
### LM specifies a model, returns parameters and the specified model
### It also has a summary, a repr method, and a optimize function
### Fit, predict, and diagnosis are abstract methods
class LM:
    ### Constructor
    def __init__(self) -> None:
        """
        _model: x and y stacked as np.ndarray
        _fitted: result from optimizer
        _params: coefficients minimizing the objective function
        _text: specified model as a string
        _indices: indices for coefficient numbers
        _mui: predicted mean vector
        _train: placeholder for True: training dataset or False: test set
        """
        # Protected instance variables
        self._model = None
        self._fitted = None
        self._params = None
        self._text = ""
        self._indices = None
        self._mui = None
        self._train = None
    
    ### Linear model method for specifying the model
    ### @text the model as a string
    def linearModel(self, text: str) -> np.ndarray:
        """
        Convention is to write: "dependent variable ~ intercept + coefficients*covariates"
        y: dependent variable
        b0: intercept
        b1, b2, ..., bn: coefficients
        x1, x2, ..., xn: covariates
        Examples:
        With intercept: "y ~ b0 + b1*x1 + b2*x2"
        Without intercept: "y ~ b1*x3 + b2*x5"
        """
        indices = []
        split = text.lower()
        self._text = text
        if "b0" in split:
            if np.mean(self._x[0,:]) == 1 and np.std(self._x[0,:]) == 0:
                indices.append(0)
            else:
                raise Exception("x does not have a constant in the dataset, use add_constant method to add")
        for i in range(1, len(self.x)):
            if "x" + str(i) in split:
                indices.append(i)
        self._indices = indices
        data = self._x[indices,:]
        self._model = np.vstack([self._y, data])
        return self._model

    ### Method to fit the specified model
    ### An abstract method
    def fit(self) -> None:
        raise NotImplementedError("Not implemented!")

    ### Method to predict using the fitted coefficients
    ### An abstract method
    def predict(self) -> None:
        raise NotImplementedError("Not implemented!")
    
    ### Method to access the fitted parameters
    ### An accessor method using @property as decorator
    @property
    def params(self) -> np.ndarray:
        return self._params

    ### Method to optimize the objective function
    ### We want to minimize the deviance
    ### @param fit the objective function
    ### @param init_val the initial guesses for the coefficients
    def optimize(self, fit, init_val = 1) -> float:
        init_params = np.repeat(init_val, len(self._model) - 1)
        results = minimize(fit, init_params)
        self._params = results['x']
        return results.fun

    ### Method to return the specified model
    ### An accessor method using @property as decorator
    @property
    def model(self) -> str:
        if self._text is None:
            return print("You have not specified a model!")
        else:
            return self._text
    
    ### Method to get the accuracy of the model
    def diagnosis(self) -> float:
        raise NotImplementedError("Not implemented!")

    ### Method to return a string with fitted parameters
    def __repr__(self) -> str:
        # If called before specifying a model in the method linearModel
        if self._text is None:
            return print("I am a LinearModel.")
        # If called after specifying a model in the method linearModel
        else:
            info = "y ~ "
            # If parameters have not been fitted
            if self._params is None:
                # If there is an intercept
                if "b0" in self._text:
                    for i in range(len(self._indices)):
                        if i == 0:
                            info += str(0)
                        else:
                            info += " + " + str(0) + "*x" + str(self._indices[i])
                # If there is no intercept
                else: 
                    for i in range(len(self._indices)):
                        if i == 0:
                            info += str(0) + "*x" + str(self._indices[i])
                        else:
                            info += " + " + str(0) + "*x" + str(self._indices[i])
            # If parameters have been fitted
            else:
                par = np.around(self._params, 2)
                # If there is an intercept
                if "b0" in self._text:
                    for i in range(len(par)):
                        if i == 0:
                            info += str(par[i])
                        else:
                            if self._params[i] < 0:
                                info += " - " + str(abs(par[i])) + "*x" + str(self._indices[i])
                            else:
                                info += " + " + str(par[i]) + "*x" + str(self._indices[i])
                # If there is no intercept
                else:
                    for i in range(len(par)):
                        if i == 0:
                            info += str(par[i]) + "*x" + str(self._indices[i])
                        else:
                            if self._params[i] < 0:
                                info += " - " + str(abs(par[i])) + "*x" + str(self._indices[i])
                            else:
                                info += " + " + str(par[i]) + "*x" + str(self._indices[i])
        return info
    
    ### Method to print a summary of the fitted model
    ### Returns the model specified, fitted parameters, and accuracy
    ### An accessor method using @property as decorator
    @property
    def summary(self) -> None:
        print("")
        print(f"---------- Summary of linear model ----------")
        print("")
        print(f"Model specified:")
        print(f"{self.model}")
        print("")
        print(f"Fitted parameters:")
        print(f"{self.__repr__()}")
        print("")
        self.diagnosis()
        print("")
        print(f"---------------------------------------------")

##########
### LinearRegression class (subclass of LM)
### Takes data as numpy array
### Option to do MinMaxScaling on x
### @param x the explanatory variables
### @param y the dependent variable
### @param scale_x the scaling option, default is False
### @param transposed True if data transposed, False if not
class LinearRegression(LM, DataSet):
    # Constructor
    def __init__(self, x: np.ndarray, y: np.ndarray, scale_x = False, transposed = False) -> None:
        # Call the superclass constructors
        LM.__init__(self)
        DataSet.__init__(self, x, y, scale_x, transposed)
    
    ### Method to fit the specified model
    ### @param train whether to fit on full data or training set
    def fit(self, train = False) -> None:
        if train is False:
            deviance = lambda params: np.sum((self._model[0,:] - self._model[1:,:].T @ params)**2)
            self._fitted = LM.optimize(self, deviance)
        else:
            deviance = lambda params: np.sum((self.y_tr - self.x_tr.T @ params)**2)
            LM.optimize(self, deviance)
            self._fitted = np.sum((self.y_te - self.x_te.T @ self._params)**2)
        return self._fitted
    
    ### Method to predict using the fitted coefficients
    ### @param test whether to predict on full data, testing set, or training set
    def predict(self, test = False) -> np.ndarray:
        if self._params is None:
            return print("You need to fit the model first!")
        else:
            if test is False:
                self._mui = self._model[1:,:].T @ self._params
            else:
                self._mui = self.x_te.T @ self._params
            return self._mui
    
    ### Method to get the accuracy of the model (R2)
    ### @param test False if training set, True if test set
    def diagnosis(self, test = False) -> float:
        # If model not fitted
        if self._params is None:
            return print("You need to fit the model first")
        # If model is fitted
        else:
            # If constant is added: R2
            if np.mean(self._model[1,:]) == 1 and np.std(self._model[1,:]) == 0:
                # If not test set
                if test is False:
                    R2 = 1 - self.fit() / (np.var(self._model[0,:]) * self._model.shape[1])
                # If test set
                else:
                    R2 = 1 - self.fit(test = True) / (np.var(self.y_te) * len(self.y_te))
            # If constant not added: uncentered R2
            else:
                # If not test set
                if test is False:
                    R2 = 1 - self.fit() / np.sum(self.y**2)
                # If test set
                else:
                    R2 = 1 - self.fit(test = True) / np.sum(self.y_te**2)
        return print(f"R2: {round(R2, 2)}")

##########
### LogisticRegression class (subclass of LM)
### Takes data as numpy array
### Option to do MinMaxScaling on x
### @param x the explanatory variables
### @param y the dependent variable
### @param scale_x the scaling option, default is False
### @param transposed True if data transposed, False if not
class LogisticRegression(LM, DataSet):
    ### Constructor
    def __init__(self, x: np.ndarray, y: np.ndarray, scale_x = False, transposed = False) -> None:
        # Call the superclass constructors
        LM.__init__(self)
        DataSet.__init__(self, x, y, scale_x, transposed)
    
    ### Method to fit the specified model
    ### @param train whether to fit on full data or training set
    def fit(self, train = False) -> None:
        self._train = train
        if self._train is False:
            deviance = lambda params: np.sum(np.log(1 + np.exp(self._model[1:,:].T @ params)) - self._model[0,:] * (self._model[1:,:].T @ params))
            self._fitted = LM.optimize(self, deviance)
        else:
            deviance = lambda params: np.sum(np.log(1 + np.exp(self.x_tr.T @ params)) - self.y_tr * (self.x_tr.T @ params))
            LM.optimize(self, deviance)
            self._fitted = np.sum(np.log(1 + np.exp(self.x_te.T @ self._params)) - self.y_te * (self.x_te.T @ self._params))
        return self._fitted
    
    ### Method to predict using the fitted coefficients
    ### @param test whether to predict on full data, testing set, or training set
    def predict(self, test = "all") -> np.ndarray:
        test.lower()
        if self._params is None:
            return Exception("You need to fit the model first!")
        else:
            if test is "all":
                self._mui = np.exp(self._model[1:,:].T @ self._params) / (1 + np.exp(self._model[1:,:].T @ self._params))
            if test is "test":
                self._mui = np.exp(self.x_te.T @ self._params) / (1 + np.exp(self.x_te.T @ self._params))
            if test is "train":
                self._mui = np.exp(self.x_tr.T @ self._params) / (1 + np.exp(self.x_tr.T @ self._params))
        if self._mui is None:
            return Exception("Enter either all, train or test!")
        return self._mui

    ### Method to get the accuracy of the model (AUC)
    ### @param test False if training set, True if test set
    def diagnosis(self) -> float:
        if self._params is None:
            return print("You need to fit the model first!")
        else:
            if self._train is False:
                auc = roc_auc_score(self._model[0,:], self.predict())
                return print(f"AUC: {round(auc, 2)}")
            else:
                auc_te = roc_auc_score(self.y_te, self.predict("test"))
                auc_tr = roc_auc_score(self.y_tr, self.predict("train"))
                auc = roc_auc_score(self._model[0,:], self.predict())
                return print(f"AUC full: {round(auc, 2)} | AUC test: {round(auc_te, 2)} | AUC train: {round(auc_tr, 2)}")

##########
### DiagnosticPlot
### Returns a plot for y vs mu
### Either for LinearRegression or for LogisticRegression
### @param OLS True if linear regression, False is logistic regression
class diagnosticPlot:
    SCATTER_SIZE = 10
    ### Constructor
    def __init__(self, model):
        if "Logistic" in str(type(model)):
            self._modelType = "Logistic"
        if "Linear" in str(type(model)):
            self._modelType = "Linear"
    
    ### Method used to plot y vs mu
    ### @param y the dependent variable vector
    ### @param mu the vector with predictions
    def plot(self, y: np.ndarray, mu: np.ndarray) -> plt.scatter:
        if self._modelType == "Linear":
            plt.scatter(y, mu, s = diagnosticPlot.SCATTER_SIZE)
            plt.title("y vs prediction")
            plt.xlabel("Prediction")
            plt.ylabel("y")
            plt.show()
        else:
             fpr, tpr, thresholds = metrics.roc_curve(y, mu)
             roc_auc = metrics.auc(fpr, tpr)
             display = metrics.RocCurveDisplay(fpr = fpr, tpr = tpr, roc_auc = roc_auc, estimator_name ='ROC curve')
             display.plot()
             plt.show()