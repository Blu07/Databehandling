import matplotlib.pyplot as plt

def plotLinje(data, aar):
    plt.figure(figsize=(16,9))
    for d in data:
        plt.plot(aar, d, ".-")
    plt.grid()
    plt.show()

