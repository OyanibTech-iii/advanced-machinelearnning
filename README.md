# Advance Charts

A collection of customized matplotlib chart functions styled with the Poppins font family.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-FF6F00?style=for-the-badge&logo=matplotlib&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## Features

- Line, Bar, Horizontal Bar, Stacked Bar charts
- Scatter, Pie, Histogram, Box, Violin charts
- Area, Stack, Heatmap, Radar charts
- 3D Surface, Bubble, Error Bar, Step charts
- Multi-panel dashboard subplots
- Custom color palette and global styling
- Automatic Poppins font loading (local, system, or fallback)

## Project Structure

```
advance/
├── README.md
├── examples/
│   └── matplotlib_eg.py
└── output_charts/
    ├── 01_line_chart.png
    ├── 02_bar_chart.png
    ├── ...
    └── 18_dashboard_subplots.png
```

## Requirements

```
matplotlib
numpy
```

## Usage

### Generate all charts

```bash
python examples/matplotlib_eg.py
```

### Import individual functions

```python
from examples.matplotlib_eg import plot_bar_chart, plot_scatter_chart

plot_bar_chart(show=True)
plot_scatter_chart(show=True)
```

## Font Setup

Poppins is a Google Font and is not bundled with matplotlib by default. The script will:

1. Look for Poppins `.ttf` files in a local `./fonts` folder
2. Check for Poppins installed on the system
3. Fall back to matplotlib's default sans-serif font if not found

To enable Poppins, download the font files from [Google Fonts](https://fonts.google.com/specimen/Poppins) and place them in a `fonts` folder.

## Chart Types

| Chart | Function | Output |
|-------|----------|--------|
| Line | `plot_line_chart()` | `01_line_chart.png` |
| Bar | `plot_bar_chart()` | `02_bar_chart.png` |
| Horizontal Bar | `plot_horizontal_bar_chart()` | `03_horizontal_bar.png` |
| Stacked Bar | `plot_stacked_bar_chart()` | `04_stacked_bar.png` |
| Scatter | `plot_scatter_chart()` | `05_scatter_chart.png` |
| Pie | `plot_pie_chart()` | `06_pie_chart.png` |
| Histogram | `plot_histogram()` | `07_histogram.png` |
| Box Plot | `plot_box_plot()` | `08_box_plot.png` |
| Violin Plot | `plot_violin_plot()` | `09_violin_plot.png` |
| Area | `plot_area_chart()` | `10_area_chart.png` |
| Stack Plot | `plot_stackplot()` | `11_stackplot.png` |
| Heatmap | `plot_heatmap()` | `12_heatmap.png` |
| Radar | `plot_radar_chart()` | `13_radar_chart.png` |
| 3D Surface | `plot_3d_surface()` | `14_3d_surface.png` |
| Bubble | `plot_bubble_chart()` | `15_bubble_chart.png` |
| Error Bar | `plot_error_bar_chart()` | `16_error_bar.png` |
| Step | `plot_step_chart()` | `17_step_chart.png` |
| Dashboard | `plot_subplots_dashboard()` | `18_dashboard_subplots.png` |
