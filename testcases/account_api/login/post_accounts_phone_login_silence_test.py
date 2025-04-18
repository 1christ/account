# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_api\login\post_accounts_phone_login_silence.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCasePostAccountsPhoneLoginSilence(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-code-status_code-msg": [
                    ["手机验证码登录-输入错误的验证码登录", 1, 403, "校验验证码失败"],
                    ["手机验证码登录-输入正确的验证码登录", 2, 200, "token"],
                    ["手机验证码登录-输入已经过期的验证码登录", 3, 403, "校验验证码失败"],
                    ["手机验证码登录-验证码传空登录", 4, 400, "输入格式错误"],
                    ["手机验证码登录-不发送验证码登录", 5, 403, "校验验证码失败"],
                    ["手机验证码登录-手机号未注册,静默注册", 6, 200, "token"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("/tiger/v3/app/accounts/phone/login/silence通过手机号短信登入(静默登入)")
        .variables(**{"base_url": "${ENV(ACCOUNT_API_URL)}"})
        .base_url("${ENV(ACCOUNT_API_URL)}")
    )

    teststeps = [
        Step(
            RunRequest("$name")
            .setup_hook("${accounts_phone_login_silence($request,$code,$base_url)}")
            .post("/tiger/v3/web/accounts/phone/login/silence")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCasePostAccountsPhoneLoginSilence().test_start()
