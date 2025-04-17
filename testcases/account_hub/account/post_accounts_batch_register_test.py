# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_hub\account\post_accounts_batch_register.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCasePostAccountsBatchRegister(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-code-status_code-msg": [
                    ["通用批量用户名注册-传不存在的pid", 1, 403, "不合法的pid"],
                    ["通用批量用户名注册-pid传空", 2, 400, "size must be between 1 and 10"],
                    ["通用批量用户名注册-密码传空", 3, 400, "size must be between 6 and 60"],
                    ["通用批量用户名注册-密码小于6位", 4, 400, "size must be between 6 and 60"],
                    ["通用批量用户名注册-密码大于60位", 5, 400, "size must be between 6 and 60"],
                    ["通用批量用户名注册-username传空", 6, 400, "a-zA-Z"],
                    ["通用批量用户名注册-username不符合规则", 7, 400, "a-zA-Z"],
                    ["通用批量用户名注册-username已存在", 8, 200, "false"],
                    ["通用批量用户名注册-传多个用户名,其中一个不符合规则", 9, 400, "a-zA-Z"],
                    ["通用批量用户名注册-通过用户名注册一个账号", 10, 200, "true"],
                    ["通用批量用户名注册-通过用户名注册多个账号", 11, 200, "true"],
                    ["通用批量用户名注册-pid不传", 12, 400, "HttpMessageNotReadableException"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("/accounts/batch/register 通用批量用户名注册").base_url("${ENV(BASE_URL)}")

    teststeps = [
        Step(
            RunRequest("$name")
            .setup_hook("${account_batch_register($request,$code)}")
            .post("/accounts/batch/register")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCasePostAccountsBatchRegister().test_start()
