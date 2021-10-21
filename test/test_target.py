import pytest

from fact.exceptions import SSHInfoError
from fact.target import SSHAccessInfo


def test_ssh_host_format_error():
    with pytest.raises(SSHInfoError) as e:
        SSHAccessInfo("testuser", "127.0.0.1", 22)
    assert "Input is not a list of 1 host" in str(e.value)


def test_ssh_number_of_host_error():
    with pytest.raises(SSHInfoError) as e:
        SSHAccessInfo("testuser", ["127.0.0.1", "127.0.0.2"], 22)
    assert "More than 1 target host" in str(e.value)
