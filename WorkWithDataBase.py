# ---------------------------------- Parsing -------------------------------------
import sqlite3
import os


def InsertIntoCategories(CategoryName, CategoryLink):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT INTO Categories(CategoryName, CategoryLink) VALUES (?, ?)
    ''', (CategoryName, CategoryLink))
    DataBase.commit()
    DataBase.close()


def InsertIntoSubcategories(CategoryLink, SubcategoryName, SubcategoryLink):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT INTO Subcategories(SubcategoryName, SubcategoryLink, CategoryId) VALUES (?, ?, (SELECT CategoryId FROM Categories WHERE CategoryLink = ?))
    ''', (SubcategoryName, SubcategoryLink, CategoryLink))
    DataBase.commit()
    DataBase.close()


def InsertIntoSubcategoryTypes(SubcategoryLink, SubcategoryTypeLink, SubcategoryTypeName):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT INTO SubcategoryTypes(SubcategoryTypeName, SubcategoryTypeLink, SubcategoryId) VALUES (?, ?, (SELECT SubcategoryId FROM Subcategories WHERE SubcategoryLink = ?))
    ''', (SubcategoryTypeName, SubcategoryTypeLink, SubcategoryLink))
    DataBase.commit()
    DataBase.close()


def InsertIntoProducts(SubcategoryTypeLink, ProductName, ProductLink, SubcategoryId):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT OR IGNORE INTO Products(ProductName, ProductLink, ProductSubId, SubcategoryId) 
    VALUES (?, ?, (SELECT SubcategoryTypeId FROM SubcategoryTypes WHERE SubcategoryTypeLink = ?), ?)
    ''', (ProductName, ProductLink, SubcategoryTypeLink, SubcategoryId))
    DataBase.commit()
    DataBase.close()


def GetSubcategoryId(SubcategoryName):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT SubcategoryId FROM Subcategories WHERE SubcategoryName = ?
    ''', (SubcategoryName,))
    SubcategoryId = Cursor.fetchone()
    DataBase.close()
    return SubcategoryId


def InsertIntoProductsBySubcategoryId(ProductName, ProductLink, SubcategoryId):
    DataBase = sqlite3.connect('Texnomart.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
        INSERT OR IGNORE INTO Products(ProductName, ProductLink, SubcategoryId) 
        VALUES (?, ?, ?)
        ''', (ProductName, ProductLink, SubcategoryId))
    DataBase.commit()
    DataBase.close()


# ----------------------------------------------TelegramBot---------------------------------------

