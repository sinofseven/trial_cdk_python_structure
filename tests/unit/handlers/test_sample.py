import pytest
import sample.sample as index


class TestHandler:
    @pytest.mark.parametrize(
        "set_environments, expected",
        [
            (
                {"SYSTEM_NAME": "ZGMF-X10A Freedom"},
                index.EnvironmentVariables(system_name="ZGMF-X10A Freedom"),
            ),
            (
                {"SYSTEM_NAME": "STTS-909 Rising Freedom"},
                index.EnvironmentVariables(system_name="STTS-909 Rising Freedom"),
            ),
        ],
        indirect=["set_environments"],
    )
    @pytest.mark.usefixtures("set_environments")
    def test_normal(self, dummy_context, expected):
        # 実際のテストだともう少し引数は工夫する
        actual = index.handler(None, dummy_context)
        assert actual == expected
