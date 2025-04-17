# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_hub\account\post_accounts_search.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCasePostAccountsSearch(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "name-status_code-msg-type": [
                    ["搜索用户信息-使用ID查询已经注册的用户 ", 200, "id", 1],
                    ["搜索用户信息-搜索不存在的用户ID ", 200, "", 2],
                    ["搜索用户信息-使用email 查询已经注册的邮箱 ", 200, "fullname", 3],
                    ["搜索用户信息-使用存在手机号查询用户信息 ", 200, "phone_number", 4],
                    ["搜索用户信息-使用不存在手机号查询用户信息 ", 200, "", 5],
                    ["搜索用户信息-使用QQ查询用户信息", 200, "nickname", 6],
                    ["搜索用户信息-使用用户名查询用户信息 ", 200, "id", 7],
                    ["搜索用户信息-使用identity 查询email ", 200, "id", 8],
                    ["搜索用户信息-使用identity 查询手机号 ", 200, "id", 9],
                    ["搜索用户信息-使用identity 查询用户名 ", 200, "id", 10],
                    ["搜索用户信息-使用几个查询字段查询 ", 200, "", 11],
                    ["搜索用户信息-组合查询 ", 200, "phone_number", 12],
                    ["搜索用户信息-不传查询字段进行查询 ", 403, "查询字段不能为空", 13],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("/accounts/search B端搜索用户信息")
        .variables(**{"url": "${ENV(BASE_URL)}"})
        .base_url("${ENV(BASE_URL)}")
    )

    teststeps = [
        Step(
            RunRequest("$name")
            .setup_hook("${accounts_search($request,$type)}")
            .post("/accounts/search")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_contains("text", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCasePostAccountsSearch().test_start()
