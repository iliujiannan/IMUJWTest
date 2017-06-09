import httplib2

class room:
    jxl = ""
    js = ""
    jslx = ""

class jwxt():
    def __init__(self, UserId, Password):
        self.UserId = UserId
        self.Password = Password
        self.oper = "ld"
        self.zxxnxq = "2016-2017-2-2"
        self.zxXaq = "01"
        self.zxJxl = "002"
        self.zxZc = "16"
        self.zxJc = ""
        self.zxxq = "5"
        self.pageNo = None
    def anylisis(self, str1):
        result = []
        temp = str(str1).split("<tbody>")
        str_temp = temp[1]
        list_temp1 = str_temp.split("</tr>")
        for i in range(0, len(list_temp1)-3):
            list_temp2 = list_temp1[i].split("</td>")
            r = room
            r.jxl = list_temp2[2].split("<td>")[1].replace("\r\n\t\t\t\t\t\t\t\t\t\t\t", "").replace("\r\n\t\t\t\t\t\t\t\t\t\t","")
            r.js = list_temp2[3].split("<td>")[1].replace("\r\n\t\t\t\t\t\t\t\t\t\t\t", "").replace("\r\n\t\t\t\t\t\t\t\t\t\t","")
            r.jslx = list_temp2[4].split("<td>")[1].replace("\r\n\t\t\t\t\t\t\t\t\t\t\t", "").replace("\r\n\t\t\t\t\t\t\t\t\t\t","")
            result.append(r)
        return result
    def getCookies(self):
        try:
            conn = httplib2.Http()
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': '	keep-alive',
                'Host': 'jwxt.imu.edu.cn',
                'Referer': 'http://jwxt.imu.edu.cn/',
                'User-Agent': '	Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }
            c1, c = conn.request('http://jwxt.imu.edu.cn/loginAction.do?zjh='+ self.UserId + '&mm=' + self.Password, 'GET', headers=header)
            str1 = str(c.decode('gb2312')).replace(' ', '')
            # print(c1)
            if '不正确' in str1 or '你输入的证件号不存在' in str1:
                return '登录失败'
            else:
                cookie = c1['set-cookie'].replace('; path=/', '')
                return cookie
        except Exception as e:
            print(e)
            return '登录失败'
    def executeGetEmptyRoomList(self):
        cookie = self.getCookies()
        data = "?oper=" + self.oper + "&zxxnxq=" + self.zxxnxq + "&zxXaq=" + self.zxXaq + "&zxJxl=" + self.zxJxl + "&zxZc=" + self.zxZc + "&zxJc=" + self.zxJc + \
               "&zxxq=" + self.zxxq
        data3 = "&zxxnxq=" + self.zxxnxq + "&zxXaq=" + self.zxXaq + "&zxJxl=" + self.zxJxl + "&zxZc=" + self.zxZc + "&zxJc=" + self.zxJc + \
               "&zxxq=" + self.zxxq + "&pagepageSize=20&page=1&currentPage=1"
        url = "http://jwxt.imu.edu.cn/xszxcxAction.do"
        url1 = "http://jwxt.imu.edu.cn/xszxcxAction.do?oper=xszxcx_lb"
        url3 = "http://jwxt.imu.edu.cn/xszxcxAction.do?oper=tjcx"
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': '	keep-alive',
            'Cookie': cookie,
            'Host': 'jwxt.imu.edu.cn',
            'Referer': 'http://jwxt.imu.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        conn = httplib2.Http()
        conn.request(url1, "GET", headers=header)
        conn.request(url + data, "GET", headers=header)
        c1, c = conn.request("http://jwxt.imu.edu.cn/xszxcxAction.do?oper=tjcx&zxxnxq=2016-2017-2-2&zxXaq=01&zxJxl=002&zxZc=16&zxJc=&zxxq=5&pagepageSize=20&page=1&currentPage=1", "GET", headers=header)
        result = str(c.decode('gb2312').replace(' ', ''))
        return self.anylisis(result)


#call
j = jwxt("0151122350", "15248113901")
j.executeGetEmptyRoomList()
