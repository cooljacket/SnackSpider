# -*- coding:utf-8 -*-
import sys

from DataModel import DataModel


def main(args):
	model = DataModel(
		url = 'https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161104&sort=sale-desc',
		pattern = '"raw_title":"([^"]*)","pic_url":"([^"]*)","detail_url":"([^"]*)","view_price":"([^"]*)","view_fee":"[^"]*","item_loc":"[^"]*","reserve_price":"[^"]*","view_sales":"(\d+)人付款","comment_count":"(\d+)"',
		resultFileName = 'result.html'
		)

	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))
