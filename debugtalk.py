import json
import logging
import random
import time
import requests
from typing import List
import pymysql

test_host = "rm-bp1orqjl80dle29ur878.mysql.rds.aliyuncs.com"
test_user = "test_all"
test_password = "HJklEw832BnghcRsjoWQpsxsDsj23"

staging_host = "rm-bp1va24i42upn6l22.mysql.rds.aliyuncs.com"
staging_user = "staging_all"
staging_password = "tE6JnVoplLGJVD32JMB2Jgcc"

avatar_url_list = ["https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_01.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_02.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_03.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_04.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_05.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_06.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_07.jpg",
                   "https://cdn-community.codemao.cn/community_frontend/community_default_avatar/avatar_300x300_08.jpg"
                   ]


def time_sleep():
    time.sleep(0.1)


def return_random_string(type_code):
    """
    随机返回一个字段名做断言,  get  accounts/接口 专用
    :return: 一个字段
    """
    list01 = ["id", "bcmid", "phone_number", "nickname", "fullname", "username", "birthday", "remark",
              "avatar_url", "sex", "qq", "description", "product_id", "grade", "grade_desc", "gold", "created_at",
              "close", "robotBasics", "programmingBasics", "operatingSystem", "parentalExpectation",
              "parentalExpectationInput"]
    list02 = ["id", "username", "phone_number"]
    list03 = ["javax.validation.ConstraintViolationException", "Param-Invalid@Common", "size must be between 1 and 500"]
    if type_code == 1:
        return random.choice(list01)
    elif type_code == 2:
        return random.choice(list02)
    elif type_code == 3:
        return ""
    elif type_code == 4:
        return random.choice(list03)


#  post  accounts/接口 专用
def return_random_phone_number(type_code):
    if type_code == 1:
        return "188" + str(random.randint(10000000, 99999999))
    elif type_code == 2:
        return ""
    elif type_code == 3:
        return "13037375544"


def return_random_email(type_code):
    if type_code == 1:
        return str(random.randint(1000000000000, 9999999999999)) + "@qaq.com"
    elif type_code == 2:
        return ""
    elif type_code == 3:
        return "1583492267@qq.com"


def return_random_nickname(type_code):
    if type_code == 1:
        return str(random.randint(10000000, 99999999)) + "nickname"
    elif type_code == 2:
        return "1997"
    elif type_code == 3:
        return "1⚐⚑⚆⚇⚈⚉"


def return_random_string_2(type_code):
    if type_code == 1:
        return "id"
    elif type_code == 2:
        return "手机号已注册"
    elif type_code == 3:
        return "邮箱已被注册"
    elif type_code == 4:
        return "已存在相同的昵称"
    elif type_code == 5:
        return "㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㍢㍣㍤㍥㍦㍧㍨㍩㍪㍫"
    elif type_code == 6:
        return "size must be between 1 and 10"


# post_accounts 专用
def setup_hook_dispose(request):
    if request["req_json"]["password"] == "":
        del request["req_json"]["password"]
    elif request["req_json"]["email"] == "":
        del request["req_json"]["email"]
    elif request["req_json"]["phone_number"] == "":
        del request["req_json"]["phone_number"]
    return request


# /accounts/{id}/basic_auth
# 获取主账号信息 专用
def return_random_string_3(type_code):
    """
    随机返回一个字段名做断言, 获取主账号信息 接口 专用
    :return: 一个字段
    """
    if type_code == 1:
        list02 = ["id", "username", "email", "phone_number", "has_password"]
        return random.choice(list02)
    elif type_code == 2:
        return "用户不存在"


def return_random_string_4(type_code):
    """
    随机返回一个字段名做断言, 获取主账号信息 接口 专用
    :return: 一个字段
    """
    if type_code == 1:
        return random.choice(["id", "gold", "age", "grade", "level"])
    elif type_code == 2:
        return ""
    elif type_code == 3:
        return "id"


