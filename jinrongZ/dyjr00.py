from jinrongZ.huobigupiao import huobi,gp



list1 = ["sh000001", "sz000917", "sz002649", "sz300692", "sh600705", "sh600611","sh600150",  "sh601066", ]
list2=["btcusdt","ethusdt","eosusdt","bchusdt","xrpusdt","htusdt","cmtusdt","paiusdt"]
#CW当周 NW次周 CQ季度
dmlist=["BTC_CW","BTC_NW","XRP_CQ"]
bj=0.2997

huobi.usdt()
huobi.hb(list2)
# huobi.hbdm(dmlist,bj)
gp.gupiao(list1)

