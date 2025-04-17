# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcases\account_hub\address\address.yml
import pytest

from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters


class TestCaseAddress(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"name-default": [["地址库 - 添加普通地址", "false"], ["地址库 - 添加默认地址", "true"]]}
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("地址相关").base_url("${ENV(BASE_URL)}")

    teststeps = [
        Step(
            RunRequest("添加收货地址")
            .post("/accounts/delivery-information")
            .with_json(
                {
                    "cityId": 202,
                    "consignee": 1,
                    "countryId": 156,
                    "defaultAddress": "$default",
                    "detail": "第一次添加收货地址",
                    "districtId": 1859,
                    "phoneNumber": "18585855555",
                    "provinceId": 19,
                    "userId": 10000,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("text", "")
        ),
        Step(
            RunRequest("获取所有收货地址")
            .get("/accounts/delivery-information?userId=10000")
            .extract()
            .with_jmespath("body[0].id", "id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("text", "第一次添加收货地址")
        ),
        Step(
            RunRequest("编辑收货地址")
            .patch("/accounts/delivery-information")
            .with_json(
                {
                    "cityId": 202,
                    "consignee": 1,
                    "countryId": 156,
                    "defaultAddress": "$default",
                    "detail": "第二次编辑收货地址",
                    "districtId": 1859,
                    "phoneNumber": "18585855555",
                    "provinceId": 19,
                    "userId": 10000,
                    "deliveryId": "$id",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("删除收货地址")
            .delete("/accounts/delivery-information")
            .with_json({"userId": 10000, "deliveryId": "$id"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseAddress().test_start()
