"""
当前模块主要用于对服务器在接收到数据后对接收的返回数据设定
"""
import demjson
import time
def build_reply(result,user_name=""):
    """
    将返回的结果转换为JSON格式
    :param result:
    :param timestamp:
    :return: str
    """
    return demjson.encode({"result":result,"user_name":user_name,"timestamp":time.time()})

Reply_LoginSucceed = build_reply("login_succeed")
Reply_LoginError = build_reply("login_error")
Reply_RegError = build_reply("reg_error")
Reply_RegSucceed = build_reply("reg_succeed")
Reply_TypeError = build_reply("type_error")
