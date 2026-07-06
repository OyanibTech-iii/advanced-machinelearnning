"""
matplotlib_poppins_examples.py
================================
A collection of customized matplotlib.pyplot graph functions, all styled
with the "Poppins" font family.

HOW POPPINS IS LOADED
----------------------
Poppins is a Google Font and is NOT bundled with matplotlib by default.
This script will:
  1. Look for Poppins .ttf files in a local "./fonts" folder.
  2. If not found, look for Poppins already installed on the system.
  3. If still not found, fall back gracefully to matplotlib's default
     sans-serif font and print a warning (so the script never crashes).

To get real Poppins rendering, download the font files (Poppins-Regular.ttf,
Poppins-Medium.ttf, Poppins-SemiBold.ttf, Poppins-Bold.ttf) from
https://fonts.google.com/specimen/Poppins and place them in a "fonts"
folder next to this script, OR install Poppins system-wide.

USAGE
-----
Run directly to generate every example as a PNG in "./output_charts":
    python matplotlib_poppins_examples.py

Or import individual functions:
    from matplotlib_poppins_examples import plot_bar_chart
    plot_bar_chart(show=True)
"""

import os
import glob
import warnings

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Wedge
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (enables 3d projection)


# ----------------------------------------------------------------------------
# 1. FONT SETUP — Poppins
# ----------------------------------------------------------------------------
def setup_poppins_font(fonts_dir: str = "fonts") -> str:
    """
    Registers the Poppins font with matplotlib if available and sets it as
    the global font family. Returns the family name actually applied.
    """
    font_family_name = "Poppins"
    found_any = False

    # 1) Local ./fonts folder
    if os.path.isdir(fonts_dir):
        ttf_files = glob.glob(os.path.join(fonts_dir, "*.ttf"))
        for ttf in ttf_files:
            if "poppins" in os.path.basename(ttf).lower():
                fm.fontManager.addfont(ttf)
                found_any = True

    # 2) Already installed on the system
    system_matches = [
        f for f in fm.fontManager.ttflist if "poppins" in f.name.lower()
    ]
    if system_matches:
        found_any = True

    if found_any:
        plt.rcParams["font.family"] = font_family_name
    else:
        warnings.warn(
            "Poppins font not found locally or system-wide. "
            "Falling back to matplotlib's default sans-serif font. "
            "Download Poppins from https://fonts.google.com/specimen/Poppins "
            "and place the .ttf files in a 'fonts' folder to enable it.",
            stacklevel=2,
        )
        plt.rcParams["font.family"] = "sans-serif"
        font_family_name = plt.rcParams["font.family"][0]

    return font_family_name


FONT_FAMILY = setup_poppins_font()

# ----------------------------------------------------------------------------
# 2. GLOBAL STYLE — applied to every chart
# ----------------------------------------------------------------------------
COLORS = {
    "bg": "#FAFAFA",
    "panel": "#FFFFFF",
    "primary": "#6C5CE7",
    "secondary": "#00B894",
    "accent": "#FD79A8",
    "warn": "#FDCB6E",
    "danger": "#E17055",
    "text": "#2D3436",
    "grid": "#DFE6E9",
    "palette": ["#6C5CE7", "#00B894", "#FD79A8", "#FDCB6E", "#0984E3", "#E17055"],
}

plt.rcParams.update({
    "figure.facecolor": COLORS["bg"],
    "axes.facecolor": COLORS["panel"],
    "axes.edgecolor": COLORS["grid"],
    "axes.grid": True,
    "grid.color": COLORS["grid"],
    "grid.linewidth": 0.8,
    "axes.labelcolor": COLORS["text"],
    "text.color": COLORS["text"],
    "xtick.color": COLORS["text"],
    "ytick.color": COLORS["text"],
    "font.size": 11,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.labelsize": 12,
    "legend.frameon": False,
    "savefig.facecolor": COLORS["bg"],
})

OUTPUT_DIR = "output_charts"


