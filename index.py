#!C:\Users\lenovo\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type: text/html; charset=euc-kr\n")



import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = '박재혁'
    description = '안녕하세요'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="p.py">박재혁</a></h1>
  <p>
		<img src="\img\ss.png" width="245">
	</p>	
  <ol>
    <li><a href="p.py?id=HTML">자기소개</a></li>
    <li><a href="p.py?id=CSS">파이썬</a></li>
    <li><a href="p.py?id=JavaScript">각오</a></li>
    
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))