# encoding:utf-8

import requests
import time


class sms_send_1(object):
    """http://register.818long.com/register.jsp"""

    def __init__(self, mobile):
        self.url = "http://register.818long.com/securityInfo"
        self.header = {
            "Referer": "http://register.818long.com/register.jsp",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        self.mobile = mobile

    def run(self):
        data = {
            "mobilePhone": self.mobile
        }
        get_response(self.url, data, self.header, mobile)


class sms_send_2(object):
    """https://account.xiaomi.com/pass/sendServiceLoginTicket"""

    def __init__(self, mobile):
        self.url = "https://account.xiaomi.com/pass/sendServiceLoginTicket"
        self.header = {
            "User-Agent": "APP/com.xiaomi.miwatch APPV/1.3 iosPassportSDK/3.6.8 iOS/13.6 miHSTS",
            'Cookie': 'deviceId=EE6F43D7820CECC5; sdkVersion=3.6.8',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.mobile = mobile

    def run(self):
        data = 'sid=miothealth&user=' + str(self.mobile)
        get_response(self.url, data, self.header, mobile)


def get_response(url, data, header, mobile):
    try:
        response = requests.post(url=url,
                                 data=data,
                                 headers=header
                                 )
        print(response.content)
        print("{}:{}>>>Succeeded".format(url, mobile))
    except Exception:
        print("{}:{}>>>Failed".format(url, mobile))


if __name__ == "__main__":
    # +86 supported yet
    mobile = ""
    mobile = input("Phone input: ")
    sms_send_1(mobile).run()
    sms_send_2(mobile).run()
