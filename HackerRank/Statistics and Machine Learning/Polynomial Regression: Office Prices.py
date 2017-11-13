from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# EXTRACT DATA
feature_count, row_count = map(int, input().strip().split())
training_feature, training_class, testing_feature = [], [], []
for _ in range(row_count):
    training_vector = list(map(float, input().strip().split()))
    training_feature.append(training_vector[:-1])
    training_class.append(training_vector[-1])
for _ in range(int(input())):
    testing_vector = list(map(float, input().strip().split()))
    if len(testing_vector) > 1:
        testing_feature.append(testing_vector)

# TRANSFORM FEATURES
poly = PolynomialFeatures(degree=3)
processed_training_feature = poly.fit_transform(training_feature)

# BUILD MODEL
model = LinearRegression().fit(processed_training_feature, training_class)
testing_processed = poly.fit_transform(testing_feature)

# PREDICT OUTPUT
predictions = model.predict(testing_processed)
for prediction in predictions:
    print(prediction)
