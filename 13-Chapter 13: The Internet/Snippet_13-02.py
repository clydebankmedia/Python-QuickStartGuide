# Import urlopen from the urllib module
from urllib.request import urlopen

# Import regular expression functionality
import re

# Import unescaped from HTML
from html import unescape

# URL to GET
url = "https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&page=Mount_Tambora"

# Request the page
response = urlopen(url)

# Get the page content
page_content = str(response.read())

# Unescape the page
page_content = unescape(page_content)

# Use this regex to find the elevation of Mt. Tambora
regex = r"elevation\_m\s=\s(\d*)"

# Perform the search
result = re.search(regex, page_content)

# Fetch the first match (which is the elevation)
elevation = result[1]

# Print the elevation
print("The elevation of Mt. Tambora is " + str(elevation) + ".")
