##encoding=utf-8

"""
This is a web app you can use to do batch sentiment analysis.
Notice: To use this app, first edit the ip address at the bottom of this script first.

Prerequisite
------------
    numpy, pandas, bottle
"""

from textprocessingdotcom import SentimentProcessor
import pandas as pd
import bottle
import datetime
import os
import time

processor = SentimentProcessor()

class Payload():
    def __init__(self):
        self.data = {
            "batch_query_result": None
            }

@bottle.route("/")
def index():
    payload = Payload()
    return bottle.template("index", payload.data)

@bottle.post("/result")
def get_sentiment_analysis_result():
    payload = Payload()
    upload = bottle.request.files.get("upload")
    filename = str(datetime.datetime.now().timestamp()) # add timestamp as surfix
    uploadpath = r"user_uploaded\%s.tmp" % filename
    upload.save(uploadpath)
    
    # read user uploaded data
    try:
        df = list()
        with open(uploadpath, "r") as f:
            for line in f.read().strip().split("\n"):
                df.append([line,])
    except:
        pass
    
    for row in df:
        res = processor.process(row[0])
        if res:
            row.append(res[0])
            row.append(res[1])
        else:
            row.append(None)
            row.append(None)
    df = pd.DataFrame(df, columns=["text", "polarity", "positive score"])
    df.to_csv(r"user_uploaded\%s.csv" % filename, index=False)
    
    payload.data["batch_query_result"] = "%s.csv" % filename
    return bottle.template("index", payload.data)

@bottle.route("/<filename>")
def serve_static(filename):
    if filename == "example_input.txt":
        return bottle.static_file(filename, root="static")
    else:
        return bottle.static_file(filename, root="user_uploaded")

if __name__ == "__main__":
    try:
        os.mkdir("user_uploaded")
    except:
        pass
    bottle.run(host="10.255.145.57", port=8081) # <=== Edit this IP address