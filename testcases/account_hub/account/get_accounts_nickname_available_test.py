# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_hub\account\get_accounts_nickname_available.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCaseGetAccountsNicknameAvailable(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-nickname-msg": [
                    [
                        "使用一个不符合规则的昵称查询",
                        "43erewrwerewrewewewewewew",
                        "43erewrwerewrewewewewewew",
                    ],
                    ["使用一个不存在的昵称进行查询", "q2w3e4r5o9", "q2w3e4r5o9"],
                    ["使用一个已经存在的昵称进行查询", "qinwang", "nickname"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("/accounts/nickname/available 检查并返回可用昵称").base_url(
        "${ENV(BASE_URL)}"
    )

    teststeps = [
        Step(
            RunRequest("$name")
            .get("/accounts/nickname/available")
            .with_params(**{"nickname": "$nickname"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetAccountsNicknameAvailable().test_start()
