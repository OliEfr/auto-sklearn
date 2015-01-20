from HPOlibConfigSpace.configuration_space import ConfigurationSpace, \
    Configuration


from ..preprocessor_base import AutoSklearnPreprocessingAlgorithm

import numpy as np


class TFIDF(AutoSklearnPreprocessingAlgorithm):
    def __init__(self, random_state=None):
        #
        # This is implementation is for sparse data only! It will make inplace changes to the data!
        #
        # TODO: Define some meaningful parameter. Maybe some thresholding or so
        #		Should transform return X again?
        #		Should transform raise a NotImplementedError?
        #		'handles_multilabel'???
        self.idf = None
        self.random_state = random_state

    def fit(self, X, Y):
        #count the number of docmunts in which each word occurs 
        weights = (X>0.0).sum(axis=0)
        # words that never appear have to be treated differently!
        indices = np.ravel(np.where(weights == 0)[1])
        
        # calculate (the log of) the inverse document frequencies
        self.idf = np.array(np.log(float(X_train.shape[0])/(weights)))[0]
        # words that are not in the training data get will be set to zero
        self.idf[indices] = 0
        

        return self

    def transform(self, X):
        if self.idf is None:
            raise NotImplementedError()
        X.data *= self.idf[X.indices]
        return X

    @staticmethod
    def get_properties():
        return {'shortname': 'TFIDF',
                'name': 'Term Frequency (times) Inverse Document Frequency',
                'handles_missing_values': False,
                'handles_nominal_values': False,
                'handles_numerical_features': True,
                'prefers_data_scaled': False,
                'prefers_data_normalized': False,
                'handles_regression': False,
                'handles_classification': True,
                'handles_multiclass': True,
                'handles_multilabel': None,
                'is_deterministic': True,
                'handles_sparse': True,
                # TODO find out what is best used here!
                'preferred_dtype': np.float32}

    @staticmethod
    def get_hyperparameter_search_space(dataset_properties=None):
        cs = ConfigurationSpace()
        return cs

    def __str__(self):
        name = self.get_properties()['name']
        return "AutoSklearn %" % name
