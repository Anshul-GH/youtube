# Lets user python to scrape simple webpage and read data.
# We will use a module/lib called scrapy for this.

# We will scrap data from the following url:
# http://quotes.toscrape.com/

# Lets get started !!

# 1. Install the scrapy module 
# 2. Open the terminal or cmd (for windows) in the directory 
# location where you are working
# 3. Create a new scrapy project using the following command
# scrapy startproject MyScrapper
# This will create a project directory with some auto-generated code
# 4. Next we will create a new 'spider' or the actual
# bot or web crawler that will scrape the data. For that
# move to the directory 'spiders' i the terminal
# 5. Create a new spider using the command:
# scrapy genspider myspd "http://quotes.toscrape.com/"
# The URL is the one from which we wish to scrape the data
# 6. This has generated another set of code (auto-generated) 
# that will contain the actual spider or crawler class
# this is also sometimes referred to as boiler-plate code
# The parse module within the spider calls - myspd.py 
# is the one where we will write the actual steps and
# identify the attributes to scrape.
# 7. Comment the 'allowed_domains' variable for simplicity
# and also verify the 'start_urls' attribute to contain 
# the correct url - http://quotes.toscrape.com/

# 8. Next we need to inspect the backend elements of the url to identify the attributes that we need
# to read via the spider
# We need to read the Auther name and the corresponding Quote
# If you understand elementary HTML/CSS, this is how the 
# attribute values can be referenced:
# attribute = <tageName>.<className>::<textContent>
# # Hence in our scenario:
# authorName="small.author::text"
# quotes="span.text::text"

# If you are facing difficulty understanding this 
# its worth reviewing some HTML/CSS basics. I have tried to keep it very simple though

# 9. Since these values will be a part of the response that
# the spider/crawler will fetch, this is how it will be syntactically
# read within the code:

# Also, there is a way to validate if the tag references we
# have identified are correct or not. For that we need to use
# scrapy shell. Lets see that:
# The command for that is: scrapy shell url
# scrapy shell "http://quotes.toscrape.com/"
# Lets test the references now

# So the references seem to be working fine.

# Next, lets run the actual crawler and see if the values are getting read via the 
# python code as well, the same way:

# Lets run the crawler now
# This is the command to use:
# scrapy crawl myspd
# Where myspd is the name of the spider/crawler

# So we are getting the values as expected.
# Cool :)

# 10. Next, the core idea is to be able to store and use
# the scraped data. The simplest way to do that is to write the
# output to some file. Most common - xml or json

# Lets try to write the output to a xml file.
# Command for that: 
# scrapy crawl myspd -o data.xml

# The file got created, but there is no data within.

# The reason for that is because scrapy has another class called
# items that is responsible for defining the attributes that we
# are looking to scrape and store

# We will have to define the attributes within this 'items' calls
# Attributes - values that we need to scrape and also store

# next we will have to go back to the spider class and add a 
# reference to the items class and use its object to store 
# the values

# Lets run the crawler again

# We got the scrapped data in the XML
# Pretty Coool :)

# Hope this helps.
# I am a learner myself, not an expert with videographing my work
# just looking to share and help 

# thanks !! :)