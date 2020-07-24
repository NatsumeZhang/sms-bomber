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

    def get_response(self):
        time_now = int(time.time() * 1000)

        data = {
            "mobilePhone": self.mobile
        }

        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header
                                     )
            print(response.content)
            print("{}:{}>>>Succeeded".format(self.url, self.mobile))
        except Exception:
            print("{}:{}>>>Failed".format(self.url, self.mobile))

    def run(self):
        self.get_response()


if __name__ == "__main__":
    # +86 supported yet
    mobile = ""
    mobile = input("Phone input: ")
    sms_send_1(mobile).run()
