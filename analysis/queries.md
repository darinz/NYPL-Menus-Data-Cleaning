
# SQL Queries

## Query 1.1: Creating dish table to hold Dish_clean.csv data.

```sql
CREATE TABLE IF NOT EXISTS dish (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    menus_appeared INTEGER NOT NULL,
    times_appeared INTEGER NOT NULL CHECK (times_appeared >= 0),
    first_appeared INTEGER NOT NULL,
    last_appeared INTEGER NOT NULL,
    lowest_price REAL,
    highest_price REAL,
    CONSTRAINT CHK_first_appeared CHECK (first_appeared >= 1840 AND first_appeared <= 2008),
    CONSTRAINT CHK_last_appeared CHECK (last_appeared >= 1840 AND last_appeared <= 2008)
)
```

## Query 1.2: Inserting data into dish table.

```sql
INSERT INTO dish (id, name, menus_appeared, times_appeared, first_appeared, last_appeared, lowest_price, highest_price)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
```

## Query 2.1: Creating menu table to hold Menu_clean.csv data.

```sql
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sponsor TEXT,
    event TEXT,
    venue TEXT,
    place TEXT,
    physical_description TEXT,
    occasion TEXT,
    notes TEXT,
    call_number TEXT,
    keywords TEXT,
    language TEXT,
    date TEXT,
    location TEXT NOT NULL,
    location_type TEXT,
    currency TEXT,
    currency_symbol TEXT,
    status TEXT NOT NULL,
    page_count INTEGER NOT NULL,
    dish_count INTEGER NOT NULL
)
```

## Query 2.2: Inserting data into menu table.

```sql
INSERT INTO menu (id, name, sponsor, event, venue, place, physical_description, occasion,
                      notes, call_number, keywords, language, date, location, location_type,
                      currency, currency_symbol, status, page_count, dish_count)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
```

## Query 3.1: Creating menu_page table to hold MenuPage_clean.csv data.

```sql
CREATE TABLE IF NOT EXISTS menu_page (
    id INTEGER PRIMARY KEY,
    menu_id INTEGER NOT NULL,
    page_number INTEGER,
    image_id TEXT NOT NULL,
    full_height REAL,
    full_width REAL,
    uuid TEXT NOT NULL,
    FOREIGN KEY(menu_id) REFERENCES menu(id)
)
```

## Query 3.2: Inserting data into menu_page table.

```sql
INSERT INTO menu_page (id, menu_id, page_number, image_id, full_height, full_width, uuid)
VALUES (?, ?, ?, ?, ?, ?, ?)
```

## Query 4.1: Creating menu_item table to hold MenuItem_clean.csv data.

```sql
CREATE TABLE IF NOT EXISTS menu_item (
    id INTEGER PRIMARY KEY,
    menu_page_id INTEGER NOT NULL,
    price REAL,
    high_price REAL,
    dish_id INTEGER,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    xpos REAL NOT NULL,
    ypos REAL NOT NULL,
    FOREIGN KEY(menu_page_id) REFERENCES menu_page(id),
    FOREIGN KEY(dish_id) REFERENCES dish(id)
)
```

## Query 4.2: Inserting data into menu_item table.

```sql
INSERT INTO menu_item (id, menu_page_id, price, high_price, dish_id, created_at, updated_at, xpos, ypos)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
```

## Query 5: Gathering the top 10 dishes for each year to help answer Use Case 1.

```sql
SELECT *
FROM
(
        SELECT
            CAST(substr(menu.date, 1, 4) as INTEGER) AS Year,
            dish.name AS 'DishName',
            COUNT(dish.name) AS Occurences,
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
                menu_item.dish_id NOT NULL AND
                menu.date NOT NULL AND
                menu.date NOT LIKE '0%' AND
                menu.date NOT LIKE '10%' AND
                dish.id NOT NULL AND
                (dish.name NOT LIKE '"' AND dish.name NOT LIKE '" "%')
        GROUP BY Year, dish.name
)
WHERE Rank <= 10
```