# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
# 报告里关闭截图
#ST.SAVE_IMAGE = False
auto_setup(__file__)
#干员列表
ganYuanLieBiao = {
        '无时装山':{'干员名称': Template(r"山-名字.png", threshold=0.7999999999999999, record_pos=(-0.024, 0.143), resolution=(1440, 810)),'干员头像':Template(r"山-头像.png", threshold=0.8, record_pos=(-0.197, -0.174), resolution=(1440, 810)),'干员助战卡片':Template(r"无皮肤山-助战卡片.png", threshold=0.8, record_pos=(-0.134, 0.005), resolution=(1440, 810)),'干员技能':True},
        '乌云皮肤山':{'干员名称': Template(r"山-名字.png", threshold=0.7999999999999999, record_pos=(-0.089, 0.063), resolution=(2376, 1152)),'干员头像':Template(r"皮肤山-头像.png", threshold=0.8, record_pos=(-0.217, -0.019), resolution=(1440, 810)),'干员助战卡片':Template(r"皮肤山-助战卡片.png", threshold=0.8, record_pos=(-0.025, 0.003), resolution=(1440, 810)),'干员技能':True},
        '乌云皮肤山':{'干员名称': Template(r"山-名字.png", threshold=0.7999999999999999, record_pos=(-0.089, 0.063), resolution=(2376, 1152)),'干员头像':Template(r"tpl1664417843817.png", threshold=0.8, record_pos=(0.067, -0.135), resolution=(1440, 810)),'干员助战卡片':Template(r"tpl1664417766707.png", threshold=0.8, record_pos=(-0.13, 0.035), resolution=(1440, 810)),'干员技能':True},
        '羽毛笔':{'干员名称': Template(r"羽毛笔-名字.png", threshold=0.8, record_pos=(0.431, 0.143), resolution=(1440, 810)),'干员头像':Template(r"羽毛笔-头像.png", threshold=0.7499999999999999, record_pos=(-0.171, -0.12), resolution=(1440, 810)),'干员助战卡片':Template(r"羽毛笔-助战卡片.png", threshold=0.7499999999999999, record_pos=(0.191, 0.015), resolution=(1440, 810)),'干员技能':False},
        '音律皮肤煌':{'干员名称':Template(r"煌-名字.png", threshold=0.8500000000000001, record_pos=(-0.003, 0.076), resolution=(1440, 810)),'干员头像':Template(r"音律皮肤煌-头像.png", threshold=0.8, record_pos=(0.062, -0.11), resolution=(1440, 810)),'干员助战卡片':Template(r"音律皮肤煌-助战卡片.png", record_pos=(0.301, 0.032), resolution=(1440, 810)),'干员技能':True},
        '欢乐喜锯人':{'干员名称':Template(r"煌-名字.png", threshold=0.8500000000000001, record_pos=(-0.003, 0.076), resolution=(1440, 810)),'干员头像':Template(r"tpl1664418663749.png", threshold=0.8, record_pos=(0.049, -0.119), resolution=(1440, 810)),'干员助战卡片':Template(r"tpl1664418646538.png", threshold=0.8, record_pos=(0.321, 0.037), resolution=(1440, 810)),'干员技能':True},
        '梓兰':{'干员名称': Template(r"梓兰-名字.png", record_pos=(0.003, -0.031), resolution=(1440, 810)),'干员头像':Template(r"梓兰-头像.png", threshold=0.8, record_pos=(0.062, -0.14), resolution=(1440, 810)),'干员助战卡片':None,'干员技能':False},
        '安塞尔':{'干员名称': Template(r"安塞尔-名字.png", record_pos=(0.01, -0.031), resolution=(1440, 810)),'干员头像':Template(r"安塞尔-头像.png", threshold=0.8, record_pos=(0.069, -0.107), resolution=(1440, 810)),'干员助战卡片':None,'干员技能':False}  
    }
