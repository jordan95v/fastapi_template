from unittest.mock import MagicMock
from pytest_mock import MockerFixture
from core.config import SESSION
from core.models.base import Base
import pytest

__all__: list[str] = ["TestBase"]


class TestBase:
    @pytest.mark.parametrize("method_name", ["add", "commit"])
    def test_base_methods(self, mocker: MockerFixture, method_name: str) -> None:
        session_mock: MagicMock = mocker.patch.object(SESSION, method_name)
        base: Base = Base()
        getattr(base, method_name)()
        session_mock.assert_called_once()
