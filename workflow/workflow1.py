import pandas as pd
import sqlite3

# @BEGIN DataCleaningProject_Workflow1
# @PARAM file_pth
# @IN raw_data_file @URI file:{file_pth}/dirty_data
# @OUT menu_item_historical_frequencies @URI file:{file_pth}/final_cleaned_data.csv

def data_cleaning_project(file_pth='.'):
    
    # @BEGIN DataProfiling @desc Understand the data, define use case, identify data quality issues, design database schema
    # @PARAM file_pth
    # @IN raw_data_file @URI file:{file_pth}/Dish_dirty.csv
    # @OUT profiled_data_file @URI file:{file_pth}/profiled_data
    def data_profiling(file_pth):
        raw_data = pd.read_csv(f'{file_pth}/Dish_dirty.csv')
        profiled_data = raw_data
        profiled_data.to_csv(f'{file_pth}/profiled_data.csv', index=False)
        return profiled_data
    # @END DataProfiling
    profiled_data = data_profiling(file_pth)
    
    # @BEGIN DataLoading @desc Read raw data and prepare it for the data transform phase
    # @PARAM file_pth
    # @IN profiled_data_file @URI file:{file_pth}/profiled_data
    # @OUT loaded_data_file @URI file:{file_pth}/loaded_data
    def data_loading(file_pth):
        profiled_data = pd.read_csv(f'{file_pth}/profiled_data.csv')
        loaded_data = profiled_data
        loaded_data.to_csv(f'{file_pth}/loaded_data.csv', index=False)
        return loaded_data
    # @END DataLoading
    loaded_data = data_loading(file_pth)
    
    # @BEGIN DataCleaning_OpenRefine @desc Data profiling, text transform (trim, standardize name, Regex extraction, format), data cleaning 
    # @PARAM file_pth
    # @IN loaded_data_file @URI file:{file_pth}/loaded_data
    # @OUT cleaned_data_file @URI file:{file_pth}/cleaned_data_openrefine
    def data_transform(file_pth):
        load_data = pd.read_csv(f'{file_pth}/loaded_data.csv')
        transformed_data = load_data
        transformed_data.to_csv(f'{file_pth}/cleaned_data.csv', index=False)
        return transformed_data
    # @END DataCleaning_OpenRefine
    cleaned_data = data_transform(file_pth)

    # @BEGIN DataCleaning_Pandas @desc Additional data cleaning and data manipulation (filter, profile, remove duplicates, fill missing data)
    # @PARAM file_pth
    # @IN cleaned_data_file @URI file:{file_pth}/cleaned_data_openrefine
    # @OUT cleaned_final_data_file @URI file:{file_pth}/cleaned_data_pandas
    def data_cleaning(file_pth):
        load_data = pd.read_csv(f'{file_pth}/cleaned_data.csv')
        cleaned_data = load_data
        cleaned_data.to_csv(f'{file_pth}/cleaned_final_data.csv', index=False)
        return cleaned_data
    # @END DataCleaning_Pandas
    cleaned_final_data = data_cleaning(file_pth)
    
    # @BEGIN ICViolationChecks @desc Verify referential integrity and check constrains
    # @PARAM file_pth
    # @IN cleaned_final_data_file @URI file:{file_pth}/cleaned_data_pandas
    # @OUT ic_checked_data_file @URI file:{file_pth}/ic_checked_data
    def ic_violation_checks(file_pth):
        cleaned_data = pd.read_csv(f'{file_pth}/cleaned_final_data.csv')
        ic_checked_data = cleaned_data
        ic_checked_data.to_csv(f'{file_pth}/ic_checked_data.csv', index=False)
        return ic_checked_data
    # @END ICViolationChecks
    ic_checked_data = ic_violation_checks(file_pth)

    
    # @BEGIN DB_DataIngestion @desc Create DB tables with cleaned ic_checked_data (Dish, Menu, Menu Page, Menu Item)
    # @PARAM file_pth
    # @IN ic_checked_data_file @URI file:{file_pth}/ic_checked_data_file
    # @OUT database_tables @URI file:{file_pth}/database_tables
    def database_creation(file_pth):
        database = pd.read_csv(f'{file_pth}/ic_checked_data.csv')
        conn = sqlite3.connect(f'{file_pth}/data.db')
        database.to_sql('data', conn, if_exists='replace', index=False)
        return database
    # @END DB_DataIngestion
    db = database_creation(file_pth)
    
    # @BEGIN Usecase1Query @desc Query the data to generate historical frequencies of menu items
    # @PARAM file_pth
    # @IN database_tables @URI file:{file_pth}/database_tables
    # @OUT menu_item_historical_frequencies @URI file:{file_pth}/menu_item_historical_frequencies.csv
    def use_case_query(file_pth):
        conn = sqlite3.connect(f'{file_pth}/data.db')
        query = '''
            SELECT Year, DishName, Occurrences, Rank
            FROM (
                SELECT
                    strftime('%Y', menu.date) AS Year,
                    dish.name AS DishName,
                    COUNT(dish.name) AS Occurrences,
                    ROW_NUMBER () OVER (
                        PARTITION BY strftime('%Y', menu.date)
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
                    dish.id IS NOT NULL
                GROUP BY Year, dish.name
            ) t
            WHERE Rank <= 10
        '''
        df = pd.read_sql_query(query, conn)
        df.to_csv(f'{file_pth}/menu_item_historical_frequencies.csv', index=False)
        return df
    # @END Usecase1Query
    query = use_case_query(file_pth)

# @END DataCleaningProject_Workflow1

data_cleaning_project()