#关卡名称列表
guanQiaMingCheng={
        '作战' : Template(r"敌方情报.png", threshold=0.8500000000000001, record_pos=(0.283, -0.003), resolution=(1440, 810)),
        '射手部队':Template(r"射手部队.png", threshold=0.9000000000000001, record_pos=(0.287, -0.123), resolution=(1440, 810)),
        '共生':Template(r"共生.png", threshold=0.9000000000000001, record_pos=(0.287, -0.123), resolution=(1440, 810)),
        '蓄水池':Template(r"蓄水池.png", threshold=0.9000000000000001, record_pos=(0.287, -0.123), resolution=(1440, 810)),
        '虫群横行':Template(r"虫群横行.png", threshold=0.9000000000000001, record_pos=(0.287, -0.123), resolution=(1440, 810)),
        '商店' : Template(r"商店.png", threshold=0.9000000000000001, record_pos=(0.247, -0.144), resolution=(1440, 810)) ,
        '不期而遇': Template(r"不期而遇.png", threshold=0.9000000000000001, record_pos=(0.247, -0.144), resolution=(1440, 810)) ,
        '地区委托': Template(r"地区委托.png", threshold=0.9000000000000001, record_pos=(0.247, -0.145), resolution=(1440, 810)) ,
    }
#战斗关卡列表
guanQiaLieBiao ={
        #0、1、2是第n个放置的干员，放置坐标是拖动干员时画面偏移后需要放置的坐标位置，拖动坐标是干员的朝向，点击坐标是干员在正常画面中放置的坐标位置。
        '射手部队':{0:{'放置坐标':(1150,330),'拖动坐标':(1150,720),'点击坐标':(1070,360)},
                1:{'放置坐标':(1030,330),'拖动坐标':(1030,720),'点击坐标':None},
                2:{'放置坐标':(930,440),'拖动坐标':(1300,440),'点击坐标':None}}, 
        '共生':{0:{'放置坐标':(820,455),'拖动坐标':(820,100),'点击坐标':(720,460)},
                1:{'放置坐标':(930,430),'拖动坐标':(630,430),'点击坐标':None},
                2:{'放置坐标':(1050,430),'拖动坐标':(650,430),'点击坐标':None}}, 
        '蓄水池':{0:{'放置坐标':(1070,500),'拖动坐标':(770,500),'点击坐标':(990,540)},
               1:{'放置坐标':(1060,380),'拖动坐标':(1060,600),'点击坐标':None}, 
               2:{'放置坐标':(1040,290),'拖动坐标':(1040,600),'点击坐标':None}}, 
        '虫群横行':{0:{'放置坐标':(1050,440),'拖动坐标':(1050,700),'点击坐标':(970,460)},
                1:{'放置坐标':(925,340),'拖动坐标':(925,700),'点击坐标':None},
                2:{'放置坐标':(1200,540),'拖动坐标':(800,560),'点击坐标':None}}, 
}
#招募干员开局从左到右的顺序，第一个请务必是主力干员。
zhaoMu=['无时装山','梓兰','安塞尔']
#关卡可能在的坐标
guanQiaZuoBiao=[(880,370),(880,280),(880,210),(880,440),(880,510)]
#初始招募近卫券所在坐标（从左到右三张初始券）
zhaoMuQuanZuoBiao=[(390,600),(700,600),(1040,600)]
#如果自己有干员就写True，没有干员就写False。选True，即使没有干员也不会有问题，还是会助战找。
xunZhao = True
#商店是否想要离开到第二层，False是不去第二层，True是去第二层（对于部分人想多拿少许经验的配置）
liKaiSD = False
#选择分队（0是突击作战分队，1是指挥分队）
fenDui = 1
#战斗后是否取物品(true取物品，False不取物品)
quWuPin = True
'''------------↑↑↑这里有些可以自己设置的选项↑↑↑------------''' 
#判断是否存在图片，有就返回图片坐标，没就返回NoneF
def tryPanDuan(img):
    try:
        result=wait(img,timeout=1)
        return(result)
    except:
        return 
    return
#随便弄了一个1秒内尝试点击一个图片，没有找到图片就不点击，且不会因报错而停止的函数。
def tryTouch(img):
    try:
        touch(wait(img,timeout=1))
    except:
        pass
    return
