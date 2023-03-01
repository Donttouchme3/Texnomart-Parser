import requests
from bs4 import BeautifulSoup
import time

from Configs import GetUserAgent, URL, HOST
from WorkWithDataBase import *


class TexnomartParser:
    def __init__(self):
        self.Url = URL
        self.Host = HOST
        self.Header = GetUserAgent()

    def GetHtml(self, Url):
        Html = requests.get(Url, headers=self.Header).text
        Soup = BeautifulSoup(Html, 'html.parser')
        return Soup

    def CatalogParser(self):
        time.sleep(1)
        Soup = self.GetHtml(self.Url)
        CatalogContainer = Soup.find('div', class_='category__wrap')
        CategoryItem = CatalogContainer.find_all('div', class_='category__item')
        for Category in CategoryItem:
            CategoryLink = self.Host + Category.find('a', class_='category__link').get('href')
            CategoryName = Category.find('h2', class_='content__title').get_text(strip=True)
            # InsertIntoCategories(CategoryName, CategoryLink)
            self.CategoryParser(CategoryLink)

    def CategoryParser(self, CategoryLink):
        Soup = self.GetHtml(CategoryLink)
        try:
            CategoryWrap = Soup.find('div', class_='category__wrap')
            CategoryItem = CategoryWrap.find_all('div', class_='category__item')
            for Subcategory in CategoryItem:
                SubcategoryLink = self.Host + Subcategory.find('a', class_='category__link').get('href')
                SubcategoryName = Subcategory.find('h2', class_='content__title').get_text(strip=True)
                # InsertIntoSubcategories(CategoryLink, SubcategoryName, SubcategoryLink)
                SubcategoryId = GetSubcategoryId(SubcategoryName)[0]
                self.SubcategoryParser(SubcategoryLink, int(SubcategoryId))
        except:
            pass

    def SubcategoryParser(self, SubcategoryLink, SubcategoryId):
        time.sleep(1)
        Soup = self.GetHtml(SubcategoryLink)
        try:
            CategoryWrap = Soup.find('div', class_='category__wrap')
            CategoryItem = CategoryWrap.find_all('div', class_='category__item')
            for SubcategoryType in CategoryItem:
                SubcategoryTypeLink = SubcategoryType.find('a', class_='category__link').get('href')
                SubcategoryTypeName = SubcategoryType.find('h2', class_='content__title').get_text(strip=True)
                print(SubcategoryTypeName)
                # InsertIntoSubcategoryTypes(SubcategoryLink, SubcategoryTypeLink, SubcategoryTypeName)
                try:
                    self.CheckIfExistsCategory(Link=f'{self.Host + SubcategoryTypeLink}', AddLink=SubcategoryTypeLink, SubcategoryId=SubcategoryId)
                except:
                    self.ProductCategoryParser(SubcategoryTypeLink, SubcategoryTypeLink, SubcategoryId)
        except:
            try:
                Pages = Soup.find('div', class_='pagination')
                Buttons = Pages.find_all('buttons')
                LastPage = Buttons[- 2]
                for i in range(1, int(LastPage) + 1):
                    Soup = self.GetPageHtml(SubcategoryLink, i)
                    ProductsBox = Soup.find('div', class_='products-box')
                    Products = ProductsBox.find_all('div', class_='product-item-wrapper')
                    for Product in Products:
                        ProductDetail = Product.find('div', class_='product-bottom')
                        ProductName = ProductDetail.find('h3').get_text(strip=True)
                        ProductLink = self.Host + ProductDetail.find('a', class_='product-name').get('href')
                        print(ProductName)
                        print(ProductLink)
                        try:
                            InsertIntoProductsBySubcategoryId(ProductName, ProductLink, SubcategoryId)
                            print('Добавлено')
                        except Exception as e:
                            print(e)
            except:
                try:
                    ProductsBox = Soup.find('div', class_='products-box')
                    Products = ProductsBox.find_all('div', class_='product-item-wrapper')
                    for Product in Products:
                        time.sleep(1)
                        ProductDetail = Product.find('div', class_='product-bottom')
                        ProductName = ProductDetail.find('h3').get_text(strip=True)
                        ProductLink = self.Host + ProductDetail.find('a', class_='product-name').get('href')
                        print(ProductName)
                        print(ProductLink)
                        try:
                            InsertIntoProductsBySubcategoryId(ProductName, ProductLink, SubcategoryId)
                            print('Добавлено')
                        except:
                            print('Нечего добавлять')
                except Exception as e:
                    print(e)

    def ProductCategoryParser(self, SubcategoryTypeLink, AddLink, SubcategoryId):
        Soup = self.GetHtml(Url=f'{self.Host + SubcategoryTypeLink}')
        time.sleep(1)
        try:
            Pages = Soup.find('div', class_='pagination')
            Buttons = Pages.find_all('button')
            LastPage = Buttons[-2].get_text(strip=True)
            print(LastPage)
            for Page in range(1, int(LastPage) + 1):
                time.sleep(1)
                Soup = self.GetPageHtml(SubcategoryTypeLink=f'{self.Host + SubcategoryTypeLink}', Page=Page)
                ProductsBox = Soup.find('div', class_='products-box')
                Products = ProductsBox.find_all('div', class_='product-item-wrapper')
                for Product in Products:
                    ProductDetail = Product.find('div', class_='product-bottom')
                    ProductName = ProductDetail.find('h3').get_text(strip=True)
                    ProductLink = self.Host + ProductDetail.find('a', class_='product-name').get('href')
                    print(ProductName)
                    print(ProductLink)
                    try:
                        InsertIntoProducts(AddLink, ProductName, ProductLink, SubcategoryId)
                        print('Добавлено')
                    except Exception as e:
                        print(e)
        except:
            try:
                ProductsBox = Soup.find('div', class_='products-box')
                Products = ProductsBox.find_all('div', class_='product-item-wrapper')
                for Product in Products:
                    time.sleep(1)
                    ProductDetail = Product.find('div', class_='product-bottom')
                    ProductName = ProductDetail.find('h3').get_text(strip=True)
                    ProductLink = self.Host + ProductDetail.find('a', class_='product-name').get('href')
                    print(ProductName)
                    print(ProductLink)
                    try:
                        InsertIntoProducts(AddLink, ProductName, ProductLink, SubcategoryId)
                        print('Добавлено')
                    except:
                        print('Нечего добавить')
            except Exception as e:
                print(e)

    # -------------------------------------Доп Функции ----------------------------------

    def GetPageHtml(self, SubcategoryTypeLink, Page):
        Html = requests.get(SubcategoryTypeLink + f'?page={Page}').text
        Soup = BeautifulSoup(Html, 'html.parser')
        return Soup

    def CheckIfExistsCategory(self, Link, AddLink, SubcategoryId):
        Soup = self.GetHtml(Link)
        ProductCategory = Soup.find('div', class_='category__wrap')
        Products = ProductCategory.find_all('div', class_='category__item')
        for Product in Products:
            ProductLink = Product.find('a', class_='category__link').get('href')
            ProductName = Product.find('h2', class_='content__title').get_text(strip=True)
            print(ProductName)
            print(ProductLink)
            self.ProductCategoryParser(ProductLink, AddLink, SubcategoryId)


if __name__ == '__main__':
    Parser = TexnomartParser()
    Parser.CatalogParser()
