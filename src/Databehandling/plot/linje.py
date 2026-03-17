

import matplotlib.pyplot as plt
import numpy as np
from settings import COLORS

def plot_to_figure(
    fig,
    data:list,
    aar:list,
    rom_soner_index,
    show_legend: bool = False,
    show_grid: bool = True,
    show_axis_labels: bool = True,
    show_average: bool = False,
    y_lim_zero: bool = False,
    show_inflation: bool = False,
    title: str = "Plot",
    x_label: str = "X-axis",
    y_label: str = "Y-axis"
):
    """_summary_

    Args:
        fig (_type_): _description_
        data (_type_): _description_
        aar (_type_): _description_
        rom_soner_index (_type_): _description_
        show_legend (bool, optional): _description_. Defaults to False.
        show_grid (bool, optional): _description_. Defaults to True.
        show_axis_labels (bool, optional): _description_. Defaults to True.
        show_average (bool, optional): _description_. Defaults to False.
        y_lim_zero (bool, optional): _description_. Defaults to False.
        show_inflation (bool, optional): _description_. Defaults to False.
        title (str, optional): _description_. Defaults to "Plot".
        x_label (str, optional): _description_. Defaults to "X-axis".
        y_label (str, optional): _description_. Defaults to "Y-axis".
    """

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
        "#5A28BE",
        "#0e7d08",
        "#412034",
        "#ed0aea",
        "#fb5607",
        "#f01a6c",
        "#3a86ff",
        "#f9ec00",
    ]
    
    rom_sone_i = 0
    for rom in data:
        for sone in rom:     
            
            use_index = rom_sone_i % len(colors)
                   
            ax.plot(aar, sone, ".-", color=colors[use_index], label=f"{rom_soner_index[rom_sone_i]}")

            if show_average:
                # Legg til linje for gjennomsnitt
                avg = np.nanmean(sone)
                ax.hlines(avg, aar[0], aar[-1], colors=colors[use_index], linestyle="--")
                
            if show_inflation:
                # Legg til linje for inflasjons
                inflasjon = 0.025  # 2.5% årlig inflasjon
                priser = np.array(sone)
                for i in range(1, len(priser)):
                    priser[i] = priser[i-1] * (1 + inflasjon)
                ax.plot(aar, priser, "-", color=colors[use_index])
        
            rom_sone_i += 1

    if show_grid: plt.grid()
    if show_legend: plt.legend()
    if show_axis_labels:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    if y_lim_zero: plt.ylim(bottom=0)
    
    plt.title(title)
    