#滑动屏幕
def huaPing():
    swipe((1100,400),(200,400),duration=2)
    sleep(1)
    return
#点击开始探索的按钮
def kaiShiTanSuo():
    while not exists(Template(r"开始探索.png", threshold=0.9000000000000001, record_pos=(0.405, 0.191), resolution=(1440, 810))):
        touch((690,40))
    sleep(1.0)
    touch(Template(r"开始探索.png", threshold=0.9000000000000001, record_pos=(0.405, 0.191), resolution=(1440, 810)))
    sleep(1.0)
    return
#选择分队
def xuanZeFenDui(fenDui):
    if(fenDui==0):
        while not exists(Template(r"突击作战分队.png", threshold=0.9000000000000001, record_pos=(0.203, 0.063), resolution=(1440, 810))):
    #精二高级的山比较稳定过关，所以选了这个分队'''
            huaPing()
        else:
            touch(Template(r"突击作战分队.png", threshold=0.9000000000000001, record_pos=(0.203, 0.063), resolution=(1440, 810)))
    #有需要的就把这两个突击战术分队的图片换成自己想要的分队吧，用左侧Airtest辅助窗里的功能就可以截图生成自己的代码了。'''
            sleep(1.0)
            touch(Template(r"黄色勾勾.png", threshold=0.85, record_pos=(0.287, 0.182), resolution=(1440, 810)))
        return
    elif(fenDui==1):
        touch(Template(r"指挥分队.png", threshold=0.8500000000000001, record_pos=(0.299, 0.08), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"蓝色确认键.png", record_pos=(0.299, 0.178), resolution=(1440, 810)))
        return
#选择招募组合
def xuanZeZuHe():
    touch(Template(r"取长补短.png", threshold=0.8, record_pos=(0.11, 0.081), resolution=(1440, 810)))
    touch(Template(r"蓝色确认键.png", record_pos=(0.299, 0.178), resolution=(1440, 810)))
    return
#招募脚本选择的干员(干员名称，头像，是否向右滑寻找，干员助战的卡片)
def zhaoMuGanYuan(mingcheng,touxiang,xunzhao,zhuzhankapian):
    #查找次数
    chazhaocishu =0
    while not exists(mingcheng):#
        if xunzhao == True:
            if  chazhaocishu < 2:
                huaPing()
                chazhaocishu+=1
                continue
            else:
                xunzhao = False
        else:
            touch(Template(r"选择助战.png", threshold=0.85, record_pos=(0.374, -0.257), resolution=(1440, 810)))
            while not exists(zhuzhankapian):
                touch((1300,30))
                sleep(4)
            else:
                touch(zhuzhankapian)
            sleep(1.0)
            touch(Template(r"招募助战.png", threshold=0.85, record_pos=(0.169, 0.125), resolution=(1440, 810)))
            sleep(2.0)
            break
    else:
        touch(mingcheng)
        sleep(1.0)
        touch((1250,750))
        sleep(3.0)
    while not exists(touxiang):#判断画面是否在那个招到了干员的画面。
        sleep(1.0)
    else:
        sleep(3.0)
    touch((700,730))#上面判断到了在那个画面再点击一下屏幕进入下一步。
    sleep(1.0)
    return
#放弃招募干员
def fangQiZhaoMu():
    touch(Template(r"放弃.png", threshold=0.9000000000000001, record_pos=(0.277, 0.247), resolution=(1440, 810)))
    sleep(1.0)
    touch(Template(r"放弃招募勾勾.png", threshold=0.9000000000000001, record_pos=(0.157, 0.106), resolution=(1440, 810)))
    return
#选择初始招募
def xuanZeZhaoMu(zhaoMuZuoBiao):
    tryPanDuan(Template(r"招募券.png", threshold=0.85, record_pos=(-0.226, 0.145), resolution=(1440, 810)))
    for i in range(3):
        touch(zhaoMuQuanZuoBiao[i])
        zhaoMuGanYuan(ganYuanLieBiao[zhaoMu[i]]['干员名称'],ganYuanLieBiao[zhaoMu[i]]['干员头像'],xunZhao,ganYuanLieBiao[zhaoMu[i]]['干员助战卡片'] )
    return
