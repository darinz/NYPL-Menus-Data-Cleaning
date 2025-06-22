# Analysis Folder

[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

## Overview

This folder contains data analysis notebooks and results for the NYPL Menus dataset. The analysis focuses on identifying trends in popular dishes over time and exploring the cleaned dataset.

## Files

### Jupyter Notebooks

#### `Trend-Analysis.ipynb`
Main analysis notebook for identifying trends in popular dishes over time.

**Key Features:**
- Historical frequency analysis of dishes
- Top 10 most popular dishes per year
- Visualization of trends over time
- Statistical analysis of dish popularity

#### `Queries.ipynb`
SQL queries and data exploration notebook.

**Key Features:**
- Database queries for data exploration
- Data quality checks
- Statistical summaries
- Cross-table analysis

### Data Files

#### `use_case_1_historical_frequencies.csv`
Processed frequency data for the main use case analysis.

**Columns:**
- `dish_name`: Name of the dish
- `year`: Year of appearance
- `frequency`: Number of times the dish appeared
- `rank`: Ranking within that year

#### `menu_item_historical_frequencies.csv`
Detailed historical frequency data for menu items.

#### `restaurant_menus.db.zip`
SQLite database containing the cleaned dataset.

**Tables:**
- `Menu`: Menu metadata
- `MenuPage`: Menu page information
- `MenuItem`: Menu item details
- `Dish`: Dish information

### Documentation

#### `queries.txt`
Text file containing SQL queries used for analysis.

## Usage

1. **Start with Trend Analysis:**
   ```bash
   jupyter notebook Trend-Analysis.ipynb
   ```

2. **Explore Data with Queries:**
   ```bash
   jupyter notebook Queries.ipynb
   ```

3. **Load the Database:**
   ```python
   import sqlite3
   conn = sqlite3.connect('restaurant_menus.db')
   ```

## Key Analyses

- **Temporal Trends**: How dish popularity changes over decades
- **Geographic Patterns**: Regional variations in menu items
- **Price Analysis**: Historical price trends for popular dishes
- **Seasonal Patterns**: Menu variations across seasons and events

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- sqlite3
- jupyter

## Output Examples

The analysis produces:
- Interactive visualizations of dish trends
- Statistical summaries of popularity patterns
- CSV files with processed frequency data
- SQLite database for further exploration 