from fact.target import _parse_lsblk_output


def test_linux_lsblk_parsing():
    expected = [
        ("loop9", 33878016, "loop", "/snap/snapd/13170"),
        ("sda", 85899345920, "disk", ""),
        ("sda1", 536870912, "part", "/boot/efi"),
    ]

    with open("test/files/lsblk_test.txt", "rb") as f:
        data = f.read()
        lsblk_list = _parse_lsblk_output(data)
        assert expected == lsblk_list