def put_accounts():
    list01 = []
    # 只修改age
    age = random.randint(1, 100)
    data_1 = {"num": 1, "name": "修改age", "fields": {"age": age}, "status_code": 204, "value": age}
    list01.append(data_1)

    # 修改头像
    avatar_url = random.choice(avatar_url_list)
    data_2 = {"num": 2, "name": "修改头像", "fields": {"avatar_url": avatar_url}, "status_code": 204,
              "value": avatar_url}
    list01.append(data_2)

    # 修改生日
    birthday = random.randint(1501245133, 1701245133)
    data_3 = {"num": 3, "name": "修改生日", "fields": {"birthday": birthday}, "status_code": 204,
              "value": birthday}
    list01.append(data_3)

    # 修改description
    description = random.randint(1, 88888888)
    data_4 = {"num": 4, "name": "修改description", "fields": {"description": description}, "status_code": 204,
              "value": description}
    list01.append(data_4)

    # 修改 doing
    doing = "test" + str(random.random())
    data_5 = {"num": 5, "name": "修改 doing", "fields": {"doing": doing}, "status_code": 204, "value": doing}
    list01.append(data_5)

    # 修改邮箱
    email = "qinwang" + str(random.randint(10000, 99999)) + "@qwq.com"
    data_6 = {"num": 6, "name": "修改邮箱", "fields": {"email": email}, "status_code": 204, "value": email}
    list01.append(data_6)

    # 修改familiar_sprite
    familiar_sprite = random.randint(1, 100)
    data_7 = {"num": 7, "name": "修改 familiar_sprite", "fields": {"familiar_sprite": familiar_sprite},
              "status_code": 204, "value": familiar_sprite}
    list01.append(data_7)

    # 修改fullname
    fullname_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    random.shuffle(fullname_list)
    fullname = "".join(fullname_list)
    data_8 = {"num": 8, "name": "修改 fullname", "fields": {"fullname": fullname}, "status_code": 204,
              "value": fullname}
    list01.append(data_8)

    # 修改年级
    grade = random.randint(1, 16)
    data_9 = {"num": 9, "name": "修改年级", "fields": {"grade": grade}, "status_code": 204, "value": grade}
    list01.append(data_9)

    # 修改mlz_name
    mlz_name = "test" + str(random.randint(100, 999))
    data_10 = {"num": 10, "name": "修改 mlz_name", "fields": {"mlz_name": mlz_name}, "status_code": 204,
               "value": mlz_name}
    list01.append(data_10)

    # 修改nickname
    nickname = "qw" + str(random.randint(1000, 9999))
    data_11 = {"num": 11, "name": "修改 nickname", "fields": {"nickname": nickname}, "status_code": 204,
               "value": nickname}
    list01.append(data_11)

    # 修改operatingSystem
    operating_system = random.randint(0, 3)
    data_12 = {"num": 12, "name": "修改 operatingSystem", "fields": {"operatingSystem": [operating_system]},
               "status_code": 204, "value": operating_system}
    list01.append(data_12)

    # 修改parentalExpectation
    parental_expectation = random.randint(0, 11)
    data_13 = {"num": 13, "name": "修改 parentalExpectation 家长期望",
               "fields": {"parentalExpectation": [parental_expectation]},
               "status_code": 204, "value": parental_expectation}
    list01.append(data_13)

    # 修改parental_expectation_input
    parental_expectation_input = "我期望" + str(random.randint(100, 999))
    data_14 = {"num": 14, "name": "修改 parental_expectation_input",
               "fields": {"parentalExpectationInput": parental_expectation_input},
               "status_code": 204, "value": parental_expectation_input}
    list01.append(data_14)

    # 修改password 为a123456789
    password = "a123456789"
    data_15 = {"num": 15, "name": "修改 password为a123456789", "fields": {"password": password}, "status_code": 204,
               "value": "65a0ec385ca6a0c1e20d1f8270c28303"}
    list01.append(data_15)

    # 修改password 回 123456
    password = "123456"
    data_16 = {"num": 16, "name": "修改 password为 123456", "fields": {"password": password}, "status_code": 204,
               "value": "e10adc3949ba59abbe56e057f20f883e"}
    list01.append(data_16)

    # 修改手机号  为18866686667
    phone_number = "18866686667"
    data_17 = {"num": 17, "name": "修改 phone_number 为18866686667", "fields": {"phone_number": phone_number},
               "status_code": 204, "value": "902f064fe19ff65e2f362c8b89b509e9cc203991f74133289fbbe9e7f589c010"
               }
    list01.append(data_17)

    # 修改手机号回 18866686666
    phone_number = "18866686666"
    data_18 = {"num": 18, "name": "修改 phone_number 为18866686666", "fields": {"phone_number": phone_number},
               "status_code": 204, "value": "2a46dc5d109493a395d75b40fefb9e8a40e3ff549beaa19a8c031c21413e14c1"}
    list01.append(data_18)

    # 修改pid
    # pid = random.choice(["account"])

    # 修改preview_work_id
    preview_work_id = random.randint(1, 100)
    data_19 = {"num": 19, "name": "修改 preview_work_id", "fields": {"preview_work_id": preview_work_id},
               "status_code": 204, "value": preview_work_id}
    list01.append(data_19)

    # 修改programmingBasics
    programming_basics = random.randint(1, 10)
    data_20 = {"num": 20, "name": "修改 programmingBasics", "fields": {"programmingBasics": programming_basics},
               "status_code": 204, "value": programming_basics}
    list01.append(data_20)

    # 修改QQ
    qq = random.randint(100000000, 999999999)
    data_21 = {"num": 21, "name": "修改 QQ", "fields": {"qq": qq}, "status_code": 204, "value": qq}
    list01.append(data_21)

    # 修改备注remark
    remark = "test_qin_wang" + str(random.randint(100, 999))
    data_22 = {"num": 22, "name": "修改备注", "fields": {"remark": remark}, "status_code": 204, "value": remark}
    list01.append(data_22)

    # 修改robotBasics
    robot_basics = random.randint(1, 10)
    data_23 = {"num": 23, "name": "修改 robotBasics", "fields": {"robotBasics": robot_basics},
               "status_code": 204, "value": robot_basics}
    list01.append(data_23)

    # 修改sex 性别
    sex = random.randint(0, 1)
    data_24 = {"num": 24, "name": "修改 sex", "fields": {"sex": sex}, "status_code": 204, "value": sex}
    list01.append(data_24)

    # 修改username
    username = "test_qin_wang" + str(random.randint(100, 999))
    data_25 = {"num": 25, "name": "修改 username", "fields": {"username": username}, "status_code": 204,
               "value": username}
    list01.append(data_25)

    return list01