#进入古堡
def jinRu():
    touch(Template(r"探索海洋.png", threshold=0.8, record_pos=(0.44, -0.007), resolution=(1440, 810)))
    sleep(8)
    return
#编队
def bianDui():
    touch(Template(r"编队.png", threshold=0.85, record_pos=(0.359, 0.262), resolution=(1440, 810)))
    sleep(1.0)
    if tryPanDuan(ganYuanLieBiao[zhaoMu[0]]['干员名称'])!=None:#判断行动选干员界面有没有山
        pass#有就pass不管
    else:
        touch(Template(r"快捷编队.png", threshold=0.85, record_pos=(0.285, -0.251), resolution=(1440, 810)))#没有就执行这段选山和选择技能。
        for i in zhaoMu[::-1]:
            touch(ganYuanLieBiao[i]['干员名称'])
            sleep(1.0)
        if ganYuanLieBiao[zhaoMu[0]]['干员技能'] ==True:            
            touch((200,600))
            sleep(1.0)
        else:
            pass
        touch(Template(r"编队确认.png", threshold=0.85, record_pos=(0.424, 0.247), resolution=(1440, 810)))
    sleep(2)
    touch(Template(r"编队返回按钮.png", threshold=0.85, record_pos=(-0.464, -0.254), resolution=(1440, 810)))
    return
#判断关卡，函数返回相应名称。
def panDuanGuanQia():
    jieguo = '无判断'
    while jieguo == '无判断':
        if tryPanDuan(guanQiaMingCheng['作战'])!=None:
            if tryPanDuan(guanQiaMingCheng['射手部队'])!=None:
                jieguo='射手部队'
                break
            elif tryPanDuan(guanQiaMingCheng['共生'])!=None:
                jieguo='共生'
                break
            elif tryPanDuan(guanQiaMingCheng['蓄水池'])!=None:
                jieguo='蓄水池'
                break
            elif tryPanDuan(guanQiaMingCheng['虫群横行'])!=None:
                jieguo='虫群横行'
                break
        else:
            if tryPanDuan(guanQiaMingCheng['商店'])!=None:
                jieguo='商店'
                break
            elif tryPanDuan(guanQiaMingCheng['不期而遇'])!=None:
                jieguo='事件'
                break
            elif tryPanDuan(guanQiaMingCheng['地区委托'])!=None:
                jieguo='委托'
                break
            else:
                jieguo='无判断'
    return (jieguo)
#进入战斗的编队页面
def chuFa():
    touch(Template(r"出发前往.png", threshold=0.85, record_pos=(0.388, 0.112), resolution=(1440, 810)))
    sleep(1.5)
    return
#战斗（干员头像，干员技能，放置坐标，拖动坐标，点击坐标）
def zhanDou():
    touch(Template(r"开始行动.png", record_pos=(0.322, 0.242), resolution=(1440, 810)))
    sleep(0.5)
    tryTouch(Template(r"tpl1664426422826.png", threshold=0.8, record_pos=(0.249, 0.104), resolution=(1440, 810)))
    while not exists(Template(r"目标生命.png", threshold=0.9000000000000001, record_pos=(0.044, -0.258), resolution=(1440, 810))):
        sleep(1)  
    sleep(2)
    touch(Template(r"倍速按钮.png", threshold=0.9000000000000001, record_pos=(0.362, -0.25), resolution=(1440, 810)))
    sleep(7)
    for i in range(3):
        zuobiao=tryPanDuan(ganYuanLieBiao[zhaoMu[i]]['干员头像'])
        swipe(zuobiao,guanQiaLieBiao[jieguo][i]['放置坐标'],duration=1)#拖干员到位置
        sleep(1)
        swipe(guanQiaLieBiao[jieguo][i]['放置坐标'],guanQiaLieBiao[jieguo][i]['拖动坐标'],duration=1)#设置朝向
        sleep(5)
        if ganYuanLieBiao[zhaoMu[i]]['干员技能'] == True:
            touch(guanQiaLieBiao[jieguo][i]['点击坐标'])#点击干员
            sleep(2.0)
            touch((950,460))#开技能
            sleep(1.0)
            touch((260,100))
        else:
            pass
        sleep(3)
    return
    
