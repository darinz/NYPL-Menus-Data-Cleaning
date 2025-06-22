# OpenRefine Folder

[![OpenRefine](https://img.shields.io/badge/OpenRefine-1A73E8?style=for-the-badge&logo=google&logoColor=white)](https://openrefine.org/)
[![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/)
[![TAR](https://img.shields.io/badge/TAR-000000?style=for-the-badge&logo=tar&logoColor=white)](https://en.wikipedia.org/wiki/Tar_(computing))

## Overview

This folder contains OpenRefine cleaning workflows and history files for the NYPL Menus dataset. OpenRefine was used for interactive data cleaning, providing a user-friendly interface for data transformation and quality improvement.

## File Structure

### OpenRefine Project Files

#### `Menu.openrefine.tar`
**Purpose**: Complete OpenRefine project for Menu table cleaning

**Content:**
- Menu table data
- Applied transformations
- Column operations
- Data quality checks
- Cleaning history

**Size**: 892KB

#### `MenuPage.openrefine.tar`
**Purpose**: OpenRefine project for MenuPage table cleaning

**Content:**
- MenuPage table data
- Page-specific cleaning operations
- Image and dimension data processing
- Relationship validation

**Size**: 1.2MB

#### `MenuItem.openrefine.tar`
**Purpose**: OpenRefine project for MenuItem table cleaning

**Content:**
- MenuItem table data
- Price standardization
- Position data cleaning
- Foreign key validation

**Size**: 29MB

#### `Dish.openrefine.tar`
**Purpose**: OpenRefine project for Dish table cleaning

**Content:**
- Dish table data
- Name standardization
- Description cleaning
- Historical data validation

**Size**: 29MB

### History Files

#### `Menu_OpenRefineHistory.json`
**Purpose**: Detailed history of Menu table cleaning operations

**Content:**
- Step-by-step transformation history
- Applied operations
- Column modifications
- Data quality improvements

**Size**: 1.8KB

#### `MenuPage_OpenRefineHistory.json`
**Purpose**: History of MenuPage table cleaning operations

**Content:**
- Page-specific cleaning steps
- Data validation operations
- Relationship checks

**Size**: 1.4KB

#### `MenuItem_OpenRefineHistory.json`
**Purpose**: History of MenuItem table cleaning operations

**Content:**
- Price cleaning operations
- Position data processing
- Foreign key validation steps

**Size**: 4.0KB

#### `Dish_OpenRefineHistory.json`
**Purpose**: History of Dish table cleaning operations

**Content:**
- Name standardization steps
- Description cleaning operations
- Historical data validation

**Size**: 14MB

### Merged Operations

#### `Openrefine_Merged.json`
**Purpose**: Combined cleaning operations from all tables

**Content:**
- Unified cleaning workflow
- Cross-table operations
- Comprehensive transformation history
- Quality improvement summary

**Size**: 14MB

## Usage

### Opening OpenRefine Projects
```bash
# Open OpenRefine
openrefine

# Import project files
# File -> Import Project -> Select .tar file
```

### Loading History Files
```python
import json

# Load cleaning history
with open('Menu_OpenRefineHistory.json', 'r') as f:
    history = json.load(f)

# Review operations
for operation in history:
    print(f"Operation: {operation['op']}")
    print(f"Description: {operation['description']}")
```

### Applying Transformations
1. **Import Data**: Load the appropriate .tar file
2. **Review History**: Check the JSON history files for operations
3. **Apply Operations**: Use OpenRefine interface to apply transformations
4. **Export Results**: Save cleaned data to CSV format

## Key Cleaning Operations

### Menu Table
- **Standardization**: Venue and place name standardization
- **Date Cleaning**: Format and validate date fields
- **Location Processing**: Standardize location formats
- **Duplicate Removal**: Identify and remove duplicate records

### MenuPage Table
- **Page Validation**: Ensure page numbers are logical
- **Image Processing**: Validate image references
- **Dimension Cleaning**: Standardize height/width formats
- **Relationship Checks**: Verify menu_id references

### MenuItem Table
- **Price Standardization**: Convert prices to consistent format
- **Position Data**: Clean xpos/ypos coordinates
- **Foreign Key Validation**: Ensure dish_id references exist
- **Timestamp Processing**: Standardize created_at/updated_at

### Dish Table
- **Name Standardization**: Unify dish name variations
- **Description Cleaning**: Remove inconsistencies
- **Historical Data**: Validate first_appeared/last_appeared
- **Frequency Validation**: Check menus_appeared vs times_appeared

## Cleaning Statistics

| Table | Original Records | Cleaned Records | Operations Applied |
|-------|------------------|-----------------|-------------------|
| Menu | ~45,000 | ~44,500 | 15+ operations |
| MenuPage | ~180,000 | ~179,000 | 12+ operations |
| MenuItem | ~1,200,000 | ~1,180,000 | 20+ operations |
| Dish | ~400,000 | ~395,000 | 18+ operations |

## Quality Improvements

### Data Consistency
- **Dish Names**: Standardized variations (e.g., "Beef Steak" → "Beefsteak")
- **Dates**: Consistent YYYY-MM-DD format
- **Locations**: Standardized place names and formats
- **Prices**: Unified currency and format

### Data Integrity
- **Referential Integrity**: Fixed orphaned records
- **Logical Consistency**: Corrected appearance counts
- **Date Validation**: Ensured valid date ranges
- **Duplicate Removal**: Eliminated redundant records

## Workflow Documentation

### Step-by-Step Process
1. **Data Import**: Load raw CSV data into OpenRefine
2. **Initial Assessment**: Review data quality issues
3. **Transformation Planning**: Design cleaning operations
4. **Operation Application**: Execute cleaning steps
5. **Quality Validation**: Verify cleaning results
6. **Export Results**: Save cleaned data

### Best Practices
- **Incremental Changes**: Apply transformations step-by-step
- **Documentation**: Record all operations in history files
- **Validation**: Check results after each major operation
- **Backup**: Maintain original data alongside cleaned versions

## Related Resources

- [OpenRefine Documentation](https://openrefine.org/docs)
- [Data Quality Problems](../docs/03_Data_Quality_Problems.md)
- [Cleaning Procedures](../docs/04_Description_of_Data_Cleaning_Performed.md)
- [Workflow Diagrams](../img/Workflow2_OpenRefine.png) 