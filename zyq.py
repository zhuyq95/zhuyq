# -*- coding: utf-8 -*-
all_price=10000                    #现在银行里面存的现金
buy_price=0
add_suuccess=1
mima=12345
goods=[{"name":"豪车","price": 1000},{"name":"房子","price": 2000},{"name":"老婆","price": 1500},{"name":"儿子","price": 1100},{"name":"女儿","price": 1200},{"name":"孙子","price": 1300}]
car=[]
get_price=input("取现：")         #取出现金，出去购物
if get_price>all_price:
    print("先生您好：您的余额不足!")
else:
    print "取现成功！\n","余额：%d"%(all_price-get_price)
    print("当前商品")
    for i in goods:
        print i["name"] ,i["price"]
    while 1 :
        choose_goods=raw_input("请选择：")
        if choose_goods=="查看购物车" or choose_goods=="结算" :########查看购物车
            print "名称", "单价"
            if len(car)==0:
                print "无", "无"
            else:
                for j in car:
                     print j["name"],j["price"]
            if  choose_goods=="结算" :
                print "总价"
                for m in car:
                    buy_price+=m["price"]
                print buy_price
                check=raw_input("确认结算（yes/no）")
                if check == "yes" :
                    if buy_price<get_price:
                        if mima == input("请输入您的密码："):
                            print "购买成功\n","支付金额：%d"%buy_price,"剩余金额：%d"%(get_price-buy_price)
                            break
                        else:
                            print("密码不正确！")
                    else:
                        print"余额不足，请您取现后再购买！"
                else :
                    print("输入格式不正确，麻烦您重新结算！")
                buy_price = 0
        elif choose_goods=="取现":
            print "余额：%d"%(all_price-get_price)
            get_price=get_price+input("请输入取现金额")
            if get_price > all_price:
                print("先生您好：您的余额不足!")
            else:
                print "取现成功！\n","余额：%d\n"% (all_price - get_price),"已取现:%d"%get_price
        else:                           #########添加商品
            for x in goods:
                if choose_goods==x["name"]:
                    add_suuccess=1      #########添加成功
                    break
                else:
                    add_suuccess=0
            if  add_suuccess==1 :
                print("恭喜您，“%s”已加入购物车"%choose_goods)
                for k in goods :
                    shangpin = {}
                    if choose_goods==k["name"]:
                        shangpin.update(k)
                        car.append(shangpin)
            else:
                print("抱歉，我们不提供“%s”商品"%choose_goods)