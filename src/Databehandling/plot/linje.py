import matplotlib.pyplot as plt

def plotLinje(data, aar):
    plt.figure(figsize=(16,9))
    for rom in data:
        for d in rom:
            print(aar,d)
            plt.plot(aar, d, ".-")
    plt.grid()
    plt.show()


