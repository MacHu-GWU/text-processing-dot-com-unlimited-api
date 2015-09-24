text-processing-dot-com unlimited api
================================================================================

Wanna extract the polarity (pos or neg) and the sentiment value (from 0.0 to 1.0) from text? The basic idea is easy, but building a system suit for arbitrary long and complex text is way more difficult than you think.

`textblob <https://textblob.readthedocs.org/en/stable/>`_, a Python NLTK (nature language tool kits), provides a simple sentimental analysis API. But we cannot use that in production envrionment because of it's poor accuracy and speed.

http://text-processing.com/demo/sentiment is a sentiment anaylysis web service, they have huge corpus in the backend to support it's high performance and accuracy. So I come up an idea of making a web bot to call their free http API. Enjoy hacking.


Download and Install
--------------------------------------------------------------------------------

**Download** 

Download here: https://github.com/MacHu-GWU/text-processing-dot-com-unlimited-api/archive/master.zip

**Install**

In windows:

.. code-blcok: console

	cd text-processing-dot-com-unlimited-api\textprocessingdotcom
	python zzz_manual_install.py

In unix or mac, just put ``textprocessingdotcom`` directory into your python site-packages folder

Sentiment Analysis API
--------------------------------------------------------------------------------

This module can make http request to http://text-processing.com/demo/sentiment to get sentiment analysis result. Because it doesn't use www.text-processing.com API, so it's completely free and no limited. But if you make too much http requests in short period of time, your IP could be banned for short time.

Usage example::

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	from __future__ import print_function, unicode_literals
	from textprocessingdotcom import SentimentProcessor
	
	processor = SentimentProcessor()
	text = "I don't like it."
	print(processor.process(text))