def update_accounts_put(request, fields):
    # 把变量fields 的值，付给请求body
    request["req_json"] = fields
    return request


def select_mysql_date(num, user_id):
    if user_id == "1676888367":
        db = connect_to_mysql(test_host, test_user, test_password)
    elif user_id == "1203646479":
        db = connect_to_mysql(staging_host, staging_user, staging_password)

    if num == 1:
        sql = f"select age from user_extension where user_id = {user_id}"
    elif num == 2:
        sql = f"select avatar_url from user where id = {user_id}"
    elif num == 3:
        sql = f"select birthday from user where id = {user_id}"
    elif num == 4:
        sql = f"select description from user where id = {user_id}"
    elif num == 5:
        sql = f"select doing from user_extension where user_id = {user_id}"
    elif num == 6:
        sql = f"select email from basic_auth where user_id = {user_id}"
    elif num == 7:
        sql = f"select familiar_sprite from user_extension where user_id = {user_id}"
    elif num == 8:
        sql = f"select fullname from user where id = {user_id}"
    elif num == 9:
        sql = f"select grade from user where id = {user_id}"
    elif num == 10:
        sql = f"select mlz_name from user_extension where user_id = {user_id}"
    elif num == 11:
        sql = f"select nickname from user where id = {user_id}"
    elif num == 12:
        sql = f"select operating_system from user where id =  {user_id}"
    elif num == 13:
        sql = f"select parental_expectation  from user where id= {user_id}"
    elif num == 14:
        sql = f"select parental_expectation_input from user where id = {user_id}"
    elif num == 15:
        sql = f"select password from basic_auth where user_id = {user_id}"
    elif num == 16:
        sql = f"select password from basic_auth where user_id = {user_id}"
    elif num == 17:
        sql = f"select hashed_phone_number from basic_auth where user_id = {user_id}"
    elif num == 18:
        sql = f"select hashed_phone_number from basic_auth where user_id = {user_id}"
    elif num == 19:
        sql = f"select preview_work_id from user_extension where user_id = {user_id}"
    elif num == 20:
        sql = f"select programming_basics from user where id = {user_id}"
    elif num == 21:
        sql = f"select qq from user where id = {user_id}"
    elif num == 22:
        sql = f"select remark from user where id = {user_id}"
    elif num == 23:
        sql = f"select robot_basics from user where id = {user_id}"
    elif num == 24:
        sql = f"select sex from user where id = {user_id}"
    elif num == 25:
        sql = f"select username from basic_auth where user_id = {user_id}"
    return start_sql(sql, db)


def connect_to_mysql(host, username, password):
    """
    Connects to a MySQL database and returns a connection object.
    """
    try:
        # Change the parameters below to match your MySQL database configuration
        db = pymysql.connect(host=host,
                             port=3306,
                             user=username,
                             password=password,
                             database="account",
                             charset="utf8"
                             )
        print("Connected to MySQL!")
        return db.cursor()
    except pymysql.connect.Error as error:
        print("Failed to connect to MySQL database:", error)
        return None


def start_sql(sql, db):
    try:
        db.execute(sql)
        data = db.fetchone()[0]
        db.close()
        return data
    except Exception as e:
        print(e)


def update_patch_accounts_username(request, code, base_url):
    if code == 1:
        return request
    elif code == 2:
        json_data = {"phone_number": return_phone(), "pid": "account"}
        data = requests.post(url=base_url + "/accounts", json=json_data)
        print(data.json())
        user_id = data.json()["id"]

        request["req_json"] = {"username": "username" + str(random.randint(10000, 99999))}
        request["url"] = base_url + f"/accounts/{user_id}/username"
        print(request)

        return request


def delete_phone(code, base_url):
    if code == 1:
        phone_number = return_phone()
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        password = 123456789
        user_id = register_account(base_url=base_url, phone_number=phone_number, email=email, password=password)
        return user_id
    elif code == 2:
        # 用户未设置用户名
        phone_number = return_phone()
        password = 123456789
        user_id = register_account(base_url=base_url, phone_number=phone_number, password=password)
        return user_id
    elif code == 3:
        # 解绑手机号-用户设置了用户名，没有设置密码
        phone_number = return_phone()
        user_id = register_account(base_url=base_url, phone_number=phone_number)
        # 去设置下用户名
        username_data = {"username": "username" + str(random.randint(10000, 99999))}
        requests.patch(url=base_url + "/accounts/" + str(user_id) + "/username", json=username_data)
        return user_id
    elif code == 4:
        # 解绑手机号-用户设置了邮箱，没有设置了密码
        phone_number = return_phone()
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        user_id = register_account(base_url=base_url, phone_number=phone_number, email=email)
        return user_id


