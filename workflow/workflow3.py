import numpy as np
import pandas as pd
import sqlite3
import csv

# @BEGIN DataCleaningProject_Workflow3
# @PARAM file_pth
# @IN Dish_clean.csv
# @IN Menu_clean.csv
# @IN MenuPage_clean.csv
# @IN MenuItem_clean.csv
# @OUT menu_item_historical_frequencies.csv
# @OUT Dish_clean_final.csv
# @OUT Menu_clean_final.csv
# @OUT MenuPage_clean_final.csv
# @OUT MenuItem_clean_final.csv

def data_cleaning_project(file_pth='.'):
    
    # @BEGIN Load_Cleaned_CSV_Files @desc Load the cleaned CSV files into pandas DataFrames.
    # @IN Dish_clean.csv
    # @IN Menu_clean.csv
    # @IN MenuPage_clean.csv
    # @IN MenuItem_clean.csv
    # @OUT dish_clean
    # @OUT menu_clean
    # @OUT menupage_clean
    # @OUT menuitem_clean
    def load_cleaned_csv_files(file_pth):
        dish_clean = pd.read_csv(f"{file_pth}/clean_data/Dish_clean.csv")
        menu_clean = pd.read_csv(f"{file_pth}/clean_data/Menu_clean.csv")
        menupage_clean = pd.read_csv(f"{file_pth}/clean_data/MenuPage_clean.csv")
        menuitem_clean = pd.read_csv(f"{file_pth}/clean_data/MenuItem_clean.csv")
        return dish_clean, menu_clean, menupage_clean, menuitem_clean
    dish_clean, menu_clean, menupage_clean, menuitem_clean = load_cleaned_csv_files(file_pth)
    # @END Load_Cleaned_CSV_Files
    
    # @BEGIN Data_Profiling @desc Profile the data to understand its structure and content.
    # @IN dish_clean
    # @IN menu_clean
    # @IN menupage_clean
    # @IN menuitem_clean
    # @OUT dish_profile_stats
    # @OUT menu_profile_stats
    # @OUT menupage_profile_stats
    # @OUT menuitem_profile_stats
    def data_profiling(dish_clean, menu_clean, menupage_clean, menuitem_clean):
        dish_profile_stats = dish_clean.describe(include='all')
        menu_profile_stats = menu_clean.describe(include='all')
        menupage_profile_stats = menupage_clean.describe(include='all')
        menuitem_profile_stats = menuitem_clean.describe(include='all')
        return dish_profile_stats, menu_profile_stats, menupage_profile_stats, menuitem_profile_stats
    dish_profile_stats, menu_profile_stats, menupage_profile_stats, menuitem_profile_stats = data_profiling(dish_clean, menu_clean, menupage_clean, menuitem_clean)
    # @END Data_Profiling
    
    # @BEGIN Handle_Missing_Values @desc Handle missing values in the datasets.
    # @IN dish_clean
    # @IN menu_clean
    # @IN menupage_clean
    # @IN menuitem_clean
    # @OUT dish_no_missing
    # @OUT menu_no_missing
    # @OUT menupage_no_missing
    # @OUT menuitem_no_missing
    def handle_missing_values(dish_clean, menu_clean, menupage_clean, menuitem_clean):
        dish_no_missing = dish_clean.fillna(method='ffill')
        menu_no_missing = menu_clean.fillna(method='ffill')
        menupage_no_missing = menupage_clean.fillna(method='ffill')
        menuitem_no_missing = menuitem_clean.fillna(method='ffill')
        return dish_no_missing, menu_no_missing, menupage_no_missing, menuitem_no_missing
    dish_no_missing, menu_no_missing, menupage_no_missing, menuitem_no_missing = handle_missing_values(dish_clean, menu_clean, menupage_clean, menuitem_clean)
    # @END Handle_Missing_Values
    
    # @BEGIN Remove_Duplicates @desc Remove duplicate rows from the datasets.
    # @IN dish_no_missing
    # @IN menu_no_missing
    # @IN menupage_no_missing
    # @IN menuitem_no_missing
    # @OUT dish_no_duplicates
    # @OUT menu_no_duplicates
    # @OUT menupage_no_duplicates
    # @OUT menuitem_no_duplicates
    def remove_duplicates(dish_no_missing, menu_no_missing, menupage_no_missing, menuitem_no_missing):
        dish_no_duplicates = dish_no_missing.drop_duplicates()
        menu_no_duplicates = menu_no_missing.drop_duplicates()
        menupage_no_duplicates = menupage_no_missing.drop_duplicates()
        menuitem_no_duplicates = menuitem_no_missing.drop_duplicates()
        return dish_no_duplicates, menu_no_duplicates, menupage_no_duplicates, menuitem_no_duplicates
    dish_no_duplicates, menu_no_duplicates, menupage_no_duplicates, menuitem_no_duplicates = remove_duplicates(dish_no_missing, menu_no_missing, menupage_no_missing, menuitem_no_missing)
    # @END Remove_Duplicates
    
    # @BEGIN Standardize_Columns @desc Standardize column names and data types.
    # @IN dish_no_duplicates
    # @IN menu_no_duplicates
    # @IN menupage_no_duplicates
    # @IN menuitem_no_duplicates
    # @OUT dish_standardized
    # @OUT menu_standardized
    # @OUT menupage_standardized
    # @OUT menuitem_standardized
    def standardize_columns(dish_no_duplicates, menu_no_duplicates, menupage_no_duplicates, menuitem_no_duplicates):
        dish_standardized = dish_no_duplicates.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
        menu_standardized = menu_no_duplicates.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
        menupage_standardized = menupage_no_duplicates.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
        menuitem_standardized = menuitem_no_duplicates.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
        return dish_standardized, menu_standardized, menupage_standardized, menuitem_standardized
    dish_standardized, menu_standardized, menupage_standardized, menuitem_standardized = standardize_columns(dish_no_duplicates, menu_no_duplicates, menupage_no_duplicates, menuitem_no_duplicates)
    # @END Standardize_Columns
    
    # @BEGIN Clean_Negative_Values @desc Replace negative values in numerical columns with 0.
    # @IN dish_standardized
    # @IN menuitem_standardized
    # @OUT dish_cleaned_negatives
    # @OUT menuitem_cleaned_negatives
    def clean_negative_values(dish_standardized, menuitem_standardized):
        dish_standardized['times_appeared'] = dish_standardized['times_appeared'].where(dish_standardized['times_appeared'] >= 0, 0)
        menuitem_standardized['price'] = menuitem_standardized['price'].where(menuitem_standardized['price'] >= 0, 0)
        dish_cleaned_negatives = dish_standardized
        menuitem_cleaned_negatives = menuitem_standardized
        return dish_cleaned_negatives, menuitem_cleaned_negatives
    dish_cleaned_negatives, menuitem_cleaned_negatives = clean_negative_values(dish_standardized, menuitem_standardized)
    # @END Clean_Negative_Values
    
    # @BEGIN Clip_Values @desc Clip values in specific columns to a specified range.
    # @IN dish_cleaned_negatives
    # @OUT dish_clipped
    def clip_values(dish_cleaned_negatives):
        dish_cleaned_negatives['first_appeared'] = dish_cleaned_negatives['first_appeared'].clip(lower=1840, upper=2008)
        dish_cleaned_negatives['last_appeared'] = dish_cleaned_negatives['last_appeared'].clip(lower=1840, upper=2008)
        dish_clipped = dish_cleaned_negatives
        return dish_clipped
    dish_clipped = clip_values(dish_cleaned_negatives)
    # @END Clip_Values
    
    # @BEGIN Save_Cleaned_CSVs @desc Save the cleaned DataFrames to new CSV files.
    # @IN dish_clipped
    # @IN menu_standardized
    # @IN menupage_standardized
    # @IN menuitem_cleaned_negatives
    # @OUT Dish_clean_final.csv 
    # @OUT Menu_clean_final.csv 
    # @OUT MenuPage_clean_final.csv 
    # @OUT MenuItem_clean_final.csv 
    def save_cleaned_csvs(dish_clipped, menu_standardized, menupage_standardized, menuitem_cleaned_negatives, file_pth):
        dish_clipped.to_csv(f"{file_pth}/clean_data/Dish_clean_final.csv", index=False)
        menu_standardized.to_csv(f"{file_pth}/clean_data/Menu_clean_final.csv", index=False)
        menupage_standardized.to_csv(f"{file_pth}/clean_data/MenuPage_clean_final.csv", index=False)
        menuitem_cleaned_negatives.to_csv(f"{file_pth}/clean_data/MenuItem_clean_final.csv", index=False)
    save_cleaned_csvs(dish_clipped, menu_standardized, menupage_standardized, menuitem_cleaned_negatives, file_pth)
    # @END Save_Cleaned_CSVs
    
    # @BEGIN Connect_Database @desc Connect to the SQLite database.
    # @OUT db_conn
    # @OUT db_cursor
    def connect_database():
        db_conn = sqlite3.connect('restaurant_menus.db')
        db_cursor = db_conn.cursor()
        return db_conn, db_cursor
    db_conn, db_cursor = connect_database()
    # @END Connect_Database
    
    # @BEGIN Create_Tables @desc Create tables in the SQLite database for the cleaned data.
    # @IN db_cursor
    # @IN db_conn
    # @OUT tables_created
    def create_tables(db_cursor, db_conn):
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS dish (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                menus_appeared INTEGER NOT NULL,
                times_appeared INTEGER NOT NULL,
                first_appeared INTEGER NOT NULL,
                last_appeared INTEGER NOT NULL,
                lowest_price REAL,
                highest_price REAL
            )
        ''')
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_page (
                id INTEGER PRIMARY KEY,
                menu_id INTEGER NOT NULL,
                number INTEGER NOT NULL,
                FOREIGN KEY (menu_id) REFERENCES menu (id)
            )
        ''')
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_item (
                id INTEGER PRIMARY KEY,
                menu_page_id INTEGER NOT NULL,
                dish_id INTEGER,
                price REAL,
                FOREIGN KEY (menu_page_id) REFERENCES menu_page (id),
                FOREIGN KEY (dish_id) REFERENCES dish (id)
            )
        ''')
        db_conn.commit()
    create_tables(db_cursor, db_conn)
    # @END Create_Tables
    
    # @BEGIN Insert_Data @desc Insert data from the cleaned CSV files into the respective tables in the SQLite database.
    # @IN db_cursor
    # @IN db_conn
    # @IN Dish_clean_final.csv 
    # @IN Menu_clean_final.csv 
    # @IN MenuPage_clean_final.csv 
    # @IN MenuItem_clean_final.csv
    # @OUT data_inserted
    def insert_data(db_cursor, db_conn, file_pth):
        dish_clean_final = pd.read_csv(f"{file_pth}/clean_data/Dish_clean_final.csv")
        menu_clean_final = pd.read_csv(f"{file_pth}/clean_data/Menu_clean_final.csv")
        menupage_clean_final = pd.read_csv(f"{file_pth}/clean_data/MenuPage_clean_final.csv")
        menuitem_clean_final = pd.read_csv(f"{file_pth}/clean_data/MenuItem_clean_final.csv")
    
        dish_clean_final.to_sql('dish', db_conn, if_exists='replace', index=False)
        menu_clean_final.to_sql('menu', db_conn, if_exists='replace', index=False)
        menupage_clean_final.to_sql('menu_page', db_conn, if_exists='replace', index=False)
        menuitem_clean_final.to_sql('menu_item', db_conn, if_exists='replace', index=False)
    insert_data(db_cursor, db_conn, file_pth)
    # @END Insert_Data
    
    # @BEGIN Potential_Issues_Analysis @desc Analyze and record potential issues in text in the cleaned data.
    # @IN tables_created
    # @IN data_inserted
    # @OUT issues_diagnose @URI file:{file_pth}/issues_diagnose_text
    def potential_issues_analysis(dish_clean_final, menu_clean_final, menupage_clean_final, menuitem_clean_final, file_pth):
        potential_issues = {
            'missing_values': {
                'dish': dish_clean_final.isnull().sum().to_dict(),
                'menu': menu_clean_final.isnull().sum().to_dict(),
                'menupage': menupage_clean_final.isnull().sum().to_dict(),
                'menuitem': menuitem_clean_final.isnull().sum().to_dict(),
            },
            'duplicates': {
                'dish': dish_clean_final.duplicated().sum(),
                'menu': menu_clean_final.duplicated().sum(),
                'menupage': menupage_clean_final.duplicated().sum(),
                'menuitem': menuitem_clean_final.duplicated().sum(),
            },
            'range_issues': {
                'dish': {
                    'first_appeared_out_of_range': dish_clean_final[(dish_clean_final['first_appeared'] < 1840) | (dish_clean_final['first_appeared'] > 2008)].shape[0],
                    'last_appeared_out_of_range': dish_clean_final[(dish_clean_final['last_appeared'] < 1840) | (dish_clean_final['last_appeared'] > 2008)].shape[0],
                }
            }
        }
        issues_report = pd.DataFrame(potential_issues)
        issues_report.to_csv(f"{file_pth}/issues_report.csv", index=False)
    potential_issues_analysis(dish_clean_final, menu_clean_final, menupage_clean_final, menuitem_clean_final, file_pth)
    # @END Potential_Issues_Analysis
    
    # @BEGIN Query_Top_Dishes @desc Perform a complex SQL query to find the top 10 menu items per year and save the result to a CSV file.
    # @IN issues_diagnose
    # @IN db_cursor @desc Database cursor object.
    # @OUT menu_item_historical_frequencies.csv
    def query_top_dishes(db_cursor, file_pth):
        filename = f"{file_pth}/menu_item_historical_frequencies.csv"
        query = '''
            SELECT *
            FROM
            (
                    SELECT
                        CAST(substr(menu.date, 1, 4) as INTEGER) AS Year,
                        dish.name AS 'DishName',
                        COUNT(dish.name) AS Occurrences,
                        ROW_NUMBER () OVER (
                            PARTITION BY CAST(substr(menu.date, 1, 4) as INTEGER)
                            ORDER BY COUNT(dish.name) DESC, dish.name
                        ) Rank
                    FROM
                            menu_item
                            LEFT OUTER JOIN dish ON menu_item.dish_id = dish.id
                            LEFT OUTER JOIN menu_page ON menu_item.menu_page_id = menu_page.id
                            LEFT OUTER JOIN menu ON menu_page.menu_id = menu.id
                    WHERE 
                            menu_item.dish_id IS NOT NULL AND
                            menu.date IS NOT NULL AND
                            menu.date NOT LIKE '0%' AND
                            menu.date NOT LIKE '10%' AND
                            dish.id IS NOT NULL AND
                            (dish.name NOT LIKE '"' AND dish.name NOT LIKE '" %')
                    GROUP BY Year, dish.name
            ) t
            WHERE Rank <= 10
        '''
        db_cursor.execute(query)
        fields = ['Year', 'DishName', 'Occurrences', 'Rank']
        rows = db_cursor.fetchall()
    
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for row in rows:
                csvwriter.writerow(list(row))
    query_top_dishes(db_cursor, file_pth)
    # @END Query_Top_Dishes

# @END DataCleaningProject_Workflow3

data_cleaning_project()