#判断关卡结果
def guanQiaJieGuo():
    Final = False
    while not exists(Template(r"成功通过.png", threshold=0.85, record_pos=(-0.366, 0.15), resolution=(1440, 810))):#判断过关
        sleep(4.0)#没有成功通过就等4秒，然后继续循环找成功通过
        if exists(Template(r"联系中断.png", threshold=0.8, record_pos=(-0.008, -0.003), resolution=(1440, 810))):
            touch(Template(r"联系中断.png", threshold=0.8, record_pos=(-0.008, -0.003), resolution=(1440, 810)))
            Final = True
            return(Final)
        else:
            pass          
    else:
        sleep(2.0)#找到了之后，为了防止在“成功通关”这四个字从画面左边飞到画面内的瞬间识别到并立刻进行点击而设置的一个等待时间。（因为计算机执行速度非常快。）
    touch((1000,490))#识别到了点击一下
    sleep(1.0)
    if quWuPin == True:
        if tryPanDuan(Template(r"tpl1664422094967.png", threshold=0.8500000000000001, record_pos=(-0.376, -0.001), resolution=(1440, 810)))!=None:
            touch(Template(r"tpl1664422115818.png", threshold=0.8500000000000001, record_pos=(-0.375, 0.129), resolution=(1440, 810)))
        else:
            pass
        sleep(1.5)
        if tryPanDuan(Template(r"取藏品.png", threshold=0.8500000000000001, record_pos=(-0.156, 0.128), resolution=(1440, 810)))!=None:
            touch(Template(r"取藏品.png", threshold=0.8500000000000001, record_pos=(-0.156, 0.128), resolution=(1440, 810)))
        else:
            pass
        sleep(1.5)
    else:
        pass
    while not exists(Template(r"不要了走了.png", threshold=0.85, record_pos=(0.296, 0.07), resolution=(1440, 810))):#判断有没有这个图片
        swipe((670,500),vector=[-0.3,0])#判断没有，就自右往左滑动屏幕，移到右边，移完回去继续判断图片
    else:
        touch(Template(r"不要了走了.png", threshold=0.85, record_pos=(0.296, 0.07), resolution=(1440, 810)))#判断到了就点它
    sleep(1.0)
    touch(Template(r"关卡结算红色勾勾.png", threshold=0.8, record_pos=(0.122, 0.149), resolution=(1440, 810)))
    sleep(1.5)
    return(Final)
#事件处理
def shiJian():
    touch(Template(r"出发前往.png", record_pos=(0.395, 0.096), resolution=(1440, 810)))
    sleep(4.0)
    touch((1190,406))#这个点击的坐标可以在只有一个或两个选项的时候点击到最下面选项的位置。
    sleep(3.0)
    if tryPanDuan(Template(r"事件离开按钮.png", threshold=0.8500000000000001, record_pos=(0.435, 0.194), resolution=(1440, 810)))!=None:
        touch(Template(r"事件离开按钮.png", threshold=0.8500000000000001, record_pos=(0.435, 0.194), resolution=(1440, 810)))
    elif tryPanDuan(Template(r"事件按钮1.png", record_pos=(0.433, 0.169), resolution=(1440, 810)))!=None:
        touch(Template(r"事件按钮1.png", record_pos=(0.433, 0.169), resolution=(1440, 810)))
    elif tryPanDuan(Template(r"事件按钮2.png", threshold=0.8, record_pos=(0.433, 0.104), resolution=(1440, 810)))!=None:
        touch(Template(r"事件按钮2.png", threshold=0.8, record_pos=(0.433, 0.104), resolution=(1440, 810)))
    elif tryPanDuan(Template(r"事件按钮3.png", threshold=0.8, record_pos=(0.433, -0.052), resolution=(1440, 810)))!=None:
        touch(Template(r"事件按钮3.png", threshold=0.8, record_pos=(0.433, -0.052), resolution=(1440, 810)))
    else:
        touch((1190,406))
    sleep(2.0)
    tryTouch(Template(r"事件确认按钮.png", record_pos=(0.435, 0.103), resolution=(1440, 810)))
    sleep(2.5)
    tryTouch(Template(r"骰子白勾.png", threshold=0.85, record_pos=(-0.004, 0.23), resolution=(1440, 810)))
    sleep(1.0)
    if exists(Template(r"黑色确认键.png", threshold=0.8, record_pos=(0.435, 0.071), resolution=(1440, 810))):
        sleep(1)
        touch(Template(r"黑色确认键.png", record_pos=(0.0, 0.232), resolution=(1440, 810)))
    else:
        pass
    if exists(Template(r"结局走向变化确认键.png", record_pos=(0.003, 0.091), resolution=(1440, 810))):
        touch(Template(r"结局走向变化确认键.png", threshold=0.8, record_pos=(0.435, 0.071), resolution=(1440, 810)))
    else:
        pass
    return