def _finalize(fig, ax_or_axes, title, filename, show=False):
    """Shared styling + save/show step used by every plotting function."""
    axes = ax_or_axes if isinstance(ax_or_axes, (list, np.ndarray)) else [ax_or_axes]
    for ax in np.ravel(axes):
        if hasattr(ax, "spines"):
            for side in ("top", "right"):
                if side in ax.spines:
                    ax.spines[side].set_visible(False)

    fig.suptitle(title, fontsize=17, fontweight="bold", color=COLORS["text"],
                 fontfamily=FONT_FAMILY)
    fig.tight_layout(rect=[0, 0, 1, 0.95])

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=160)
    print(f"Saved: {path}")

    if show:
        plt.show()
    plt.close(fig)


# ----------------------------------------------------------------------------
# 3. CHART FUNCTIONS
# ----------------------------------------------------------------------------
def plot_line_chart(show=False):
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, np.sin(x), color=COLORS["primary"], linewidth=2.5, label="sin(x)")
    ax.plot(x, np.cos(x), color=COLORS["accent"], linewidth=2.5,
            linestyle="--", label="cos(x)")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.legend()
    _finalize(fig, ax, "Line Chart", "01_line_chart.png", show)


def plot_bar_chart(show=False):
    categories = ["Jan", "Feb", "Mar", "Apr", "May"]
    values = [23, 45, 31, 52, 39]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, values, color=COLORS["palette"], width=0.6,
                   edgecolor="white", linewidth=1.2)
    for bar in bars:
        h = bar.get_height()
        ax.annotate(f"{h}", (bar.get_x() + bar.get_width() / 2, h),
                    textcoords="offset points", xytext=(0, 6),
                    ha="center", fontweight="bold", fontfamily=FONT_FAMILY)
    ax.set_ylabel("Sales (units)")
    _finalize(fig, ax, "Bar Chart", "02_bar_chart.png", show)


def plot_horizontal_bar_chart(show=False):
    labels = ["Product A", "Product B", "Product C", "Product D"]
    values = [72, 55, 88, 41]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(labels, values, color=COLORS["secondary"], edgecolor="white")
    ax.set_xlabel("Score")
    _finalize(fig, ax, "Horizontal Bar Chart", "03_horizontal_bar.png", show)


def plot_stacked_bar_chart(show=False):
    categories = ["Q1", "Q2", "Q3", "Q4"]
    product_a = [20, 34, 30, 35]
    product_b = [25, 32, 34, 20]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(categories, product_a, label="Product A", color=COLORS["primary"])
    ax.bar(categories, product_b, bottom=product_a, label="Product B",
           color=COLORS["accent"])
    ax.set_ylabel("Revenue ($k)")
    ax.legend()
    _finalize(fig, ax, "Stacked Bar Chart", "04_stacked_bar.png", show)


def plot_scatter_chart(show=False):
    rng = np.random.default_rng(42)
    x = rng.normal(0, 1, 150)
    y = x * 0.7 + rng.normal(0, 0.6, 150)
    sizes = rng.uniform(20, 200, 150)
    fig, ax = plt.subplots(figsize=(8, 5))
    sc = ax.scatter(x, y, c=x + y, cmap="cool", s=sizes, alpha=0.75,
                     edgecolors="white", linewidth=0.5)
    fig.colorbar(sc, ax=ax, label="Value")
    ax.set_xlabel("X Variable")
    ax.set_ylabel("Y Variable")
    _finalize(fig, ax, "Scatter Plot", "05_scatter_chart.png", show)


def plot_pie_chart(show=False):
    labels = ["Chrome", "Safari", "Firefox", "Edge", "Other"]
    sizes = [45, 25, 15, 10, 5]
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", startangle=90,
        colors=COLORS["palette"], pctdistance=0.8,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
        textprops={"fontfamily": FONT_FAMILY},
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontweight("bold")
    centre_circle = plt.Circle((0, 0), 0.55, fc=COLORS["panel"])
    ax.add_artist(centre_circle)
    ax.set_aspect("equal")
    _finalize(fig, ax, "Donut / Pie Chart", "06_pie_chart.png", show)


