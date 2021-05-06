## UML Class Diagram:
![Alt text](./static/uml.png?raw=true "UML Class Diagram")

#### We use Selenium webdriver and beautiful soup 4 for scraping data from Amazon and Tapaz, and Rapid Api to get data from Aliexpress.

## How framework works:

#### Each child of Scraper interface has its own implementation of scrape method which returns the list of dictionaries. Driver class provides webdriver for both scraper classes (Amazon and Tapaz)

#### In Displayer abstract class Template hook design pattern is used, display method is template part, and the steps of algorithm are given with appropriate static and abstract methods. Display methods take the scraped list and change it according to provided options.
