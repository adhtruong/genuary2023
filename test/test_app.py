import pytest

from app import main


def test_app(capsys: pytest.CaptureFixture) -> None:
    main()
    assert "Hello world" in capsys.readouterr().out