def plot_histogram(show=False):
    rng = np.random.default_rng(1)
    data = rng.normal(loc=65, scale=12, size=1000)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data, bins=25, color=COLORS["primary"], edgecolor="white", alpha=0.9)
    ax.axvline(data.mean(), color=COLORS["danger"], linestyle="--", linewidth=2,
               label=f"Mean = {data.mean():.1f}")
    ax.set_xlabel("Score")
    ax.set_ylabel("Frequency")
    ax.legend()
    _finalize(fig, ax, "Histogram", "07_histogram.png", show)


def plot_box_plot(show=False):
    rng = np.random.default_rng(7)
    data = [rng.normal(0, s, 200) for s in (1, 2, 3, 1.5)]
    fig, ax = plt.subplots(figsize=(8, 5))
    bp = ax.boxplot(data, patch_artist=True, tick_labels=["A", "B", "C", "D"],
                     medianprops={"color": COLORS["text"], "linewidth": 2})
    for patch, color in zip(bp["boxes"], COLORS["palette"]):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)
    ax.set_ylabel("Distribution")
    _finalize(fig, ax, "Box Plot", "08_box_plot.png", show)


def plot_violin_plot(show=False):
    rng = np.random.default_rng(3)
    data = [rng.normal(0, s, 200) for s in (1, 1.5, 0.8)]
    fig, ax = plt.subplots(figsize=(8, 5))
    parts = ax.violinplot(data, showmeans=True, showmedians=False)
    for i, body in enumerate(parts["bodies"]):
        body.set_facecolor(COLORS["palette"][i % len(COLORS["palette"])])
        body.set_alpha(0.8)
        body.set_edgecolor(COLORS["text"])
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["Group 1", "Group 2", "Group 3"])
    _finalize(fig, ax, "Violin Plot", "09_violin_plot.png", show)


def plot_area_chart(show=False):
    x = np.arange(0, 10, 0.5)
    y1 = np.random.default_rng(5).uniform(1, 5, len(x))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_between(x, y1, color=COLORS["secondary"], alpha=0.4)
    ax.plot(x, y1, color=COLORS["secondary"], linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    _finalize(fig, ax, "Area Chart", "10_area_chart.png", show)


def plot_stackplot(show=False):
    x = np.arange(6)
    a = [3, 4, 5, 4, 6, 7]
    b = [2, 3, 3, 4, 4, 5]
    c = [1, 1, 2, 2, 3, 3]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.stackplot(x, a, b, c, labels=["Team A", "Team B", "Team C"],
                 colors=COLORS["palette"][:3], alpha=0.9)
    ax.legend(loc="upper left")
    ax.set_xlabel("Week")
    ax.set_ylabel("Output")
    _finalize(fig, ax, "Stack Plot", "11_stackplot.png", show)


def plot_heatmap(show=False):
    rng = np.random.default_rng(9)
    data = rng.uniform(0, 1, (8, 8))
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(data, cmap="viridis")
    fig.colorbar(im, ax=ax, label="Intensity")
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    _finalize(fig, ax, "Heatmap", "12_heatmap.png", show)


def plot_radar_chart(show=False):
    categories = ["Speed", "Power", "Accuracy", "Stamina", "Agility"]
    values = [4, 3, 5, 2, 4]
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    ax.plot(angles, values, color=COLORS["primary"], linewidth=2)
    ax.fill(angles, values, color=COLORS["primary"], alpha=0.3)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontfamily=FONT_FAMILY)
    ax.set_yticklabels([])
    _finalize(fig, ax, "Radar Chart", "13_radar_chart.png", show)


def plot_3d_surface(show=False):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-5, 5, 60)
    y = np.linspace(-5, 5, 60)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x ** 2 + y ** 2))
    surf = ax.plot_surface(x, y, z, cmap="plasma", edgecolor="none")
    fig.colorbar(surf, ax=ax, shrink=0.6, label="Z Value")
    _finalize(fig, ax, "3D Surface Plot", "14_3d_surface.png", show)


