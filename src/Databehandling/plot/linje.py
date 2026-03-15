import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_to_figure(fig, data, aar, show_legend: bool = False, show_grid: bool = True, show_axis_labels: bool = True, show_average: bool = False, y_lim_zero: bool = False, title: str = "Plot", x_label: str = "X-axis", y_label: str = "Y-axis"):
    print(data)
    for rom in range(len(data)):
        for soner in range(len(data[rom])):
            for s in range(len(data[rom][soner])):
                if data[rom][soner][s] == None:
                    data[rom][soner][s] = np.nan

    print(data)
    ax = fig.add_subplot(111)
    for rom in data:
        for d in rom:
            # print(aar,d)
            ax.plot(aar, d, ".-", label=f"{rom.index(d)+1} rom")
            
            if show_average:
                avg = np.nanmean(d)
                ax.hlines(avg, aar[0], aar[-1], "Red", linestyle="--")
    

    if show_grid: plt.grid()
    if show_legend: plt.legend()
    if show_axis_labels:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    if y_lim_zero: plt.ylim(bottom=0)
    
    plt.title(title)


