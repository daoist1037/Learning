import re
import requests
import json

class LeTvSpider(object):
    COMMENT_URL = 'http://api-my.le.com/vcm/api/list?jsonp=jQuery191020323648760135704_1583482519198'\
                    '&type=video&rows=20&page=1&sort=&cid=2&source=1&xid=1496647&pid=44348&ctype=cmt%2Cimg%2Cvote&'\
                    'listType=1&_=1583482519202'
    HEADERS = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Cookie': 'tj_lc=30854d4e8df3588eccc641039fab11d2; tj_uuid=-_15834779054275746587; tj_env=1; language=zh-cn; sso_curr_country=CN; ssoCookieSynced=1; ark_uuid=ck-39d40ba8-919a-4b25-9d44-0d43d227db90-0306-145824; bd_xid=30854d4e8df3588eccc641039fab11d2; tj_v2c=-1496647_2; _ga=GA1.2.579619591.1583482254; _gid=GA1.2.255761960.1583482254',
                'Host': 'api-my.le.com',
                'Referer': 'http://www.le.com/ptv/vplay/1496647.html',
                'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66'
                }
    def __init__(self,url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()     #如此创建该类的时候，函数也会运行
        self.get_comment()
    def get_source(self,url,headers):
        return requests.get(url,headers).content.decode()
    def get_necessary_id(self):
        source = self.get_source(self.url,self.HEADERS)
        vid = re.search(r'vid: (\d+)', source).group(1)
        pid = re.search(r'pid: (\d+)', source).group(1)
        self.necessary_info['xid'] = vid
        self.necessary_info['pid'] = pid
    def get_comment(self):
        url = self.COMMENT_URL.format(xid=self.necessary_info['xid'],pid=self.necessary_info['pid'])
        source = self.get_source(url,self.HEADERS)
        source_json = source[source.find('{"'): -1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人：{comment["user"]["username"]}，评论内容：{comment["content"]}')
if __name__ == '__main__':
    spider = LeTvSpider('http://www.le.com/ptv/vplay/1496647.html')