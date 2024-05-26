"""Unit tests to validate the adapters.ExplorationAdapter"""

import pytest
from pyventim import adapters  # pylint: disable=E0401
from pyventim import exceptions  # pylint: disable=E0401


exp = adapters.RestAdapter(hostname="https://httpstat.us/")
exp.session.headers.update({"accept": "application/json"})


def test_response_success():
    """Test success with a 200"""
    result = exp.get("200")
    assert isinstance(result, adapters.RestResult)
    assert result.status_code == 200
    assert result.message == "OK"
    assert result.json_data == {"code": 200, "description": "OK"}


def test_response_failure():
    """Test failure with a 404"""
    with pytest.raises(
        exceptions.RestException,
        match="404: Not Found",
    ):
        exp.get("404")


def test_respone_invalid_json():
    """Test json decode failure with a html response."""
    exp.session.headers.update({"accept": "application/html"})
    with pytest.raises(
        exceptions.RestException,
        match="Bad JSON in response",
    ):
        exp.get("200")
