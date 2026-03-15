

import matplotlib.pyplot as plt
import numpy as np
from settings import COLORS

def plot_to_figure(fig, data, aar, rom_soner_index, show_legend: bool = False, show_grid: bool = True, show_axis_labels: bool = True, show_average: bool = False, y_lim_zero: bool = False, title: str = "Plot", x_label: str = "X-axis", y_label: str = "Y-axis"):
    
    # Sett None til np.nan
    for rom in range(len(data)):
        for soner in range(len(data[rom])):
            for aar_ in range(len(data[rom][soner])):
                if data[rom][soner][aar_] == None:
                    data[rom][soner][aar_] = np.nan

   #plott hver linje i data
    ax = fig.add_subplot(111)
    colors = [
        "#f50000",
        "#f9ec00",
        "#ed0aea",
        "#0e7d08",
        "#5A28BE",
        "#412034",
        "#fb5607",
        "#f01a6c",
        "#3a86ff",
    ]
    
    rom_sone_i = 0
    for rom in data:
        for sone in rom:            
            ax.plot(aar, sone, ".-", color=colors[rom_sone_i%len(colors)], label=f"{rom_soner_index[rom_sone_i]}")

            if show_average:
                avg = np.nanmean(sone)
                ax.hlines(avg, aar[0], aar[-1], colors=colors[rom_sone_i%len(colors)], linestyle="--")
    
            rom_sone_i += 1

    if show_grid: plt.grid()
    if show_legend: plt.legend()
    if show_axis_labels:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    if y_lim_zero: plt.ylim(bottom=0)
    
    plt.title(title)
    
