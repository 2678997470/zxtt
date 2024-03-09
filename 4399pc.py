import tkinter as tk
import requests
import hashlib

def save_game():
    # 获取用户输入的数据
    GameUserName = username_entry.get()
    GamePassWord = password_entry.get()
    gameid = "1000" + gameid_entry.get()
    date = data_entry.get()
    title = title_entry.get()
    index = index_entry.get()

    # 在这里添加你的存档注入代码
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
    drpost = requests.post("https://ptlogin.4399.com/ptlogin/login.do?v=1", data=molianps)

    # -----------------------------获取uid------------------
    uid = requests.get("http://cz.4399.com/get_role_info.php?ac=cuid&uname=" + GameUserName)
    uid = uid.text

    # ---------------------gamekey获取------------------------------------------
    gamekey = gameid + "LPislKLodlLKKOSNlSDOAADLKADJAOADALAklsd" + gameid
    ssr = gamekey
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    gamekey = hl.hexdigest()
    print(gamekey[4:20])
    gamekey = gamekey[4:20]

    print("游戏id" + gameid + "游戏存档位置" + index)

    # ---------------------生成verify------------------------------------------
    verify = "SDALPlsldlnSLWPElsdslSE" + index + gamekey + date + title + uid + gameid + "PKslsO"
    ssr = verify
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    verify = hl.hexdigest()

    # ------------------------------获取session------------------------------------
    jbbl = "SDALPlsldlnSLWPElsdslSE" + gamekey + uid + gameid + "PKslsO"
    ssr = jbbl
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()
    hl = hashlib.md5()
    hl.update(ssr.encode("utf-8"))
    ssr = hl.hexdigest()
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
    print("这里是session：" + session.text)

    # ------------------存档注入----------------------------
    data = {
        'session': '',
        'gamekey': gamekey,
        'verify': verify,
        'data': date,
        'gameid': gameid,
        'token': '',
        'title': title,
        'refer': 'https://sda.4399.com/4399swf/upload_swf/ftp7/hanbao/20120107/6/y3v3710.htm',
        'index': index,
        'uid': uid
    }
    print(data)
    zr = requests.post("https://save.api.4399.com/?ac=save", data=data, cookies=drpost.cookies)
    print(zr.text)
    result_label.config(text=zr.text)  # 更新标签的内容

    # ...





# 创建窗口
window = tk.Tk()

# 创建编辑框和标签
username_label = tk.Label(window, text="账号：")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="密码：")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

gameid_label = tk.Label(window, text="游戏ID：")
gameid_label.pack()
gameid_entry = tk.Entry(window)
gameid_entry.pack()

data_label = tk.Label(window, text="存档data：")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

title_label = tk.Label(window, text="存档标题：")
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

index_label = tk.Label(window, text="存档位置：")
index_label.pack()
index_entry = tk.Entry(window)
index_entry.pack()
# 创建标签
result_label = tk.Label(window, text="")
result_label.pack()
# 创建按钮
save_button = tk.Button(window, text="保存", command=save_game)
save_button.pack()

# 运行窗口
window.mainloop()
