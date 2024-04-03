from dataclasses import dataclass

import pytest

import utils.dataclasses as index


@dataclass
class SampleClass:
    country: str
    capital: str


class TestLoadEnvironments:
    @pytest.mark.parametrize(
        "set_environments, options, expected",
        [
            (
                {"COUNTRY": "オーブ首長国連邦", "CAPITAL": "オロファト"},
                {"class_dataclass": SampleClass},
                SampleClass(country="オーブ首長国連邦", capital="オロファト"),
            ),
            (
                {"COUNTRY": "ユーラシア連邦", "CAPITAL": "モスクワ"},
                {"class_dataclass": SampleClass},
                SampleClass(country="ユーラシア連邦", capital="モスクワ"),
            ),
        ],
        indirect=["set_environments"],
    )
    @pytest.mark.usefixtures("set_environments")
    def test_normal(self, options, expected):
        actual = index.load_environments(**options)
        assert actual == expected