def delete_email(code, base_url):
    if code == 1:
        # 用户只设置了手机号
        phone_number = return_phone()
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        user_id = register_account(base_url=base_url, phone_number=phone_number, email=email)
        return user_id
    elif code == 2:
        # 用户设置了用户名密码
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        password = "123456789"
        user_id = register_account(base_url=base_url, password=password, email=email)
        # 去设置下用户名
        username_data = {"username": "username" + str(random.randint(10000, 99999))}
        requests.patch(url=base_url + "/accounts/" + str(user_id) + "/username", json=username_data)
        return user_id
    elif code == 3:
        # 用户设置了用户名没有设置密码
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        user_id = register_account(base_url=base_url, email=email)
        # 去设置下用户名
        username_data = {"username": "username" + str(random.randint(10000, 99999))}
        requests.patch(url=base_url + "/accounts/" + str(user_id) + "/username", json=username_data)
        return user_id
    elif code == 4:
        # 用户没有手机号或者用户名密码
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        user_id = register_account(base_url=base_url, email=email)
        return user_id
    elif code == 5:
        # 用户没有设置邮箱
        phone_number = return_phone()
        user_id = register_account(base_url=base_url, phone_number=phone_number)

        return user_id


def register_account(base_url=None, phone_number=None, email=None, password=None, pid=None):
    """
    通用注册方法
    :return: 返回用户ID
    """
    json_data = {}
    if base_url is None:
        return "URL IS NONE"
    if phone_number is not None:
        json_data["phone_number"] = phone_number
    if email is not None:
        json_data["email"] = email
    if password is not None:
        json_data["password"] = password
    if pid is None:
        json_data["pid"] = "account"
    headers = {
        "Connection": "close",
    }
    url = base_url + "/accounts"
    data = requests.post(url=url, json=json_data, headers=headers)
    time.sleep(1)
    return data.json()["id"]


def account_auth_check(request, code, url):
    """
    账号登录校验接口
    """
    if code == 1:
        # 输入正确手机号密码
        phone_number = return_phone()
        password = 123456
        # 注册账号
        register_account(base_url=url, phone_number=phone_number, password=password)
        time.sleep(1)
        request["req_json"] = {"identity": phone_number, "password": password}
        return request
    elif code == 2:
        # 输入正确邮箱密码
        email = str(random.randint(1000000000, 9999999999)) + "@qq.com"
        password = 123456
        register_account(base_url=url, email=email, password=password)
        time.sleep(1)
        request["req_json"] = {"identity": email, "password": password}
        return request
    elif code == 3:
        # 输入正确用户名密码
        phone_number = return_phone()
        password = 123456
        # 注册账号
        user_id = register_account(base_url=url, phone_number=phone_number, password=password)
        # 设置用户名
        username_data = {"username": "username" + str(random.randint(10000, 99999))}
        requests.patch(url=url + "/accounts/" + str(user_id) + "/username", json=username_data)
        time.sleep(1)
        request["req_json"] = {"identity": username_data["username"], "password": password}
        return request
    elif code == 4:
        # 用户不存在
        request["req_json"] = {"identity": "187777585858888", "password": "123456"}
        return request
    elif code == 5:
        # 输入错误密码
        request["req_json"] = {"identity": "13037375544", "password": "1234567k89"}
        return request
    elif code == 6:
        # identity传空
        request["req_json"] = {"identity": "", "password": "123456789"}
        return request
    elif code == 7:
        # 密码传空
        request["req_json"] = {"identity": "13037375544", "password": ""}
        return request


def account_batch(request, code):
    data = {"pid": "account", "prefix": "qinwangtest",
            "users": [{"fullname": "string", "password": "123456", "phoneNumber": "13037375544", "qq": "123456"}]}
    if code == 1:
        data["pid"] = "eewewe"
    elif code == 2:
        data["pid"] = ""
    elif code == 3:
        data["prefix"] = ""
    elif code == 4:
        data["prefix"] = "4554487"
    elif code == 6:
        data["users"][0]["fullname"] = "54545"
    elif code == 7:
        data["users"][0]["phoneNumber"] = ""
    elif code == 8:
        data["users"][0]["phoneNumber"] = "dfsfdsfdssf"
    elif code == 9:
        data["users"][0]["password"] = ""
    elif code == 10:
        data["users"][0]["password"] = "12345"
    elif code == 11:
        data["users"][0]["password"] = "123jjjjjjjjjjjjjj1jjj"
    elif code == 12:
        phone_number = "170" + str(random.randint(10000000, 99999999))
        data["users"][0]["phoneNumber"] = phone_number
    elif code == 13:
        data["users"][0]["phoneNumber"] = return_phone()
        data["users"].append({"fullname": "string", "password": "123456",
                              "phoneNumber": return_phone(),
                              "qq": "123456"})
    request["req_json"] = data
    return request


def account_batch_register(request, code):
    data = {"pid": "account",
            "users": [{"username": "string", "password": "123456"}]}
    if code == 1:
        data["pid"] = "eewewe"
    elif code == 2:
        data["pid"] = ""
    elif code == 3:
        data["users"][0]["password"] = ""
    elif code == 4:
        data["users"][0]["password"] = "123"
    elif code == 5:
        data["users"][0]["password"] = "123456789451237894444123456789451237894444123456789451237894444"
    elif code == 6:
        data["users"][0]["username"] = ""
    elif code == 7:
        data["users"][0]["username"] = "343434"
    elif code == 8:
        data["users"][0]["username"] = "qinwang1997"
    elif code == 9:
        data["users"].append({"password": "123456", "username": "41414"})
    elif code == 10:
        data["users"][0]["username"] = "qinw" + str(random.randint(10000, 99999))
    elif code == 11:
        data["users"][0]["username"] = "qinw" + str(random.randint(10000, 99999))
        data["users"].append({"password": "123456", "username": "qinw" + str(random.randint(10000, 99999))})
    elif code == 12:
        del data["pid"]
    request["req_json"] = data
    return request


