from pathlib import Path
import json

from pytest import fixture, MonkeyPatch


@fixture(scope="function")
def set_environments(request, monkeypatch: MonkeyPatch):
    param: dict = request.param

    for k, v in param.items():
        monkeypatch.setenv(k, v)


@fixture(scope="session")
def path_test_root() -> Path:
    return Path(__file__).parent


@fixture(scope="function")
def load_json(request, path_test_root):
    def load(filename: str):
        with open(path_test_root.joinpath(f"fixtures/load_json/{filename}")) as f:
            return json.load(f)

    names: list[str] = request.param

    return [load(x) for x in names]
