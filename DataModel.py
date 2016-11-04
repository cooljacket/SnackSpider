# -*- coding:utf-8 -*-
import re

from SinglePageSpider import SinglePageSpider


class DataModel:
	def __init__(self, url, pattern, resultFileName, coding="utf-8"):
		self.url = url
		self.pattern = pattern
		self.coding = coding
		self.saveResults(resultFileName, self.getPage())


	def getPage(self):
		page = SinglePageSpider().getPage(self.url, self.coding)
		results = re.findall(self.pattern, page)
		return results


	def saveResults(self, fileName, results):
		head = '''
<!DOCTYPE html>
<html>
<head>
	<title>淘宝最热门零食抓取结果</title>
</head>
<body>
'''

		tail = '''
</body>
</html>
'''

		with open(fileName, 'w') as f:
			f.write(head)
			for item in results:
				f.write("<div>")
				f.write('<img src="http://{0}" width="200px" height="200px" onclick="location=\'http:{1}\'"><br>'
					.format(item[1], item[2]))
				f.write('<span style="color:blue" onclick="location=\'http:{0}\'">商品名：{1}</span><br>'.format(item[2], item[0]))
				f.write('<span>销量：{0}</span><br>'.format(item[4]))
				f.write('<span>价格：{0}</span><br>'.format(item[3]))
				f.write('<span>评论数：{0}</span><br>'.format(item[5]))
				f.write('</div>')
			f.write(tail)