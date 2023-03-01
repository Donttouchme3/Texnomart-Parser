import sqlite3


def CreateCategoryTable():
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories(
        CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT UNIQUE,
        CategoryLink TEXT
    );
    ''')
    DataBase.commit()
    DataBase.close()


def CreateSubcategoryTable():
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    CREATE TABLE IF NOT EXISTS Subcategories(
        SubcategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        SubcategoryName TEXT UNIQUE,
        SubcategoryLink TEXT,
        CategoryId INTEGER,
        FOREIGN KEY(CategoryId) REFERENCES Category(CategoryIdI)
    );
    ''')
    DataBase.commit()
    DataBase.close()


def CreateSubcategoryTypesTable():
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    CREATE TABLE IF NOT EXISTS SubcategoryTypes(
        SubcategoryTypeId INTEGER PRIMARY KEY AUTOINCREMENT,
        SubcategoryTypeName TEXT UNIQUE,
        SubcategoryTypeLink TEXT,
        SubcategoryId INTEGER REFERENCES Subcategories(SubcategoryId)
    );
    ''')
    DataBase.commit()
    DataBase.close()


def CreateProductTable():
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.executescript('''
    DROP TABLE IF EXISTS Products;
    CREATE TABLE IF NOT EXISTS Products(
    
        ProductId INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT,
        ProductLink TEXT,
        ProductSubId INTEGER REFERENCES SubcategoryTypes(SubcategoryTypeId) DEFAULT 0,
        SubcategoryId INTEGER REFERENCES Subcategories(SubcategoryId)
    );
    ''')
    DataBase.commit()
    DataBase.close()


def CreateUsersTable():
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        UserId INTEGER PRIMARY KEY AUTOINCREMENT,
        ChatId BIGINT UNIQUE,
        UserName TEXT
        Phone TEXT UNIQUE
    );
    ''')
    DataBase.commit()
    DataBase.close()

# CreateCategoryTable()
# CreateSubcategoryTable()
# CreateSubcategoryTypesTable()
# CreateProductTable()
# CreateUsersTable()

