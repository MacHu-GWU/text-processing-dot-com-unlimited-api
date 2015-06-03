##encoding=utf-8

"""
Copyright (c) 2015 by Sanhe Hu
------------------------------
    Author: Sanhe Hu
    Email: husanhe@gmail.com
    Lisence: LGPL
    

Module description
------------------
    This module can make http request to www.text-processing.com to get sentiment analysis result.
    Because it doesn't use www.text-processing.com API, so it's completely free and no limited.
    But if you make too much http requests in short period of time, your IP could be banned.
    
    Generally, this processor works good with text longer than a full sentence. looks its unable to
    detect the underlying sentiment like:
        you are a bitch!
        go to hell!
        I like it.
    
Keyword
-------
    api, text, natural language processing
    
    
Compatibility
-------------
    Python2: Yes
    Python3: Yes
    
    
Prerequisites
-------------
    requests: https://pypi.python.org/pypi/requests
    beautifulsoup4: https://pypi.python.org/pypi/beautifulsoup4

Import Command
--------------
    from textprocessingdotcom import SentimentProcessor
"""

from .processor import SentimentProcessor