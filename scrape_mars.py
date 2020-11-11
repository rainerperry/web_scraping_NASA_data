from splinter import Browser
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    scraped_mars = {}
    # URL OF NASA website to be scraped
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # find the relevant class items for the title and scrape it
    step1 = soup.find('ul', class_='item_list')
    results = step1.find('li', class_="slide")
    title = results.find('div', class_="content_title").text

    #find the relevatn class items for paragraph and scrape them
    paragraph = results.find('div', class_="article_teaser_body").text

    #store data in dictionary
    scraped_mars["title"] = title
    scraped_mars["paragraph"] = paragraph

    #Scrape fatured image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('figure', class_='lede')
    image_link = image_url.a["href"]
    featured_image_url = 'https://www.jpl.nasa.gov' + image_link

    scraped_mars["featured_image_url"] = featured_image_url

    #add scraped image to dictionary?

    #Scrape Mars Facts
    url = 'https://space-facts.com/mars'
    mars_facts = pd.read_html(url)
    df = mars_facts[0]
    mars_details = df.to_html()

    scraped_mars["mars_details"] = mars_details

    #Scrape Mars Hemispheres & Images

    # url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser').find_all("a", class_="itemLink product-item")
    # hemi_titles = []
    # for i in soup:
    #     title = i.find("h3").text
    #     hemi_titles.append(title)
    #
    # url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(url)
    # hemi_list = []
    #
    # for title in range(len(hemi_titles)):
    #     dictionary = {}
    #
    #     browser.find_by_css("a.product-item h3")[title].click()
    #
    #     step1 = browser.links.find_by_text('Sample').first
    #
    #     dictionary['img_url'] = step1['href']
    #     dictionary['title'] = browser.find_by_css("h2.title")
    #
    #     hemi_list.append(dictionary)
    #     browser.back()

    # Close the browser after scraping
    browser.quit()

    # Return results
    return scraped_mars