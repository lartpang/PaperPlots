from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# data: name, values, color, marker
data = [
    ("S1", [0, 0.2, 1.2, 0.5, 0.8, 0.6, 1.6, 1.0, 0.9, 0.8, 0.9, 0.6, 0.4, 0.1, -0.2], (0.56, 0.56, 0.56), "o"),
    ("S2", [0.1, 0, 0.5, 0.4, 1.1, 0.7, 1.6, 0.9, 1.0, 0.7, 0.8, 0.5, 0.3, 0, -0.25], (0.56, 0.56, 0.56), "^"),
    ("S3", [0.3, 0, 0, 0, 0, 0.2, 1.6, 1.5, 1.0, 0.9, 0.8, 0.8, 0.7, 0.6, 0.8], (0.25, 0.50, 0.76), "o"),
    ("S4", [0.4, -0.2, 0, 0, 0.9, 1.8, 1.6, 1.5, 1.0, 0.9, 1.0, 0.9, 0.7, 0.4, 0.5], (0.15, 0.68, 0.39), "o"),
]
years = np.arange(2001, 2016)


# 创建 fig, ax = subfigures
fig, ax = plt.subplots(figsize=(6, 5))

# 阴影区
ax.fill_between([2000, 2006.5], -1, 2, color=(0.761, 0.86, 0.94), edgecolor="none")
ax.fill_between([2006.5, 2016], -1, 2, color=(0.9, 0.94, 0.98), edgecolor="none")

for s_name, s_values, s_color, s_marker in data:
    ax.plot(
        years,
        s_values,
        linestyle="-",
        marker=s_marker,
        linewidth=2.5,
        color=s_color,
        markerfacecolor=s_color,
        markersize=6,
        label=s_name,
    )

ax.set_xlabel("Year", fontsize=12, fontname="Arial")
ax.set_ylabel("Value", fontsize=12, fontname="Arial")
ax.text(2003, -0.35, "Before", fontname="Arial", fontsize=12)
ax.text(2010.5, -0.35, "After", fontname="Arial", fontsize=12)
ax.legend(loc="upper right", frameon=False, fontsize=9)

# 坐标轴设置
ax.set_xlim((2000, 2016))
ax.set_ylim((-0.5, 2))
ax.set_xticks(np.arange(2000, 2017, 1))
ax.set_yticks(np.arange(-0.5, 2.5, 0.5))
ax.tick_params(direction="out", length=3, width=1, colors="black", labelsize=10)

# 旋转刻度标签并保持中心与刻度对齐，同时调整与横轴的距离
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_horizontalalignment("center")
    label.set_rotation_mode("anchor")
    label.set_y(-0.02)  # 向下偏移，避免与横轴重叠

for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_linewidth(1)

fig.tight_layout()
fig_name = Path(__file__).with_suffix(".png").name
fig.savefig(Path(__file__).parent.joinpath("assets").joinpath(fig_name))
