# Images Folder

[![Images](https://img.shields.io/badge/Images-FF6B6B?style=for-the-badge&logo=image&logoColor=white)](https://en.wikipedia.org/wiki/Image)
[![PNG](https://img.shields.io/badge/PNG-4A90E2?style=for-the-badge&logo=png&logoColor=white)](https://en.wikipedia.org/wiki/Portable_Network_Graphics)

## Overview

This folder contains images, diagrams, and visualizations for the NYPL Menus Data Cleaning Project. These visual elements support documentation, presentations, and understanding of the project structure and workflows.

## Image Categories

### Architecture & Schema Diagrams

#### `ER_Diagram.png`
**Purpose**: Entity-Relationship Diagram showing the complete database schema

**Content:**
- Four main tables: Menu, MenuPage, MenuItem, Dish
- Primary and foreign key relationships
- All table attributes and data types
- Cardinality indicators (one-to-many relationships)

**Use Case**: Understanding the complete data structure and relationships

#### `Relationship_Diagram.png`
**Purpose**: Simplified relationship diagram for easy understanding

**Content:**
- High-level view of table relationships
- Simplified entity connections
- Clear relationship labels
- Visual flow of data

**Use Case**: Quick overview of data relationships

### Workflow Diagrams

#### `Workflow1.png`
**Purpose**: General phase workflow diagram

**Content:**
- Overall project workflow
- Phase transitions
- Key decision points
- Process flow visualization

**Use Case**: Understanding the overall project structure

#### `Workflow2_OpenRefine.png`
**Purpose**: OpenRefine cleaning workflow

**Content:**
- OpenRefine cleaning steps
- Data transformation processes
- Quality check points
- Tool-specific workflows

**Use Case**: Understanding OpenRefine cleaning procedures

#### `Workflow3_pandas.png`
**Purpose**: Python pandas cleaning workflow

**Content:**
- Pandas-based cleaning processes
- Python script workflows
- Automation steps
- Data processing pipelines

**Use Case**: Understanding Python-based cleaning procedures

### Data Quality Examples

#### `MenuID_12478.png`
**Purpose**: Example of missing menu record

**Content:**
- Screenshot showing empty menu record
- Evidence of data quality issue
- Before/after comparison

**Use Case**: Demonstrating specific data quality problems

#### `MenuID_12572.png`
**Purpose**: Example of referential integrity issue

**Content:**
- Screenshot showing orphaned records
- Evidence of relationship problems
- Data inconsistency examples

**Use Case**: Showing referential integrity violations

#### `MenuPage_ID_175.png`
**Purpose**: Example of menu page data quality issue

**Content:**
- Screenshot of problematic menu page data
- Evidence of cleaning needs
- Specific data quality problems

**Use Case**: Demonstrating page-level data issues

#### `Menupage_MenuID_12572.png`
**Purpose**: Additional evidence of referential integrity issues

**Content:**
- Screenshot showing related data problems
- Cross-table relationship issues
- Data consistency problems

**Use Case**: Supporting evidence for data quality documentation

## Usage Guidelines

### For Documentation
- Reference images in markdown files using relative paths
- Include alt text for accessibility
- Use consistent naming conventions
- Maintain image quality for readability

### For Presentations
- Use high-resolution versions when available
- Include proper attribution
- Ensure consistent formatting
- Optimize for different screen sizes

### For Analysis
- Use as reference for data quality issues
- Compare before/after cleaning results
- Support quantitative findings
- Provide visual evidence for conclusions

## Image Specifications

| Image | Format | Size | Resolution | Purpose |
|-------|--------|------|------------|---------|
| ER_Diagram.png | PNG | 242KB | High | Schema documentation |
| Relationship_Diagram.png | PNG | 59KB | Medium | Quick reference |
| Workflow1.png | PNG | 157KB | High | Process overview |
| Workflow2_OpenRefine.png | PNG | 447KB | High | Tool workflow |
| Workflow3_pandas.png | PNG | 228KB | High | Script workflow |
| MenuID_*.png | PNG | 13-29KB | Medium | Data quality examples |

## Image Management

### File Organization
- Use descriptive filenames
- Group related images together
- Maintain consistent naming conventions
- Include version information if needed

### Quality Standards
- Ensure readability at different zoom levels
- Use appropriate file formats (PNG for diagrams)
- Optimize file sizes for web use
- Maintain consistent styling

### Accessibility
- Include descriptive alt text
- Use high contrast for diagrams
- Ensure text is readable
- Provide alternative formats if needed

## Image Descriptions

### Technical Diagrams
- **ER_Diagram.png**: Complete database schema with all tables, attributes, and relationships
- **Relationship_Diagram.png**: Simplified view of table relationships for quick understanding

### Workflow Diagrams
- **Workflow1.png**: Overall project phases and transitions
- **Workflow2_OpenRefine.png**: Detailed OpenRefine cleaning process
- **Workflow3_pandas.png**: Python-based data cleaning workflow

### Data Quality Examples
- **MenuID_12478.png**: Example of missing menu data
- **MenuID_12572.png**: Referential integrity violation example
- **MenuPage_ID_175.png**: Menu page data quality issue
- **Menupage_MenuID_12572.png**: Additional referential integrity evidence

## Related Resources

- [Database Schema Documentation](../docs/01_Description_of_Dataset.md)
- [Data Quality Problems](../docs/03_Data_Quality_Problems.md)
- [Workflow Documentation](../docs/06_Workflow_Model.md) 