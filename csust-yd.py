import requests

def check():
    global count
    url = 'https://www.baidu.com'
    try:
        requests.get(url, timeout=1)
        print('network connected.')
    except:
        if count == 3 :
            print('connection error! please try to reconnect or try it later.')
            return 0
        count += 1
        print('logging in...')
        login()

def login():
    account = ''
    password = ''
    url = 'http://1.1.1.1/?isReback=1'
    try:
        r = requests.get(url, allow_redirects=False, timeout=2)
        url2 = r.headers['Location']
        index1 = url2.find('wlanuserip')
        index2 = url2.find('wlanacname')
        index3 = url2.find('wlanacip')
        index4 = url2.find('wlanusermac')
        wlanuserip = url2[index1+len('wlanuserip')+1:index2-1]
        wlanacname = url2[index2+len('wlanacname')+1:index3-1]
        wlanacip = url2[index3+len('wlanacip')+1:index4-1]
        wlanusermac = url2[index4+len('wlanusermac')+1:index4+len('wlanusermac')+13]
        maclist = list()
        j = 1
        for i in range(1, 18):
            if i % 3 == 0 :
                maclist.append('-')
                j += 1
            else:
                maclist.append(wlanusermac[i-j])
        wlanusermac = ''.join(maclist)
        post_url = 'http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanuserip={wlanuserip}&wlanacip={wlanacip}&wlanacname={wlanacname}&mac={wlanusermac}&ip={wlanuserip}&enAdvert=0&queryACIP=0&loginMethod=1'.format(
            wlanuserip=wlanuserip, wlanacip=wlanacip, wlanacname=wlanacname, wlanusermac=wlanusermac
            )
        post_data = {
            'DDDDD': ',0,' + account, 
            'upass': password, 
            'R1': '0', 
            'R2': '0', 
            'R3': '0', 
            'R6': '0', 
            'para': '00', 
            '0MKKey': '123456'
            }
        requests.post(url=post_url, data=post_data)
        check()
    except:
        print('connection error! please try to reconnect or try it later.')

count = 0
check()