# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_hub\account\captcha.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCaseCaptcha(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-captchaType-sendType-phone_number-msg-status_code": [
                    ["验证码- 通用手机验证码验证通过", "COMMON", 0, 14996857401, "", 200],
                    [
                        "验证码- 通用手机验证码验证不通过",
                        "COMMON",
                        0,
                        14996857402,
                        "CaptchaVerifyFailedException",
                        422,
                    ],
                    ["验证码- 登录手机验证码验证通过", "LOGIN", 0, 14996857403, "", 200],
                    [
                        "验证码- 登录手机验证码验证不通过",
                        "LOGIN",
                        0,
                        14996857404,
                        "CaptchaVerifyFailedException",
                        422,
                    ],
                    ["验证码- 注册手机验证码验证通过", "REGISTER", 0, 14996857405, "", 200],
                    [
                        "验证码- 注册手机验证码验证不通过",
                        "REGISTER",
                        0,
                        14996857406,
                        "CaptchaVerifyFailedException",
                        422,
                    ],
                    ["验证码- 邮箱验证码验证通过", "COMMON", 2, "qinwang@codemao.cn", "", 200],
                    [
                        "验证码- 邮箱验证码验证不通过",
                        "COMMON",
                        2,
                        "1583492267@qq.com",
                        "CaptchaVerifyFailedException",
                        422,
                    ],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("发送验证码 - 查询验证码- 校验验证码")
        .variables(**{"url": "${ENV(BASE_URL)}"})
        .base_url("${ENV(BASE_URL)}")
    )

    teststeps = [
        Step(
            RunRequest("发送验证码")
            .post("/accounts/captcha/send")
            .with_json(
                {
                    "acwTc": None,
                    "captchaType": "$captchaType",
                    "extend": "自动化脚本",
                    "identity": "account",
                    "phoneNumber": "$phone_number",
                    "pid": "account",
                    "sendType": "$sendType",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("text", "true")
        ),
        Step(
            RunRequest("验证码查询")
            .get("/accounts/captcha/search")
            .with_params(**{"phoneNumber": "$phone_number"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("text", "captcha")
        ),
        Step(
            RunRequest("校验短信验证码")
            .setup_hook("${captcha($request,$url,$phone_number)}")
            .post("/accounts/captcha/check")
            .with_json(
                {
                    "acwTc": None,
                    "captchaType": "$captchaType",
                    "sendType": "$sendType",
                    "phoneNumber": "$phone_number",
                }
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCaseCaptcha().test_start()
