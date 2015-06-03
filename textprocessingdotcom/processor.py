##encoding=utf-8

"""
Import Command
--------------
    from textprocessingdotcom.processor import SentimentProcessor
"""

from bs4 import BeautifulSoup as BS4
import requests
import time

def decimal_filter(text):
    res = list()
    for char in text:
        if char in "1234567890.":
            res.append(char)
    if len(res) > 0:
        return float("".join(res))
    else:
        return None

class SentimentProcessor():
    def __init__(self):
        self.request_url = "http://text-processing.com/demo/sentiment/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
            "Referer": "http://text-processing.com/demo/sentiment/",
            }
        self.sleeptime = 0
    
    def set_sleeptime(self, sleeptime_in_second):
        self.sleeptime = sleeptime_in_second
        
    def http_post(self, text):
        """make a http post to "http://text-processing.com/demo/sentiment/", get their analysis
        result, return the html text
        """
        time.sleep(self.sleeptime) # wait for #self.sleeptime seconds
        try:
            res = requests.post(self.request_url, headers=self.header, 
                                data={"language": "english", "text": text})
            return res.text
        except:
            return None
        
    def extract(self, html):
        """extract polarity and positive score from html
        """
        polarity, score = None, None
        try:
            soup = BS4(html)
            # find pos, neg, netrual
            for strong in soup.find_all("strong"):
                try:
                    if strong["class"] == ["large", "positive"]:
                        polarity = "pos"
                    elif strong["class"] == ["large", "negative"]:
                        polarity = "neg"
                    elif strong["class"] == ["large", "quiet"]:
                        polarity = "neutral"
                except:
                    pass
            
            # find positive value
            try:
                li_positive = soup.find("li", class_="positive")
                score = decimal_filter(li_positive.text)
            except:
                pass
            
            # fix score when polarity is neutral
            if polarity == "neutral":
                score = 0.5
            
            return polarity, score
        except:
            return None
        
    def process(self, text):
        return self.extract(self.http_post(text))

if __name__ == "__main__":
    import unittest
    from pprint import pprint as ppt

    def read(fname):
        with open(fname, "r") as f:
            return f.read()
        
    processor = SentimentProcessor()
    
    class SentimentProcessorUnittest(unittest.TestCase):
        def test_extract(self):
            ppt(processor.extract(read("pos.html")))
            ppt(processor.extract(read("neg.html")))
            ppt(processor.extract(read("netrual.html")))
            ppt(processor.extract(read("netrual_pos.html")))
            ppt(processor.extract(read("netrual_neg.html")))
        
        def test_process(self):
            ppt(processor.process("It helps me saving money"))
                
    unittest.main()