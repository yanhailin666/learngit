from jinrongZ.huobigupiao import huobi,gp
import time

list1 = ["sh000001","sz000917","sz002649","sh600705","sh600611","sh600150","sz000063","sz000561","sh601555","sz002475","sh601066","sz000839"]
list2=["btcusdt","ethusdt","eosusdt","bchusdt","xrpusdt","htusdt","cmtusdt","paiusdt"]
#CW当周 NW次周 CQ季度
dmlist=["BTC_CW","BTC_NW","XRP_CQ"]
bj=0.2997


i=13
if i==1:
    while True:
        gp.gupiao(list1)
        time.sleep(6)

elif i==2:
    huobi.usdt()
    huobi.hb(list2)

elif i==3:
    gp.gupiao(list1)

else:
    huobi.usdt()
    huobi.hb(list2)
    gp.gupiao(list