def plot_bubble_chart(show=False):
    rng = np.random.default_rng(11)
    x = rng.uniform(0, 100, 40)
    y = rng.uniform(0, 100, 40)
    sizes = rng.uniform(50, 900, 40)
    colors = rng.uniform(0, 1, 40)
    fig, ax = plt.subplots(figsize=(8, 5))
    sc = ax.scatter(x, y, s=sizes, c=colors, cmap="cool", alpha=0.6,
                     edgecolors="white")
    fig.colorbar(sc, ax=ax, label="Category")
    ax.set_xlabel("Market Reach")
    ax.set_ylabel("Engagement")
    _finalize(fig, ax, "Bubble Chart", "15_bubble_chart.png", show)


def plot_error_bar_chart(show=False):
    x = np.arange(1, 6)
    y = [12, 19, 15, 24, 20]
    err = [1.5, 2.1, 1.0, 2.6, 1.8]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(x, y, yerr=err, fmt="o-", color=COLORS["danger"],
                ecolor=COLORS["text"], elinewidth=1.5, capsize=5,
                markersize=8, markerfacecolor=COLORS["warn"])
    ax.set_xlabel("Trial")
    ax.set_ylabel("Measurement")
    _finalize(fig, ax, "Error Bar Chart", "16_error_bar.png", show)


def plot_step_chart(show=False):
    x = np.arange(0, 10)
    y = np.random.default_rng(13).integers(1, 10, size=10)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.step(x, y, where="mid", color=COLORS["primary"], linewidth=2.5)
    ax.fill_between(x, y, step="mid", alpha=0.2, color=COLORS["primary"])
    ax.set_xlabel("Step")
    ax.set_ylabel("Level")
    _finalize(fig, ax, "Step Chart", "17_step_chart.png", show)


def plot_subplots_dashboard(show=False):
    """A multi-panel dashboard combining several chart types in one figure."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    # Top-left: line
    x = np.linspace(0, 10, 100)
    axes[0, 0].plot(x, np.sin(x), color=COLORS["primary"], linewidth=2)
    axes[0, 0].set_title("Trend", fontfamily=FONT_FAMILY, fontweight="bold")

    # Top-right: bar
    axes[0, 1].bar(["A", "B", "C"], [4, 7, 3], color=COLORS["palette"][:3])
    axes[0, 1].set_title("Comparison", fontfamily=FONT_FAMILY, fontweight="bold")

    # Bottom-left: scatter
    rng = np.random.default_rng(2)
    axes[1, 0].scatter(rng.normal(size=50), rng.normal(size=50),
                        color=COLORS["accent"], alpha=0.7)
    axes[1, 0].set_title("Distribution", fontfamily=FONT_FAMILY, fontweight="bold")

    # Bottom-right: pie
    axes[1, 1].pie([40, 30, 20, 10], labels=["A", "B", "C", "D"],
                   colors=COLORS["palette"][:4], autopct="%1.0f%%",
                   textprops={"fontfamily": FONT_FAMILY})
    axes[1, 1].set_title("Share", fontfamily=FONT_FAMILY, fontweight="bold")

    _finalize(fig, axes, "Dashboard (Subplots)", "18_dashboard_subplots.png", show)


# ----------------------------------------------------------------------------
# 4. RUN ALL EXAMPLES
# ----------------------------------------------------------------------------
ALL_CHART_FUNCTIONS = [
    plot_line_chart,
    plot_bar_chart,
    plot_horizontal_bar_chart,
    plot_stacked_bar_chart,
    plot_scatter_chart,
    plot_pie_chart,
    plot_histogram,
    plot_box_plot,
    plot_violin_plot,
    plot_area_chart,
    plot_stackplot,
    plot_heatmap,
    plot_radar_chart,
    plot_3d_surface,
    plot_bubble_chart,
    plot_error_bar_chart,
    plot_step_chart,
    plot_subplots_dashboard,
]


def generate_all(show=False):
    """Runs every chart function and saves output to ./output_charts/."""
    print(f"Using font family: {FONT_FAMILY}")
    for func in ALL_CHART_FUNCTIONS:
        func(show=show)
    print(f"\nAll {len(ALL_CHART_FUNCTIONS)} charts generated in '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    generate_all(show=False)