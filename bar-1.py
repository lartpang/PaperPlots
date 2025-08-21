from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(1, 7)
ys = np.array([2.1, 1.8, 2.5, 1.9, 2.3, 2.0])
yerrs = np.array([0.2, 0.15, 0.25, 0.18, 0.22, 0.17])
# six samples with five data points
Y = np.array(
    [
        [1.8, 2.0, 2.3, 2.2, 1.9],
        [1.6, 1.9, 1.7, 1.8, 2.0],
        [2.3, 2.6, 2.4, 2.5, 2.7],
        [1.7, 1.9, 2.0, 1.8, 2.1],
        [2.1, 2.4, 2.2, 2.3, 2.5],
        [1.8, 2.1, 2.0, 1.9, 2.2],
    ]
)
# rgb colors
C = np.array(
    [
        [0.2, 0.4, 0.8],
        [0.8, 0.4, 0.2],
        [0.4, 0.8, 0.2],
        [0.8, 0.2, 0.8],
        [0.8, 0.8, 0.2],
        [0.2, 0.8, 0.8],
    ]
)

# 创建图形和坐标轴
fig, ax = plt.subplots()

# plot the bars
bars = ax.bar(xs, ys, width=0.6, edgecolor="black", alpha=0.8, linewidth=1)

# set the bar colors
for i, bar in enumerate(bars):
    bar.set_facecolor(C[i])

# add error bars
ax.errorbar(
    xs,
    ys,
    yerr=yerrs,
    fmt="none",  # show the error bars as a line
    ecolor="black",
    capsize=3,
    capthick=1.2,
    linewidth=1.2,
)

for j in range(len(xs)):
    # add a random jitter to the x positions
    x_jitter = np.random.normal(0, 0.1, size=len(Y[j]))
    x_positions = xs[j] + x_jitter

    # 绘制散点
    ax.scatter(
        x_positions,
        Y[j],
        s=30,  # scatter size
        color=C[j],
        edgecolors="black",
        linewidths=0.5,
        zorder=10,  # set a higher zorder to make sure the scatter points are on top
    )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_linewidth(1)
ax.spines["left"].set_linewidth(1)

ax.set_title("Bar with Error", fontsize=12, fontweight="bold")
ax.grid(False)

# x and y tick settings
ax.set_xlabel("X", fontsize=11)
ax.set_ylabel("Y", fontsize=11)
ax.tick_params(
    direction="out",
    length=3,
    width=1,
    colors=[0.1, 0.1, 0.1],
    which="major",
    bottom=True,
    top=False,
    left=True,
    right=False,
)
ax.tick_params(axis="both", which="major", labelsize=10)
ax.set_ylim(0, 3.5)
ax.set_xticks(range(1, 7))
ax.set_yticks(np.arange(0, 3.6, 0.5))
ax.set_xticklabels(["1", "2", "3", "4", "5", "6"])

# background color
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

fig.tight_layout()
fig_name = Path(__file__).with_suffix(".png").name
fig.savefig(Path(__file__).parent.joinpath("assets").joinpath(fig_name))