def account_batch_register_phone(request, code):
    data = {"pid": "account",
            "users": [{"phone_number": "13037375544"}]}
    if code == 1:
        data["pid"] = "eewewe"
    elif code == 2:
        data["pid"] = ""
    elif code == 3:
        data["users"][0]["phone_number"] = ""
    elif code == 4:
        data["users"][0]["phone_number"] = "4jk"
    elif code == 5:
        data["users"][0]["phone_number"] = return_phone()
    elif code == 6:
        data["users"][0]["phone_number"] = return_phone()
        data["users"].append({"phone_number": return_phone()})
        data["users"].append({"phone_number": return_phone()})
    request["req_json"] = data
    return request


def return_phone():
    # 返回一个随机手机号
    return random.choice(
        ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
         "155", "156", "157", "158", "159", "182", "183", "184", "187", "188", "189", "177", "178", "170", "171",
         "172", "173", "174", "175", "176", "147", "148", "149", "150", "151", "152", "153", "155", "156", "157"]) \
           + str(random.randint(10000000, 99999999))


def return_email():
    # 返回一个随机邮箱
    return str(random.randint(1000000000, 9999999999)) + "@qin.com"


def account_batch_search(request, code):
    data = {"fields": [], "target_type": "phone_number", "target_values": []}
    if code == 1:
        data["fields"].append("idsds")
    elif code == 2:
        data["fields"].append("phone_number")
        data["target_values"].append("13037375544")
    elif code == 3:
        data["fields"] = ["id", "bcmid", "nickname", "sex", "username", "email", "phone_number",
                          "birthday", "avatar_url", "fullname", "qq", "description", "familiar_sprite",
                          "doing", "mlz_name", "level", "preview_work_id", "grade", "grade_desc",
                          "user_id", "gold", "age", "product_id", "created_at", "close", "robotBasics",
                          "programmingBasics", "operatingSystem", "parentalExpectation",
                          "parentalExpectationInput"]
        data["target_values"].append("13037375544")
    elif code == 4:
        del data["fields"]
        data["target_values"].append("13037375544")
    # elif code == 5:
    #     data["target_type"] = "test"
    elif code == 6:
        del data["target_values"]
    elif code == 7:
        data["target_type"] = "id"
        data["target_values"].append(10000)
    elif code == 8:
        data["target_type"] = "id"
        data["target_values"].append(10000)
        data["target_values"].append(10001)
    elif code == 9:
        data["target_type"] = "id"
        data["target_values"].append(100)
    elif code == 10:
        data["target_type"] = "fullname"
        data["target_values"].append("秦旺")
    elif code == 11:
        data["target_type"] = "fullname"
        data["target_values"].append("秦旺")
        data["target_values"].append("qinwang")
    elif code == 12:
        data["target_type"] = "fullname"
        data["target_values"].append("劈商漏")
    elif code == 13:
        data["target_values"].append("13037375544")
    elif code == 14:
        data["target_values"].append("13037375544")
        data["target_values"].append("17877781769")
    elif code == 15:
        data["target_values"].append("130")
    elif code == 16:
        data["target_type"] = "email"
        data["target_values"].append("1583492267@qq.com")
    elif code == 17:
        data["target_type"] = "email"
        data["target_values"].append("1583492267@qq.com")
        data["target_values"].append("123456@qq.com")
    elif code == 18:
        data["target_type"] = "email"
        data["target_values"].append("1a@qewewwq.com")
    elif code == 19:
        data["target_type"] = "username"
        data["target_values"].append("qinwang123")
    elif code == 20:
        data["target_type"] = "username"
        data["target_values"].append("qinwang123")
        data["target_values"].append("qinwang")
    elif code == 21:
        data["target_type"] = "username"
        data["target_values"].append("lpo587juh54d")
    request["req_json"] = data
    return request


def phone_single_id(request, url, code):
    if code == 1:
        request["url"] = request["url"] + "100"
    elif code == 2:
        print(request)
        email = "lkj" + str(random.randint(1000000, 9999999)) + "@qq.com"
        user_id = register_account(base_url=url, email=email)
        request["url"] = request["url"] + str(user_id)
    elif code == 3:
        phone = return_phone()
        user_id = register_account(base_url=url, phone_number=phone)
        request["url"] = request["url"] + str(user_id)
    return request


def phone_batch(request, url, code):
    data = {"userIds": []}
    if code == 4:
        data["userIds"].append(100)
    elif code == 1:
        phone = return_phone()
        user_id = register_account(base_url=url, phone_number=phone)
        data["userIds"].append(user_id)
    elif code == 2:
        phone = return_phone()
        user_id_1 = register_account(base_url=url, phone_number=phone)
        phone = return_phone()
        user_id_2 = register_account(base_url=url, phone_number=phone)
        data["userIds"].append(user_id_1)
        data["userIds"].append(user_id_2)
    elif code == 3:
        email = "lkj" + str(random.randint(1000000, 9999999)) + "@qq.com"
        user_id = register_account(base_url=url, email=email)
        data["userIds"].append(user_id)
    print(data)
    request["req_json"] = data
    return request


