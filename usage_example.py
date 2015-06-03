##encoding=utf-8

from __future__ import print_function
from textprocessingdotcom import SentimentProcessor

processor = SentimentProcessor()
text = "I don't like it."
print(processor.process(text))