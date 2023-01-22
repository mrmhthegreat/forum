import requests

def send_otp(mobile):
    apiSecret = "27206b956ffd0bb1027855a97d9d66f987ae3162"
    message = {"secret": apiSecret,"type": "sms","mode": "devices","device": "f2a372ae-44d2-f6a9-3579-491012522678","sim": 1,"phone": "+923175041207","message": "Your OTP is {{otp}}"}
    r = requests.post(url = "https://www.cloud.smschef.com/api/send/otp", params = message)
    result = r.json()
    return result
def verfiy_otp(otpCode):
    apiSecret = "27206b956ffd0bb1027855a97d9d66f987ae3162"
    r=requests.get(url = "https://www.cloud.smschef.com/api/get/otp", params = {
    "secret": apiSecret,
    "otp": otpCode}) 
    result = r.json()
    return result