def black_list(url, code):
    if code == 1:
        phone = return_phone()
        register_account(base_url=url, phone_number=phone)
        print(phone)
        return phone
    elif code == 2:
        phone = return_phone()
        user_id = register_account(base_url=url, phone_number=phone)
        username = "qin" + str(random.randint(10000, 99999))
        requests.patch(url=url + "/accounts/" + str(user_id) + "/username",
                       json={"username": username, "pid": "account"})
        print(username)
        return username
    elif code == 3:
        email = "jul" + str(random.randint(1000000, 9999999)) + "@qq.com"
        register_account(base_url=url, email=email)
        print(email)
        return email


def captcha(request, url, phone_number):
    requests_url = url + "/accounts/captcha/search"
    if phone_number in [14996857401, 14996857403, 14996857405, "qinwang@codemao.cn"]:
        data = requests.get(url=requests_url, params={"phone_number": phone_number})
        captcha_number = data.json()["items"][0]["captcha"]
        print(captcha_number)
        request["req_json"]["captcha"] = captcha_number
        return request
    else:
        request["req_json"]["captcha"] = "123456"
        return request


def accounts_information_search(request, code):
    data_dict = {"page": 1, "limit": 10}
    if code == 1:
        data_dict["userId"] = "10000"
    elif code == 2:
        data_dict["userId"] = "100"
    elif code == 3:
        data_dict["productId"] = "1"
    elif code == 4:
        data_dict["dateStart"] = 1700422906
        data_dict["dateEnd"] = 1701422906
    elif code == 5:
        data_dict["phoneNumber"] = "13037375544"
    elif code == 6:
        data_dict["phoneNumber"] = "14337375544"
    elif code == 7:
        data_dict["phoneNumber"] = "1303737sds"
    elif code == 8:
        data_dict["close"] = "0"
    elif code == 9:
        data_dict["close"] = "1"
    elif code == 10:
        data_dict["close"] = "2"
    elif code == 11:
        data_dict["accountType"] = "0"
    elif code == 12:
        data_dict["accountType"] = "1"
    request["req_json"] = data_dict
    return request


def accounts_list_search(request, code):
    data_dict = {"page": 1, "per_page": 1,
                 "fields": ["id", "bcmid", "nickname", "sex", "username", "email", "phone_number",
                            "birthday", "avatar_url", "fullname", "qq", "description", "created_at", "close",
                            "robotBasics", "programmingBasics", "operatingSystem", "parentalExpectation",
                            "parentalExpectationInput"
                            ]}
    if code == 1:
        data_dict["id"] = 10000
    elif code == 2:
        data_dict["id"] = 100
    elif code == 3:
        data_dict["fullname"] = "秦旺"
    elif code == 4:
        data_dict["phone_number"] = "13037375544"
    elif code == 5:
        data_dict["phone_number"] = "1583484457"
    elif code == 6:
        data_dict["nickname"] = "秦旺"
    elif code == 7:
        data_dict["id"] = 10000
        data_dict["fields"] = ["id"]
    request["req_json"] = data_dict
    return request


def accounts_password_setting(request, url, code):
    data = {"password": "123456", "user_id": 10000}
    if code == 1:
        data["user_id"] = 100
    elif code == 2:
        data["password"] = "123"
    elif code == 3:
        data["password"] = "123456123456123456123456123456123456"
    elif code == 4:
        user_id = register_account(base_url=url, phone_number=return_phone(), password="123456")
        data["user_id"] = user_id
    elif code == 5:
        user_id = register_account(base_url=url, phone_number=return_phone())
        data["user_id"] = user_id
    request["req_json"] = data
    return request


def accounts_password(url):
    return register_account(base_url=url, phone_number=return_phone(), password="123456")


def accounts_register(request, code):
    data_dict = {"identity_type": 1, "identity": "", "fullname": "christ", "pid": "account"}
    if code == 1:
        data_dict["pid"] = "aaa"
    elif code == 2:
        data_dict["pid"] = ""
    elif code == 3:
        data_dict["fullname"] = "123ds"
    elif code == 4:
        data_dict["identity_type"] = 0
    elif code == 5:
        data_dict["identity"] = return_phone()
    elif code == 6:
        data_dict["identity_type"] = 2
        data_dict["identity"] = return_email()
    elif code == 7:
        data_dict["identity"] = "13037375544"
    elif code == 8:
        data_dict["identity_type"] = 2
        data_dict["identity"] = "1583492267@qq.com"
    request["req_json"] = data_dict
    return request


