from sklearn.linear_model import LinearRegression

def get_training_data(N):
    X, Y = [], []
    for _ in range(N):
        line = list(map(float, input().strip().split()))
        X, Y = X + [line[:-1]], Y + [line[-1]]
    return X, Y

def get_testing_data():
    t = int(input())
    return [list(map(float, input().strip().split())) for _ in range(t)]

def main():
    F, N = map(int, input().strip().split())
    X, Y = get_training_data(N)
    model = LinearRegression().fit(X, Y)
    for prediction in model.predict(get_testing_data()):
        print(round(prediction, 2))        

if __name__ == '__main__':
    main()
