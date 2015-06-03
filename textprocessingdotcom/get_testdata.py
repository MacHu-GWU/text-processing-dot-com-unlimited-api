##encoding=utf-8

"""
Make test text processing on http://text-processing.com/demo/sentiment/
"""

from __future__ import print_function, unicode_literals
import requests

def get_http_response(text):
    request_url = "http://text-processing.com/demo/sentiment/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
        "Referer": "http://text-processing.com/demo/sentiment/",
        }
    res = requests.post(request_url, headers=header, 
                        data={"language": "english", "text": text})
    return res.text

def write2file(fname, text):
    with open(fname, "w") as f:
        f.write(text)
        
if __name__ == "__main__":
    write2file("pos.html", get_http_response("Looks great, give me time to play around with it some more and maybe I'll have some suggestions."))
    write2file("neg.html", get_http_response("I do not like the updateed weather bug at all. I've used it for several years, but I am now thinking of deleting it."))
    write2file("netrual.html", get_http_response("Apple is red."))
    write2file("netrual_pos.html", get_http_response("I like it a lot."))
    write2file("netrual_neg.html", get_http_response("No. I would like to see this part of the app gone."))