def weiTuo():
    touch(Template(r"出发前往.png", record_pos=(0.395, 0.096), resolution=(1440, 810)))
    sleep(4.0)
    touch((1190,406))#这个点击的坐标可以在只有一个或两个选项的时候点击到最下面选项的位置。
    sleep(3.0)
    if tryPanDuan(Template(r"事件离开按钮.png", threshold=0.8500000000000001, record_pos=(0.435, 0.194), resolution=(1440, 810)))!=None:#这里是针对不期而遇里有三个选项的情况进行确认。
        touch(Template(r"事件离开按钮.png", threshold=0.8500000000000001, record_pos=(0.435, 0.194), resolution=(1440, 810)))
    else:
        touch((1190,406))
    sleep(2.0)
    tryTouch(Template(r"确定这么做.png", threshold=0.85, record_pos=(0.432, 0.18), resolution=(1440, 810)))
    sleep(2)
    tryTouch(Template(r"事件确认按钮.png", record_pos=(0.435, 0.103), resolution=(1440, 810)))
    sleep(1)
    if exists(Template(r"黑色确认键.png", threshold=0.8, record_pos=(0.435, 0.071), resolution=(1440, 810))):
        sleep(1)
        touch(Template(r"黑色确认键.png", record_pos=(0.0, 0.232), resolution=(1440, 810)))
    else:
        pass
    sleep(3)
    return
#离开商店
def liKaiShanDian():
    if tryPanDuan(Template(r"算了.png", threshold=0.85, record_pos=(-0.013, 0.103), resolution=(1440, 810)))!=None:
        for i in range(2):
            touch(Template(r"算了.png", threshold=0.85, record_pos=(-0.013, 0.103), resolution=(1440, 810)))
            sleep(1.5)
    else:
        pass
    likai = exists(Template(r"离开.png", threshold=0.85, record_pos=(0.453, 0.145), resolution=(1440, 810)))
    for i in range(2):
        touch(likai)
        sleep(1.5)
    sleep(1)
    touch(Template(r"tpl1664374000851.png", threshold=0.8500000000000001, record_pos=(-0.003, 0.231), resolution=(1440, 810)))
    sleep(1.0)
    return
#商店
def shanDian():
    Final = False
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    #初始化_投资次数
    touzicishu=0
    if exists(Template(r"前瞻性投资系统.png", threshold=0.9000000000000001, record_pos=(-0.103, -0.19), resolution=(1440, 810))):
        touch(Template(r"前瞻性投资系统.png", threshold=0.9000000000000001, record_pos=(-0.103, -0.19), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"投资入口.png", threshold=0.85, record_pos=(-0.074, -0.037), resolution=(1440, 810)))
        sleep(1.0)
        while touzicishu<5:#为解决投完了身上的源石锭还没到投资受限的情况而设置的判断（运气好试过几次17颗源石锭投完了还能继续投就卡住了的情况。）
            if tryPanDuan(Template(r"投资受限.png", threshold=0.9000000000000001, record_pos=(0.113, -0.04), resolution=(1440, 810)))==None:
                touch((1100,560),times=30)
                touzicishu+=1
            else:
                sleep(1.0)
                break
        else:
            Final = True
    else:
        pass
    sleep(1.0)
    Final = True
    if liKaiSD == True:
        liKaiShanDian()
    else:
        pass
    return(Final)

