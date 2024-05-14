import numpy as np
import matplotlib.pyplot as plt
def datasetGenerator(x: int) -> int:
    return ((2 * x) - 3) + np.random.normal(0, 5)
def meanSquaredError(y: float, y_pred: float) -> float:
    return sum((y - y_pred) ** 2 / len(y))
def gradientDescent(X: list[float],Y: list[float],Y_pred: list[float],B0: float,B1: float,learningRate: float,):
    B0 -= learningRate * np.mean(-2 * (Y - Y_pred))
    B1 -= learningRate * np.mean(2 * (Y - Y_pred) * (-X))
    return B0, B1
def betaCalculation(X: list[float], Y: list[float], n: int) -> int:
    Xtrans = [np.power(X, i) for i in range(n + 1)]
    Xnew = np.transpose(Xtrans)
    XTX = np.matmul(Xtrans, Xnew)
    XTXm1 = np.linalg.inv(XTX)
    XTXinvintoXT = np.matmul(XTXm1, Xtrans)
    Beta = np.matmul(XTXinvintoXT, Y)
    return Beta
def main():
    X = np.linspace(-5, 5, 10000)
    Y = datasetGenerator(X)
    B0 = np.random.normal(0, 1)
    B1 = np.random.normal(0, 1)
    B = [[B0, B1]]
    flag = True
    Yvals = Y
    epsarr = []
    epochsarr = []
    epochs = 0
    while flag:
        Y_pred = B0 + B1 * X
        if meanSquaredError(Yvals, Y_pred) <= 1e-6:
            flag = False
        eps = meanSquaredError(Y, Y_pred)
        B0, B1 = gradientDescent(X, Y, Y_pred, B0, B1, learningRate=0.01)
        B.append([B0, B1])
        Yvals = Y_pred
        epochs += 1
        epsarr.append(eps)
        epochsarr.append(epochs)
    print(B[-1])
    print(betaCalculation(X, Y, 1))
    #plt.show()
if __name__ == "__main__":
    main()
