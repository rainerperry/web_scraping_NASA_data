# Web Scraping - Mars Mission Data

Building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 


### Scraping

- Creating a Jupyter Notebook to complete all scraping and analysis tasks. 
- Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) and collecting the latest News Title and Paragraph Text. 
- Assigning the text to variables that can be referenced later.
- Visiting the url for JPL Featured Space Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
- Using splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string 
- Making sure to find the image url
- Making sure to save a complete url string for this image.
- Visiting the Mars Facts webpage (https://space-facts.com/mars/) and using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Using Pandas to convert the data to a HTML table string.
- Visiting the USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
- Saving both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name, using a Python dictionary 
- Appending the dictionary with the image url string and the hemisphere title to a list.

### MongoDB and Flask Application

-Using MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
-Starting by converting Jupyter notebook into a Python script that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
-Creating a route cthat will import the py script and call the scrape function.
-Storing the return value in Mongo as a Python dictionary.
-Creating a root route that will query the Mongo database and pass the mars data into an HTML template to display the data.
-Creating a template HTML file that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
