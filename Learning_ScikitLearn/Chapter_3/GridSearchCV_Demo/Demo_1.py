# -*- coding: utf-8 -*-

# @Time  : 2019/12/15 15:13

# @Author : Mr.Lin

'''

Parameter estimation using grid search with cross-validation

'''


'''
This examples shows how a classifier is optimized by cross-validation, which is done using the sklearn.model_selection.GridSearchCV object on a development set that comprises only half of the available labeled data.

The performance of the selected hyper-parameters and trained model is then measured on a dedicated evaluation set that was not used during the model selection step.

More details on tools available for model selection can be found in the sections on Cross-validation: evaluating estimator performance and Tuning the hyper-parameters of an estimator.
'''



from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC

print(__doc__)

# Loading the Digits dataset
digits = datasets.load_digits()

# To apply an classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target

# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
    )
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()

# Note the problem is too easy: the hyperparameter plateau is too flat and the
# output model is the same for precision and recall with ties in quality.


'''
Parameter estimation using grid search with cross-validation


# Tuning hyper-parameters for precision

Best parameters set found on development set:

{'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}

Grid scores on development set:

0.983 (+/-0.015) for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
0.956 (+/-0.027) for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
0.985 (+/-0.014) for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
0.981 (+/-0.020) for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
0.985 (+/-0.014) for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
0.981 (+/-0.019) for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
0.985 (+/-0.014) for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
0.981 (+/-0.019) for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
0.976 (+/-0.002) for {'C': 1, 'kernel': 'linear'}
0.976 (+/-0.002) for {'C': 10, 'kernel': 'linear'}
0.976 (+/-0.002) for {'C': 100, 'kernel': 'linear'}
0.976 (+/-0.002) for {'C': 1000, 'kernel': 'linear'}

Detailed classification report:

The model is trained on the full development set.
The scores are computed on the full evaluation set.

             precision    recall  f1-score   support

          0       1.00      1.00      1.00        89
          1       0.97      1.00      0.98        90
          2       0.99      0.98      0.98        92
          3       1.00      0.99      0.99        93
          4       1.00      1.00      1.00        76
          5       0.99      0.98      0.99       108
          6       0.99      1.00      0.99        89
          7       0.99      1.00      0.99        78
          8       1.00      0.98      0.99        92
          9       0.99      0.99      0.99        92

avg / total       0.99      0.99      0.99       899


# Tuning hyper-parameters for recall

Best parameters set found on development set:

{'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}

Grid scores on development set:

0.982 (+/-0.016) for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
0.953 (+/-0.027) for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
0.984 (+/-0.016) for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
0.981 (+/-0.020) for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
0.984 (+/-0.016) for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
0.980 (+/-0.019) for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
0.984 (+/-0.016) for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
0.980 (+/-0.019) for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
0.974 (+/-0.005) for {'C': 1, 'kernel': 'linear'}
0.974 (+/-0.005) for {'C': 10, 'kernel': 'linear'}
0.974 (+/-0.005) for {'C': 100, 'kernel': 'linear'}
0.974 (+/-0.005) for {'C': 1000, 'kernel': 'linear'}

Detailed classification report:

The model is trained on the full development set.
The scores are computed on the full evaluation set.

             precision    recall  f1-score   support

          0       1.00      1.00      1.00        89
          1       0.97      1.00      0.98        90
          2       0.99      0.98      0.98        92
          3       1.00      0.99      0.99        93
          4       1.00      1.00      1.00        76
          5       0.99      0.98      0.99       108
          6       0.99      1.00      0.99        89
          7       0.99      1.00      0.99        78
          8       1.00      0.98      0.99        92
          9       0.99      0.99      0.99        92

avg / total       0.99      0.99      0.99       899
'''








