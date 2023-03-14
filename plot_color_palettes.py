# %% imports

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

# user variables
my_xlim = (-0.5, 12)
my_ylim = (-7, 109)


# plot and label cycle
def do_plot():
    # get cycle colors
    cycle_colors = [y["color"] for y in list(plt.rcParams["axes.prop_cycle"])]

    # add lines to plot
    for i in range(10):
        (line,) = ax.plot(j, i * (j + 1))
        ax.plot(j, i * (j + 1), color=line.get_color())
        ax.text(10.1, 1.1 * i * j[-1] - 2, cycle_colors[i], color=cycle_colors[i])


# define figure
fig = plt.figure()
ax = plt.subplot(2, 1, 1)

# define range
j = np.arange(11)

# matplotlib default color cycle
# https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html#colors-color-cycles-and-colormaps

do_plot()

ax.set_xlim(my_xlim)
ax.set_ylim(my_ylim)
# set xticks empty for second plot label
ax.set_xticks([])
ax.set_title("Matplotlib v2.0+ (original Tableau 10) color palette")

# updated tableau 10 color palette
# https://www.tableau.com/blog/colors-upgrade-tableau-10-56782

# NOTE: overriding color cycle requires loading Matplotlib
# from scratch to return to default colors
plt.rcParams["axes.prop_cycle"] = cycler(
    "color",
    [
        "#4e79a7",
        "#f28e2b",
        "#e15759",
        "#76b7b2",
        "#59a14f",
        "#edc948",
        "#b07aa1",
        "#ff9da7",
        "#9c755f",
        "#bab0ac",
    ],
)

# define second subplot
ax = plt.subplot(212)

do_plot()

ax.set_xlim(my_xlim)
ax.set_ylim(my_ylim)
ax.set_title("New Tableau 10 color palette")

plt.savefig("tableau_10_original_new.png")

# %%
