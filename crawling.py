import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 브랜드명 크롤링
def brand(select_brand) :
    return select_brand.select_one(".li_inner > .article_info > .item_title").text.strip()

# 상품명 크롤링
def product(select_product): 
    return select_product.select_one(".li_inner > .article_info > .list_info > a")["title"].strip().replace(".", "")

# 리뷰 수 null 값 체크 ( 리뷰가 없는 상품 0으로 반환 )
def review(select_review) :
    try : 
        return select_review.select_one(".point").text.strip()
    except :
        return 0
    
# 가격 크롤링 ( 할인 가격 정보 제외한 정가 정보 표시 )
def price(select_price) :
    if len(select_price.select_one(".price").text.strip().split()) == 1 :
        return  select_price.select_one(".price").text.strip().split()[0]
    elif len(select_price.select_one(".price").text.strip().split()) == 2 :
        return  select_price.select_one(".price").text.strip().split()[1]
    
# 좋아요 크롤링( None 값 오류 방지 예외처리 )
def heart(select_heart) : 
    try : 
        if select_heart.select_one(".li_inner >.article_info > .txt_cnt_like ") is not None :  
            return select_heart.select_one(".li_inner >.article_info > .txt_cnt_like ").text.strip()
    except :
        return 0