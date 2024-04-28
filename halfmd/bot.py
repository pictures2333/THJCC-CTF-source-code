from selenium import webdriver
from time import sleep

wb = webdriver.Chrome()
sleep(5)

PASS = "FAKE_PASS"
HIDDEN = "FAKE_HIDDEN"

url=f"http://23.146.248.36:10009/{HIDDEN}?pass={PASS}"
wb.get(url)

while True:
        try: wb.get(url)
        except: pass
        sleep(20)

# ADMIN BOT 真跡
# 很爛更暴力