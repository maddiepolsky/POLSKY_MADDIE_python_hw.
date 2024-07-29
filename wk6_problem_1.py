import random

def sums (X,Y):
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_xy = sum(x*y for x,y in zip(X,Y))
    sum_x_squared = sum(x**2 for x in X)
    return n, sum_x, sum_y, sum_xy, sum_x_squared

def linear_regression (X,Y):
    n, sum_x, sum_y, sum_xy, sum_x_squared = sums(X,Y)
    theta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    theta_2 = (sum_y - theta_1 * sum_x) / n
    return theta_1, theta_2
def mean_squared_error(y_true, y_pred):
    mse = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)
    return mse
def train_test_split(X, Y, test_size=0.25, random_state=None):
    if random_state:
        random.seed(random_state)
    combined = list(zip(X, Y))
    random.shuffle(combined)
    X[:], Y[:] = zip(*combined)
    split_index = int(len(X) * (1 - test_size))
    return X[:split_index], X[split_index:], Y[:split_index], Y[split_index:]

def main(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    theta_1, theta_2 = linear_regression(X_train, Y_train)
    Y_train_pred = [theta_1 * x + theta_2 for x in X_train]
    Y_test_pred = [theta_1 * x + theta_2 for x in X_test]
    mse_train = mean_squared_error(Y_train, Y_train_pred)
    mse_test = mean_squared_error(Y_test, Y_test_pred)
    print(f"Learned parameters: theta_1 = {theta_1}, theta_2 = {theta_2}")
    print(f"MSE over the training dataset: {mse_train}")
    print(f"MSE over the evaluation dataset: {mse_test}")


#test case
X = [i for i in range(20)]  # X values
Y = [3 * x + 7 + random.uniform(-1, 1) for x in X]  # Y values with some noise

main(X, Y)