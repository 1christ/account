# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_api\login\post_accounts_login.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCasePostAccountsLogin(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-identity-password-pid-status_code-msg": [
                    [
                        "手机号密码登录-正确手机号密码登录",
                        "14266669999",
                        "123456",
                        "account",
                        200,
                        "token",
                    ],
                    [
                        "手机号密码登录-错误密码登录",
                        "14266669999",
                        "123456789",
                        "account",
                        403,
                        "用户不存在或者密码错误",
                    ],
                    [
                        "邮箱密码登录-正确邮箱密码登录",
                        "14266669999@qq.com",
                        "123456",
                        "account",
                        200,
                        "token",
                    ],
                    [
                        "邮箱密码登录-错误密码登录",
                        "14266669999@qq.com",
                        "123456789",
                        "account",
                        403,
                        "用户不存在或者密码错误",
                    ],
                    [
                        "用户名密码登录-正确用户名密码登录",
                        "qwtest1997",
                        "123456",
                        "account",
                        200,
                        "token",
                    ],
                    [
                        "用户名密码登录-错误密码登录",
                        "qwtest1997",
                        "123456789",
                        "account",
                        403,
                        "用户不存在或者密码错误",
                    ],
                    [
                        "手机号密码登录-手机号未注册",
                        "142666699991",
                        "123456789",
                        "account",
                        403,
                        "用户不存在或者密码错误",
                    ],
                    [
                        "手机号密码登录-PID不存在",
                        "14266669999",
                        "123456",
                        "acco1unt",
                        403,
                        "不合法的 pid",
                    ],
                    ["手机号密码登录-identity不传", "", "123456", "account", 400, "输入格式错误"],
                    ["手机号密码登录-password不传", "14266669999", "", "account", 400, "输入格式错误"],
                    ["手机号密码登录-PID不传", "14266669999", "123456", "", 400, "输入格式错误"],
                    ["手机号密码登录-PID不传", "14266669999", "123456", "", 400, "输入格式错误"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("/tiger/v3/app/accounts/login 用户名密码登录").base_url(
        "${ENV(ACCOUNT_API_URL)}"
    )

    teststeps = [
        Step(
            RunRequest("$name")
            .post("/tiger/v3/web/accounts/login")
            .with_json(
                {"identity": "$identity", "password": "$password", "pid": "$pid"}
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCasePostAccountsLogin().test_start()
