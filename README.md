# Ache-Crawler


1. Crawler Used:
The web crawler used is Acne. It is a focused web crawler. It collects the web pages from the web which follow specific criteria. Ache uses page classifiers which specify different patterns for the title, body, url and which distinguishes between relevant and irrelevant pages. It learns automatically to prioritize links to crawl relevant web pages
I have used url_regex in page_classifier which contains regular expression and consider the web page relevant if the url matches them.

  Example: pageclassifier.yml
  type: url_regex parameters:
  regular_expressions: [
"https:\\/\\/www\\.ezcontacts\\.com\\/product\\/eyeglasses\\/.*", "https:\\/\\/www\\.ezcontacts\\.com\\/womens\\-eyeglasses\\/frame\\-type\\:full\\-frame\\/.*", "https://www.ezcontacts.com/eyeglasses",
"https://www.ezcontacts.com/mens-eyeglasses", "https://www.ezcontacts.com/womens-eyeglasses", "https://www.ezcontacts.com/womens-eyeglasses/frame-type:full-frame"]

  The command I used to run the ache is as below:
    ache startCrawl -o output -c config/config_focused_crawl -s seeds/sample.seeds -m test
