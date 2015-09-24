<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Sentiment Analyzer</title>
</head>
<body>

<div>Sentiment Analyzer, url = http://10.255.145.57:8081/</div>
<div>Author: Sanhe Hu, 2015-09-24</div>
<br>
<form action="/result" method="POST" enctype="multipart/form-data">
  Select a csv or txt File: <input type="file" name="upload" />
  <input type="submit" value="Start upload and process" />
</form>

%if batch_query_result:
	<a href={{batch_query_result}}>download result csv file</a>
%else:
	<a href=example_input.txt>click here to view example of valid input file</a>
%end
</body>
</html>