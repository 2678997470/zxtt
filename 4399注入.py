import requests
import hashlib

GameUserName = input("请输入账号：")  # 游戏 账号
GamePassWord = input("请输入密码：")  # 游戏 密码
print('获取uid中')
uid= requests.get("http://cz.4399.com/get_role_info.php?ac=cuid&uname=" + GameUserName)
uid = uid.text
print(uid)
# -----------------------------获取cookies------------------
molianps: dict[str, str] = dict(loginFrom="uframe",
                                layoutSelfAdapting="true",
                                layout="vertical",
                                mainDivId="embed_login_div",
                                includeFcmInfo="false",
                                level="0",
                                regLevel="0",
                                password=GamePassWord,
                                username=GameUserName)
print(molianps)
drpost = requests.post("https://ptlogin.4399.com/ptlogin/login.do?v=1", data=molianps)
print(drpost.text)
print(drpost.cookies)
print("4399游戏存档获取 调用了requests库 与hashlib 接口源萌新 技术指导萌新")
for i in range(210000000):
    pd = input('是否更换账号  y or n')
    if "y" == pd:
        GameUserName = input("请输入账号：")  # 游戏 账号
        GamePassWord = input("请输入密码：")  # 游戏 密码
        print('获取uid中')
        # -----------------------------获取uid------------------
        uid: Response = requests.get("http://cz.4399.com/get_role_info.php?ac=cuid&uname=" + GameUserName)
        uid = uid.text
        print(uid)
        # -----------------------------获取cookies------------------
        molianps: dict[str, str] = dict(loginFrom="uframe",
                                        layoutSelfAdapting="true",
                                        layout="vertical",
                                        mainDivId="embed_login_div",
                                        includeFcmInfo="false",
                                        level="0",
                                        regLevel="0",
                                        password=GamePassWord,
                                        username=GameUserName)
        print(molianps)
        drpost = requests.post("https://ptlogin.4399.com/ptlogin/login.do?v=1", data=molianps)
        print(drpost.text)
        print(drpost.cookies)
    print(
        "西游大战僵尸2：21366’\r\n’超合金战记3：18385’\r\n’西游战记3：26403’\r\n’武将风云录1：29249’\r\n’武将风云录2：31999’\r\n’武将风云录3：49278’\r\n’爆枪英雄1：27788’\r\n’爆枪英雄2：51229’\r\n’西游灭妖传：41191’\r\n’造梦西游3:15389’\r\n’造梦西游2:：11634’\r\n’造梦西游1:10418’\r\n’萌战前线：54881’\r\n’火线风暴：28337’\r\n’机甲小子：25235’\r\n’机甲小子2:41113’\r\n’彩虹王国：22580’\r\n’梦幻三国：15899’\r\n’三国小镇：14728’\r\n’勇士的信仰：16523’\r\n’国王的勇士5:38964国王的勇士6：51855’\r\n’快打僵尸：49245’\r\n’魔城奇兵：40523’\r\n’封神太:1：16364’\r\n’封神太子2：19596’\r\n’封神太子外传2：25039’\r\n’伟大航线：19296’\r\n’造梦江湖1：23042’\r\n’造梦江湖2:21992")
    gameid = "1000" + input("请输入游戏id")
    date = input("请输入存档data：")
    title = input("请输入存档标题（数字和英文）：")
    # ---------------------gamekey获取------------------------------------------
    gamekey = gameid + "LPislKLodlLKKOSNlSDOAADLKADJAOADALAklsd" + gameid
    ssr = gamekey
    # 创建md5对象
    hl = hashlib.md5()  # 第一次加密
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()  # 第二次加密
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    gamekey = hl.hexdigest()  # 4     1            16     12
    print(gamekey[4:20])
    gamekey = gamekey[4:20]  # daac   c3127a8e0c278090  8e4ea2e76184         5, 16
    for i in range(9):
        # print(i)
        index = str(i)
        print("游戏id" + gameid + "游戏存档位置" + index)
        # ---------------------生成verify------------------------------------------
        verify = "SDALPlsldlnSLWPElsdslSE" + index + gamekey + date + title + uid + gameid + "PKslsO"
        ssr = verify
        # 创建md5对象
        hl = hashlib.md5()  # 第一次加密
        hl.update(ssr.encode("utf-8"))
        ssr = hl.hexdigest()  # 第二次加密
        hl = hashlib.md5()
        hl.update(ssr.encode("utf-8"))
        ssr = hl.hexdigest()  # 第3次加密
        hl = hashlib.md5()
        hl.update(ssr.encode("utf-8"))
        verify = hl.hexdigest()
        # ------------------------------获取session------------------------------------
        jbbl = "SDALPlsldlnSLWPElsdslSE" + gamekey + uid + gameid + "PKslsO"
        ssr = jbbl
        # 创建md5对象
        hl = hashlib.md5()  # 第一次加密
        hl.update(ssr.encode("utf-8"))
        ssr = hl.hexdigest()  # 第二次加密
        hl = hashlib.md5()
        hl.update(ssr.encode("utf-8"))
        ssr = hl.hexdigest()  # 第3次加密
        hl = hashlib.md5()
        hl.update(ssr.encode("utf-8"))
        jbbl = hl.hexdigest()
        molianps = {
            "uid": uid,
            "gameid": gameid,
            "gamekey": gamekey,
            "verify": jbbl
        }
        session = "https://save.api.4399.com/?ac=get_session"
        session = requests.post(session, molianps)
        print("这里是session："+session.text)
        # ------------------存档注入----------------------------
        data = {
            'session': '',  # 会话ID
            'gamekey': gamekey,  # 游戏密钥
            'verify': verify,  # 验证码
            'data': date,
            'gameid': gameid,  # 游戏ID
            'token': '',  # 令牌
            'title': title,  # 标题
            'refer': 'https://sda.4399.com/4399swf/upload_swf/ftp7/hanbao/20120107/6/y3v3710.htm',  # 引用链接
            'index': index,  # 索引
            'uid': uid  # 用户ID
        }
        print(data)
        zr = requests.post("https://save.api.4399.com/?ac=save", data=data, cookies=drpost.cookies)
        print(zr.text)
