import sqlite3
import os
# DataBase = sqlite3.connect('Texnomart.db')
# Cursor = DataBase.cursor()
# ProductName = 'Аксессуары для авто Baseus освежитель CRJHQ01 02 White'
# Cursor.execute('''
#    SELECT * FROM Products WHERE ProductName = ?
#    ''', (ProductName, ))
# Data = Cursor.fetchall()
# DataBase.close()
# print(Data)


# import requests
# from bs4 import BeautifulSoup
# from Configs import *
# import time
#
#
# def ProductCategoryParser():
#     Html = requests.get('https://texnomart.uz/ru/katalog/aksessuary-dlya-telefonov', headers=GetUserAgent()).text
#     Soup = BeautifulSoup(Html, 'html.parser')
#
#     ProductCategory = Soup.find('div', class_='category__wrap')
#     Products = ProductCategory.find_all('div', class_='category__item')
#     for Product in Products:
#         ProductLink = HOST + Product.find('a', class_='category__link').get('href')
#         ProductName = Product.find('h2', class_='content__title').get_text(strip=True)
#         print(ProductName)
#         print(ProductLink)
#         try:
#             CheckIfExistsCategory(ProductLink)
#         except:
#             ProductsParser(ProductLink)
#
#
# def CheckIfExistsCategory(ProductLink):
#     time.sleep(1)
#     Html = requests.get(ProductLink, headers=GetUserAgent()).text
#     Soup = BeautifulSoup(Html, 'html.parser')
#     ProductCategory = Soup.find('div', class_='category__wrap')
#     Products = ProductCategory.find_all('div', class_='category__item')
#     for Product in Products:
#         ProductLink1 = HOST + Product.find('a', class_='category__link').get('href')
#         ProductName = Product.find('h2', class_='content__title').get_text(strip=True)
#         print(ProductName)
#         print(ProductLink1)
#         ProductsParser(ProductLink1)
#
#
# def ProductsParser(ProductLink):
#     time.sleep(1)
#     Html = requests.get(ProductLink, headers=GetUserAgent()).text
#     Soup = BeautifulSoup(Html, 'html.parser')
#     try:
#         Pages = Soup.find('div', class_='pagination')
#         Buttons = Pages.find_all('button')
#         LastPage = Buttons[-2].get_text(strip=True)
#         print(LastPage)
#         for i in range(1, int(LastPage) + 1):
#             Soup = GetProducts(ProductLink, i)
#             ProductBox = Soup.find('div', class_='products-box')
#             Products = ProductBox.find_all('div', class_='product-item-wrapper')
#             for Product in Products:
#                 ProductDetail = Product.find('div', class_='product-bottom__left')
#                 ProductName = ProductDetail.find('a').get_text(strip=True)
#                 ProductDetailLInk = ProductDetail.find('a').get('href')
#                 print(ProductName)
#                 print(ProductDetailLInk)
#
#     except:
#         ProductBox = Soup.find('div', class_='products-box')
#         Products = ProductBox.find_all('div', class_='product-item-wrapper')
#         for Product in Products:
#             ProductDetail = Product.find('div', class_='product-bottom__left')
#             ProductName = ProductDetail.find('a').get_text(strip=True)
#             ProductDetailLInk = ProductDetail.find('a').get('href')
#             print(ProductName)
#             print(ProductDetailLInk)
#
#
# def GetProducts(ProductLink, i):
#     Html = requests.get(ProductLink + f'?page={i}').text
#     Soup = BeautifulSoup(Html, 'html.parser')
#     return Soup
#
#
# ProductCategoryParser()


