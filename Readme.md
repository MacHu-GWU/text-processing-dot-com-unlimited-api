#text-processing-dot-com unlimited api

##Install

Run text-processing-dot-com-unlimited-api\textprocessingdotcom\manual_install.py with Python2/Python3

##Sentiment Analysis API

This module can make http request to [http://text-processing.com/demo/stem/](http://text-processing.com/demo/stem/) to get sentiment analysis result. Because it doesn't use www.text-processing.com API, so it's completely free and no limited. But if you make too much http requests in short period of time, your IP could be banned.

**Usage example**

	##encoding=utf-8
	
	from __future__ import print_function
	from textprocessingdotcom import SentimentProcessor
	
	processor = SentimentProcessor()
	text = "I don't like it."
	print(processor.process(text))