#点击关卡可能的位置
def dianJiGuanQia():
    sleep(1.0)
    for i in guanQiaZuoBiao:
        touch(i)
        sleep(0.2)
    if tryPanDuan(Template(r"不期而遇小字.png", threshold=0.9000000000000001, record_pos=(-0.133, 0.053), resolution=(1440, 810)))!=None:
        touch(Template(r"不期而遇小字.png", threshold=0.9000000000000001, record_pos=(-0.133, 0.053), resolution=(1440, 810)))
        sleep(1)
    else:
        pass
    if tryPanDuan(Template(r"地区委托小字.png", threshold=0.8500000000000001, record_pos=(-0.135, 0.053), resolution=(1440, 810)))!=None:
        touch(Template(r"地区委托小字.png", threshold=0.8500000000000001, record_pos=(-0.135, 0.053), resolution=(1440, 810)))
        sleep(1)
    else:
        pass
    return
#退出探索
def tuiChu():
    touch((45,30))
    sleep(1.0)
    #第二次探索如果卡主，可以适当将这里的sleep时间增加一点，比如sleep(3.0)，sleep可以理解为等待一段时间的意思
    touch(Template(r"放弃本次探索.png", record_pos=(0.406, -0.013), resolution=(1440, 810)))
    sleep(1.0)
    #这个对象likai()里的这些sleep时间都可以适当改一下，改到适合自己模拟器运行加载速度的等待时间
    touch(Template(r"红色勾勾.png", threshold=0.85, record_pos=(0.159, 0.106), resolution=(1440, 810)))
    sleep(1.0)
    return
#处理结算页面，返回主页面
def fanHui():
    wait(Template(r"查看数据回溯.png", threshold=0.9,record_pos=(-0.374, -0.249), resolution=(1440, 810)))
    touch((700,720))#等一段时间点击画面进入下一个结算的界面
    sleep(1.0)
    touch((700,720))#等一段时间点击画面进入下一个结算的界面
    sleep(2.0)
    tryTouch(Template(r"生态谱系.png", threshold=0.9, record_pos=(0.01, 0.019), resolution=(1440, 810)))
    tryTouch(Template(r"解锁.png", threshold=0.9, record_pos=(0.003, -0.203), resolution=(1440, 810)))
    tryTouch(Template(r"√.png",threshold=0.8, record_pos=(-0.001, 0.189), resolution=(1440, 810)))
    tryTouch(Template(r"进行中的本月委托.png", threshold=0.9, record_pos=(0.001, -0.204), resolution=(1440, 810)))
    sleep(1.0)
    while not exists(Template(r"开始探索.png", threshold=0.9, record_pos=(0.405, 0.191), resolution=(1440, 810))):
        touch((700,720))
    return

if __name__ == "__main__":
    #开始运行
    while(True):
        #不要动↓
        Final = False
        kaiShiTanSuo()
        xuanZeFenDui(fenDui)
        xuanZeZuHe()
        xuanZeZhaoMu(zhaoMuQuanZuoBiao)
        jinRu()
        bianDui()
        sleep(1.0)
        touch(((440,370)))
        sleep(2)
        while Final != True:
            dianJiGuanQia()
            jieguo = panDuanGuanQia()
            if jieguo == '事件':
                shiJian()
            elif jieguo == '委托':
                weiTuo()
            elif jieguo == '商店':
                Final = shanDian()
            else:                
                chuFa()
                zhanDou()
                Final = guanQiaJieGuo()
        else:
            if exists(Template(r"退出按钮.png", threshold=0.8500000000000001, record_pos=(-0.464, -0.256), resolution=(1440, 810))):
                tuiChu()
            else:
                pass
            fanHui()
            continue
#Template(r"tpl1664377147344.png", record_pos=(0.433, 0.014), resolution=(1440, 810)),备用图片截图
