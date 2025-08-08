from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import Normalize

np.random.seed(0)
n = 5
a = np.arange(n**2).reshape(n, n) / n**2
data = (a + a.T) / 2
np.fill_diagonal(data, 1)
data = data.round(2)
print(data)
labels = [f"{i}" for i in range(n)]

cmap_name = "viridis_r"
cmap = plt.get_cmap(cmap_name)
norm = Normalize(vmin=np.nanmin(data), vmax=np.nanmax(data))

fig, ax = plt.subplots(figsize=(9, 8))

# 先画heatmap，去掉linewidths避免白缝隙
sns.heatmap(
    data,
    mask=np.tril(np.ones_like(data, dtype=bool), -1),
    cmap=cmap_name,
    vmin=0,
    vmax=1,
    square=True,
    linewidths=0,
    cbar=False,  # 先不画colorbar
    xticklabels=labels,
    yticklabels=labels,
    annot=False,
    ax=ax,
)

# 下三角加数字
for i in range(n):
    for j in range(n):
        if i > j:
            val = data[i, j]
            txt = f"{val:.2f}"
            color = cmap(norm(val))
            ax.text(j + 0.5, i + 0.5, txt, ha="center", va="center", color=color, fontsize=20)

# 坐标轴字体大小
ax.set_xticklabels(labels, rotation=0, fontsize=24)
ax.set_yticklabels(labels, rotation=0, fontsize=24)
ax.set_xlabel("x", fontsize=24)
ax.set_ylabel("y", fontsize=24)
ax.set_title("Heatmap", fontsize=28, fontweight="bold")

# 添加黑边框
rect = patches.Rectangle((0, 0), n, n, fill=False, edgecolor="black", linewidth=1.5)
ax.add_patch(rect)

# 手动加colorbar
# 先拿heatmap的Axes位置
pos = ax.get_position()
# 在fig上手动添加colorbar Axes，位置在heatmap右边，保持高度一致
cbar_ax = fig.add_axes((pos.x1 + 0.01, pos.y0, 0.03, pos.height))  # 0.01是横向间距，0.03是colorbar宽度

sm = plt.cm.ScalarMappable(cmap=cmap_name, norm=norm)
sm.set_array([])  # 这个必须设才能正常显示colorbar
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.ax.tick_params(labelsize=20)

fig_name = Path(__file__).with_suffix(".png").name
fig.savefig(Path(__file__).parent.joinpath("assets").joinpath(fig_name))
