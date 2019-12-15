from html.parser import HTMLParser


class HTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("attr:", attr)

    def handle_endtag(self, tag):
        print("End tag:", tag)

    def handle_comment(self, data):
        print("Comment:", data)

    def handle_data(self, data):
        print("Data:", data)

html_input = """
<html>
<head><title>Welcome!</title></head>
<body>
<!--This is a comment-->
<h2>An Unordered HTML List</h2>
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>  
<h2>An Ordered HTML List</h2>
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol> 
</body>
</html>
"""
parser = HTMLParser()
parser.feed(html_input)