def accounts_search(request, code):
    data_dict = {
        "fields": ["id", "email", "phone_number", "bcmid", "username", "nickname", "avatar_url", "fullname", "qq"]}
    if code == 1:
        data_dict["id"] = 10000
    elif code == 2:
        data_dict["id"] = 100
    elif code == 3:
        data_dict["email"] = "1583492267@qq.com"
    elif code == 4:
        data_dict["phone_number"] = "13037375544"
    elif code == 5:
        data_dict["phone_number"] = "14259858888"
    elif code == 6:
        data_dict["qq"] = "123456"
    elif code == 7:
        data_dict["username"] = "qinwang1997"
    elif code == 8:
        data_dict["identity"] = "1583492267@qq.com"
    elif code == 9:
        data_dict["identity"] = "13037375544"
    elif code == 10:
        data_dict["identity"] = "qinwang1997"
    elif code == 11:
        data_dict["phone_number"] = "13037375544"
        data_dict["qq"] = "123456"
    elif code == 12:
        data_dict["fields"] = ["id", "email", "phone_number"]
        data_dict["phone_number"] = "13037375544"
    elif code == 13:
        data_dict["fields"] = []
        data_dict["email"] = "1583492267@qq.com"

    request["req_json"] = data_dict
    return request


def accounts_oauth(request, code, url):
    data_dict = {
        "oauth_type": "WECHAT",
        "registerMode": 0,
        "unionid": "unionid" + str(random.randint(10000000000, 99999999999)),
        "openid": "openid" + str(random.randint(10000000000, 99999999999)),
        "appid": "wx4b18624114d6fb7c",
        "pid": "account"
    }
    if code == 1:
        print(data_dict)
    elif code == 2:
        data_dict["phone_number"] = return_phone()
        data_dict["password"] = "123456"
    elif code == 3:
        phone_number = return_phone()
        register_account(base_url=url, phone_number=phone_number)
        data_dict["phone_number"] = phone_number
    elif code == 4:
        data_dict["phone_number"] = 13037375544
        data_dict["password"] = "123456"
    elif code == 5:
        data_dict["appid"] = "qchenisdsds"
    elif code == 6:
        data_dict["registerMode"] = 21
    elif code == 7:
        data_dict[
            "wechat_extra"] = """{\"nickname\":\"微信用户\",\"avatar_url\":\"https://abc\",\"sex\":\"0\",\"country\":\"\",\"province\":\"\",\"city\":\"\"}"""
    request["req_json"] = data_dict
    return request


def accounts_oauth_unionId(url):
    data_dict = {
        "oauth_type": "WECHAT",
        "registerMode": 0,
        "unionid": "unionid" + str(random.randint(10000000000, 99999999999)),
        "openid": "openid" + str(random.randint(10000000000, 99999999999)),
        "appid": "wx4b18624114d6fb7c",
        "pid": "account"
    }
    requests.post(url=url + "/accounts/oauth", json=data_dict)
    time.sleep(1)
    return data_dict["unionid"]


# --------------------------------------------------------------------------------------------------------------------
# API 层方法


def accounts_api_ticket(url):
    if "test-api" in url:
        openserver_url = "https://test-open-service.codemao.cn/captcha/rule/v3"
        pid = "qinwang"
    elif "backend" in url:
        openserver_url = "https://staging-open-service.codemao.cn/captcha/rule/v3"
        pid = "qinwang"
    else:
        openserver_url = "https://open-service.codemao.cn/captcha/rule/v3"
        pid = "onLlA4EB"
    data = requests.post(url=openserver_url, json={"identity": "14266669999", "pid": pid})
    print(data.json())
    return data.json()["ticket"]


def accounts_phone_login(request, code, url):
    # 14252526363 该手机为自动化注册手机号
    data_dict = {"phone_number": 14252526363, "captcha": "", "pid": "account"}
    if code == 1:
        # 先获取发送验证码接口的 ticket
        ticket = accounts_api_ticket(url)
        # 请求发送验证码接口
        request_data = requests.post(url=url + "/tiger/v3/app/accounts/captcha/login",
                                     headers={"X-Captcha-Ticket": ticket},
                                     json={"phone_number": "14252526363"})
        if request_data.status_code == 204:
            print("验证码发送正确")
        else:
            print("验证码发送失败")
            print(request.json())
        data_dict["captcha"] = "555555"
    elif code == 2:
        # 查询发送的验证码
        time.sleep(1)
        # 去查询正确验证码
        data_dict["captcha"] = get_captcha_method(url, 14252526363)
    elif code == 3:
        data_dict["captcha"] = get_captcha_method(url, 14252526363)
    elif code == 5:
        data_dict["captcha"] = "555555"
        data_dict["phone_number"] = "13037375544"

    request["req_json"] = data_dict
    return request


