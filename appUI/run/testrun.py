import uiautomator2 as u2
import time
from Resources import params as p
#d = u2.connect('192.168.1.225') #华为手机
d = u2.connect('192.168.1.200') #华为新手机
#d = u2.connect('192.168.1.240') #平板
#d = u2.connect('192.168.1.152') #周凯
d.press("power")  #电源键
time.sleep(1)
d.swipe(0.518, 0.799 ,0.518, 0.185,steps=15) #滑动解锁
d(text="微信").click()
time.sleep(2)
#d.xpath('//android.widget.FrameLayout[3]').click()
d.swipe(0.669, 0.127,0.669, 0.882 ,steps=15)
time.sleep(1.5)
d(text="找劳保网").click()
time.sleep(1.5)
d.xpath('//*[@resource-id="com.tencent.mm:id/nc"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()#我的
time.sleep(1.5)
print(d.xpath('//android.webkit.WebView/android.view.View[1]/android.widget.Button[3]/android.view.View[2]').get_text())

time.sleep(1.5)


# time.sleep(3)
# d.press("back")
# time.sleep(1)
# d.press('home')
