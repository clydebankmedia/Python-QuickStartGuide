# Import the urllib module
import urllib.request

# URL to GET
url = "https://www.python.org/"

# Get the page content
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
  page_content = response.read()

# Save to python.html, writing in binary mode
# to preserve encoding defined by web server
with open("python.html", mode = "wb") as f:
	f.write(page_content)
