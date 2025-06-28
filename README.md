# NYPL Menus Data Cleaning Project

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![OpenRefine](https://img.shields.io/badge/OpenRefine-1A73E8?style=for-the-badge&logo=google&logoColor=white)](https://openrefine.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Comprehensive Data Cleaning and Analysis of Historical Menu Data**

*Processing 45,000+ menus from the 1840s to present for culinary trend analysis*

</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This repository contains a comprehensive data cleaning and analysis project for the New York Public Library's (NYPL) **"What's on the Menu?"** historical menu dataset. The project processes approximately **45,000 menus** dating from the 1840s to the present, providing valuable insights into culinary and cultural trends over nearly two centuries.

### Primary Research Objective
**Analyzing Historical Trends for the Top 10 Most Popular Dishes Per Year**
- Identify the most frequently appearing dishes on menus for each year (1840s–present)
- Examine how dish popularity changes over time
- Support research into culinary and cultural evolution
- Provide reproducible data cleaning workflows

---

## Key Features

- **Multi-approach Data Cleaning**: OpenRefine and Python pandas workflows
- **Comprehensive Analysis**: Trend analysis and historical frequency tracking
- **Extensive Documentation**: Detailed workflow documentation and data quality reports
- **Database Integration**: SQLite database with cleaned, queryable data
- **Visualization Ready**: Clean data optimized for trend analysis and visualization
- **Reproducible Workflows**: Automated cleaning scripts and documented procedures

---

## Dataset Description

The dataset is structured into four main tables with the following relationships:

| Table | Relationship | Description |
|-------|-------------|-------------|
| **Menu** → **MenuPage** | One-to-Many | Each menu can have multiple pages |
| **MenuPage** → **MenuItem** | One-to-Many | Each page can have multiple menu items |
| **MenuItem** → **Dish** | Many-to-One | Each menu item references a specific dish |

### Entity-Relationship Diagram
![ER Diagram](img/ER_Diagram.png)

> **Note**: For detailed schema information, see [dbdiagram.io](https://dbdiagram.io/d/RestaurantDefault-63220cfd0911f91ba5af665d)

---

## Project Structure

```
NYPL-Menus-Data-Cleaning/
├── analysis/          # Data analysis and trend analysis
│   ├── Trend-Analysis.ipynb
│   ├── Queries.ipynb
│   └── restaurant_menus.db.zip
├── data/              # Raw and cleaned datasets
│   ├── Menu_*.csv
│   ├── MenuPage_*.csv
│   ├── MenuItem_*.csv
│   └── Dish_*.csv
├── docs/              # Comprehensive documentation
│   ├── 01_Description_of_Dataset.md
│   ├── 02_Use_Cases.md
│   ├── 03_Data_Quality_Problems.md
│   └── ...
├── img/               # Images and diagrams
│   ├── ER_Diagram.png
│   ├── Workflow*.png
│   └── ...
├── openrefine/        # OpenRefine cleaning workflows
│   ├── *.openrefine.tar
│   └── *_OpenRefineHistory.json
├── pandas/            # Python pandas cleaning scripts
│   ├── pandas.ipynb
│   └── Dish_*.csv.zip
└── workflow/          # Workflow diagrams and scripts
    ├── workflow*.py
    ├── *.yw
    └── *.pdf
```

---

## Getting Started

### Prerequisites

- **Python** 3.8 or higher
- **Jupyter Notebook** or JupyterLab
- **OpenRefine** (optional, for interactive cleaning)

### Installation

```bash
# Clone the repository
git clone https://github.com/darinz/NYPL-Menus-Data-Cleaning.git
cd NYPL-Menus-Data-Cleaning

# Install Python dependencies
pip install pandas numpy jupyter matplotlib seaborn sqlite3
```

### Quick Start Guide

1. **Explore the Data**
   ```bash
   jupyter notebook analysis/Trend-Analysis.ipynb
   ```

2. **Review Documentation**
   - Start with `docs/01_Description_of_Dataset.md`
   - Review workflow documentation in `docs/`

3. **Run Cleaning Workflows**
   ```bash
   # Python-based cleaning
   jupyter notebook pandas/pandas.ipynb
   
   # Or use workflow scripts
   python workflow/workflow1.py
   ```

---

## Documentation

### Core Documentation Files

| Document | Description |
|----------|-------------|
| [`01_Description_of_Dataset.md`](docs/01_Description_of_Dataset.md) | Detailed dataset overview and schema |
| [`02_Use_Cases.md`](docs/02_Use_Cases.md) | Use case definitions and requirements |
| [`03_Data_Quality_Problems.md`](docs/03_Data_Quality_Problems.md) | Identified data quality issues |
| [`04_Description_of_Data_Cleaning_Performed.md`](docs/04_Description_of_Data_Cleaning_Performed.md) | Detailed cleaning procedures |
| [`05_Document_Data_Quality_Changes.md`](docs/05_Document_Data_Quality_Changes.md) | Quantified improvements |
| [`06_Workflow_Model.md`](docs/06_Workflow_Model.md) | Workflow documentation |
| [`07_Conclusions_and_Summary.md`](docs/07_Conclusions_and_Summary.md) | Project summary and findings |

### Key Analysis Files

- **`analysis/Trend-Analysis.ipynb`** - Main trend analysis notebook
- **`analysis/Queries.ipynb`** - SQL queries for data exploration
- **`analysis/restaurant_menus.db.zip`** - SQLite database with cleaned data

---

## Key Findings

### Data Quality Improvements
- **Consistency**: Resolved inconsistencies in dish names, dates, and referential integrity
- **Reliability**: Significant improvements in data consistency and analysis reliability
- **Reproducibility**: Established automated cleaning workflows

### Analysis Results
- **Trend Identification**: Successfully identified popular dishes and their evolution over time
- **Historical Coverage**: Comprehensive analysis spanning 180+ years
- **Culinary Insights**: Revealed changing food preferences and cultural shifts

---

## Contributing

This is a research project focused on data cleaning and analysis. For contributions or questions:

1. **Review Documentation**: Start with the `docs/` folder
2. **Check Issues**: Review existing issues and discussions
3. **Follow Patterns**: Adhere to established workflow patterns
4. **Document Changes**: Update relevant documentation

### Development Guidelines
- Follow the existing code structure and naming conventions
- Update documentation for any new features or changes
- Test workflows with sample data before committing

---

## License

This project is for **academic and research purposes**. Please refer to NYPL's terms for dataset usage.

- **Dataset**: Subject to NYPL's "What's on the Menu?" terms of use
- **Code**: MIT License
- **Documentation**: Creative Commons Attribution

---

## Acknowledgments

- **New York Public Library** for providing the "What's on the Menu?" dataset
- **Project Team** for collaborative research and development
- **Open Source Community** for tools and libraries used in this project

---

<div align="center">

**This project represents the initial phases of data cleaning and analysis. Future phases will include advanced analytics and additional use cases.**

*For questions or collaboration, please review the documentation or open an issue.*

</div>