def get_captcha_method(url, phone_number):
    if "test-api" in url:
        internal_user_id = 4012
        request_1 = requests.post(
            url="https://test-api-gateway.codemao.cn/internal-account-service/accounts/auth/token",
            headers={"Authorization": "Basic YWRtaW46YWRtaW4="},
            json={"id": internal_user_id, "authorities": ["account"]})
        internal_token = request_1.json()["token"]
        request_2 = requests.post(
            url="https://test-cloud-gateway.codemao.cn/platform-it-manage-admin-service/accounts/captcha/search",
            headers={"Cookie": f"test_internal_account_token={internal_token}"},
            json={"phoneNumber": phone_number, "pageIndex": 1, "pageSize": 1})

        phone_captcha = request_2.json()["data"]["items"][0]["captcha"]

    elif "backend" in url:
        internal_user_id = 14714
        request_1 = requests.post(
            url="https://staging-api-gateway.codemao.cn/internal-account-service/accounts/auth/token",
            headers={"Authorization": "Basic YWRtaW46YWRtaW44ODg5OTk="},
            json={"id": internal_user_id, "authorities": ["account"]})
        internal_token = request_1.json()["token"]
        request_2 = requests.post(
            url="https://staging-cloud-gateway.codemao.cn/platform-it-manage-admin-service/accounts/captcha/search",
            headers={"Cookie": f"staging_internal_account_token={internal_token}"},
            json={"phoneNumber": phone_number, "pageIndex": 1, "pageSize": 1})

        phone_captcha = request_2.json()["data"]["items"][0]["captcha"]

    else:
        internal_user_id = 16626
        request_1 = requests.post(
            url="https://api-gateway.codemao.cn/internal-account-service/accounts/auth/token",
            headers={"Authorization": "Basic aW5mcmFzdHJ1Y3R1cmVfZ3JvdXA6OWM3N2QyODRlOWEzODVlY2NiYmM5NmYyYmE5NjA0ZWU="},
            json={"id": internal_user_id, "authorities": ["account"]})
        internal_token = request_1.json()["token"]
        request_2 = requests.post(
            url="https://cloud-gateway.codemao.cn/platform-it-manage-admin-service/accounts/captcha/search",
            headers={"Cookie": f"internal_account_token={internal_token}"},
            json={"phoneNumber": phone_number, "pageIndex": 1, "pageSize": 1})
        phone_captcha = request_2.json()["data"]["items"][0]["captcha"]
    print(phone_captcha)
    return phone_captcha


def accounts_phone_login_post_process(request, code, url):
    # 14252526364 手机为自动化注册手机号
    data_dict = {"phone_number": 14252526364, "captcha": "", "pid": "account"}
    if code == 1:
        # 先获取发送验证码接口的 ticket
        ticket = accounts_api_ticket(url)
        # 请求发送验证码接口
        request_data = requests.post(url=url + "/tiger/v3/app/accounts/captcha/login/post-process",
                                     headers={"X-Captcha-Ticket": ticket},
                                     json={"phone_number": "14252526364"})
        if request_data.status_code == 204:
            print("验证码发送正确")
        else:
            print("验证码发送失败")
            print(request_data.json())
        data_dict["captcha"] = "555555"
    elif code == 2:
        # 查询发送的验证码
        time.sleep(1)
        # 去查询正确验证码
        data_dict["captcha"] = get_captcha_method(url, 14252526364)
    elif code == 3:
        data_dict["captcha"] = get_captcha_method(url, 14252526364)
    elif code == 5:
        data_dict["captcha"] = "555555"
        data_dict["phone_number"] = "13037375544"
    elif code == 6:
        # 先获取发送验证码接口的 ticket
        ticket = accounts_api_ticket(url)
        # 请求发送验证码接口
        request_data = requests.post(url=url + "/tiger/v3/app/accounts/captcha/login/post-process",
                                     headers={"X-Captcha-Ticket": ticket},
                                     json={"phone_number": "14415454854"})
        if request_data.status_code == 204:
            print("验证码发送正确")
            # 查询发送的验证码
            time.sleep(1)
            # 去查询正确验证码
            data_dict["captcha"] = get_captcha_method(url, 14415454854)
        else:
            print("验证码发送失败")
            print(request_data.json())
        data_dict["phone_number"] = "14415454854"

    request["req_json"] = data_dict
    return request


def accounts_phone_login_silence(request, code, url):
    # 14252526301 手机为自动化注册手机号
    data_dict = {"phone_number": 14252526301, "captcha": "", "pid": "account"}
    if code == 1:
        # 先获取发送验证码接口的 ticket
        ticket = accounts_api_ticket(url)
        # 请求发送验证码接口
        request_data = requests.post(url=url + "/tiger/v3/app/accounts/captcha/login/silence",
                                     headers={"X-Captcha-Ticket": ticket},
                                     json={"phone_number": "14252526301"})
        if request_data.status_code == 204:
            print("验证码发送正确")
        else:
            print("验证码发送失败")
            print(request_data.json())
        data_dict["captcha"] = "555555"
    elif code == 2:
        # 查询发送的验证码
        time.sleep(1)
        # 去查询正确验证码
        data_dict["captcha"] = get_captcha_method(url, 14252526301)
    elif code == 3:
        data_dict["captcha"] = get_captcha_method(url, 14252526301)
    elif code == 5:
        data_dict["captcha"] = "555555"
        data_dict["phone_number"] = "13037375544"
    elif code == 6:
        phone = return_phone()
        # 先获取发送验证码接口的 ticket
        ticket = accounts_api_ticket(url)
        # 请求发送验证码接口
        request_data = requests.post(url=url + "/tiger/v3/app/accounts/captcha/login/silence",
                                     headers={"X-Captcha-Ticket": ticket},
                                     json={"phone_number": phone})
        if request_data.status_code == 204:
            print("验证码发送正确")
            # 查询发送的验证码
            time.sleep(1)
            # 去查询正确验证码
            data_dict["captcha"] = get_captcha_method(url, phone)
        else:
            print("验证码发送失败")
            print(request_data.json())
        data_dict["phone_number"] = phone

    request["req_json"] = data_dict
    return request
