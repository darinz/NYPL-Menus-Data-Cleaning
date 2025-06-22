# Use Cases

[![Analysis](https://img.shields.io/badge/Analysis-00D4AA?style=for-the-badge&logo=chart&logoColor=white)](https://en.wikipedia.org/wiki/Data_analysis)
[![Data Cleaning](https://img.shields.io/badge/Data_Cleaning-FF6B6B?style=for-the-badge&logo=data&logoColor=white)](https://en.wikipedia.org/wiki/Data_cleaning)
[![Research](https://img.shields.io/badge/Research-4285F4?style=for-the-badge&logo=research&logoColor=white)](https://en.wikipedia.org/wiki/Research)

## Overview

This document defines and analyzes the primary use cases for the NYPL "What's on the Menu?" dataset. These use cases help determine the scope and requirements for data cleaning efforts, ensuring the dataset meets specific analytical needs.


## Primary Use Cases

### **U1: Data Cleaning Required (Necessary and Sufficient)**

#### Use Case: Analyzing Trends for Top 10 Most Popular Dishes Per Year

**Scenario**: A food historian wants to analyze culinary trends by identifying the most frequently appearing dishes for each year from the 1840s to the present, examining how dish popularity evolves over time.

**Research Questions**:
1. What are the **top 10 most frequently appearing dishes** on menus for each year from 1840 to the present?
2. How does the **popularity of these dishes change over time**?
3. What **culinary trends** emerge from this historical analysis?

**Data Cleaning Requirements**:

| Requirement | Description | Impact |
|-------------|-------------|---------|
| **Dish Name Standardization** | Ensure consistency in dish names across all menus | Accurate frequency counting |
| **Date Standardization** | Consistent date format for year categorization | Proper temporal analysis |
| **Historical Range Validation** | Ensure `first_appeared` values are > 1840 | Valid historical context |
| **Duplicate Removal** | Remove duplicate menu entries | Unbiased popularity analysis |
| **Referential Integrity** | Verify foreign key relationships | Data consistency |

**Specific Integrity Checks**:
- `Dish.dish_id` ↔ `MenuItem.dish_id`
- `MenuItem.menu_page_id` ↔ `MenuPage.id`
- `MenuPage.menu_id` ↔ `Menu.id`

**Expected Outcome**: A cleaned dataset (D') with standardized dish names, consistent dates, referential integrity, and no duplicates, enabling accurate trend analysis of popular dishes over time.

### **U0: No Data Cleaning Required**

#### Use Case: Counting Menus Per Year (Valid Years Only)

**Scenario**: A library administrator needs to understand the dataset's temporal distribution to identify collection gaps and assess coverage across different time periods.

**Research Questions**:
1. How many menus are available for each year from **1840 to the present**?
2. Are there **significant gaps** in the collection for certain years or decades?
3. How many years are **out of range** (before 1840 or future dates)?

**Data Cleaning Requirements**: **None required**

**Rationale**: The existing dataset structure with menu dates is sufficient for this analysis. We only count years that are valid (1840-present) and ignore invalid entries.

**Expected Outcome**: The raw dataset (D) can be used directly to count menus per year, providing insights into temporal distribution without any cleaning.

### **U2: Data Cleaning Insufficient**

#### Use Case: Nutritional Content Analysis Over Time

**Scenario**: A nutritionist aims to analyze changes in nutritional content (calories, fats, proteins, etc.) of historical menu items over time.

**Research Questions**:
1. How has the **average calorie count** of restaurant meals changed from the 1840s to the present?
2. What are the trends in **macronutrient composition** (fats, proteins, carbohydrates) for specific dishes over time?
3. How have **portion sizes and nutritional values** evolved historically?

**Data Cleaning Requirements**: **Extensive additional data required**

**Limitation**: The dataset lacks nutritional information, and no amount of data cleaning can compensate for this missing data.

**Expected Outcome**: The dataset (D) is insufficient for nutritional analysis due to fundamental data gaps.

## Use Case Comparison

| Use Case | Data Cleaning Required | Feasibility | Primary Goal |
|----------|----------------------|-------------|--------------|
| **U1** | ✅ Yes (Necessary & Sufficient) | 🟢 High | Trend Analysis |
| **U0** | ❌ No | 🟢 High | Distribution Analysis |
| **U2** | ❌ Insufficient | 🔴 Low | Nutritional Analysis |

## Use Case Prioritization

### **Primary Focus: U1**
- **Justification**: Most valuable for historical research
- **Scope**: Achievable with current data
- **Impact**: High research value
- **Effort**: Moderate cleaning required

### **Secondary Focus: U0**
- **Justification**: Baseline understanding of dataset
- **Scope**: No cleaning required
- **Impact**: Foundation for other analyses
- **Effort**: Minimal

### **Future Consideration: U2**
- **Justification**: Would require additional data sources
- **Scope**: Beyond current dataset capabilities
- **Impact**: High value if feasible
- **Effort**: Significant additional work


## Success Criteria

### For U1 (Trend Analysis)
- **Standardized dish names** across all tables
- **Consistent date formats** (YYYY-MM-DD)
- **Valid historical ranges** (1840-present)
- **No duplicate records**
- **Complete referential integrity**
- **Accurate frequency counting**

### For U0 (Distribution Analysis)
- **Valid date identification**
- **Year-based categorization**
- **Gap identification**
- **Statistical summaries**

### For U2 (Nutritional Analysis)
- **Requires external data sources**
- **Beyond current dataset scope**
- **Not achievable with cleaning alone**

## Expected Outcomes

### **U1 Outcomes**
- **Historical trend identification** for popular dishes
- **Culinary evolution insights** over 180+ years
- **Cultural pattern recognition** in dining preferences
- **Economic trend analysis** through price changes

### **U0 Outcomes**
- **Temporal distribution mapping** of menu collection
- **Collection gap identification** for future acquisitions
- **Dataset coverage assessment** across time periods
- **Statistical foundation** for other analyses

### **U2 Limitations**
- **Cannot provide nutritional insights** with current data
- **Requires external nutritional databases**
- **Would need significant additional research**

## Related Documentation

- **[Dataset Description](01_Description_of_Dataset.md)**: Understanding the data structure
- **[Data Quality Problems](03_Data_Quality_Problems.md)**: Identifying cleaning needs
- **[Cleaning Procedures](04_Description_of_Data_Cleaning_Performed.md)**: Implementation details
- **[Quality Assessment](05_Document_Data_Quality_Changes.md)**: Measuring improvements