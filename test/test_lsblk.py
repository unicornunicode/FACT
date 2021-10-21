from fact.target import _parse_lsblk_output


def test_linux_lsblk_parsing():

    expected = {
        "disk_info": [
            {
                "dev_name": "loop9",
                "size": "33878016",
                "type": "loop",
                "mountpoint": "/snap/snapd/13170",
            },
            {
                "dev_name": "sda",
                "size": "85899345920",
                "type": "disk",
                "mountpoint": "",
            },
            {
                "dev_name": "sda1",
                "size": "536870912",
                "type": "part",
                "mountpoint": "/boot/efi",
            },
        ]
    }
    with open("test/files/lsblk_test.txt", "rb") as f:
        data = f.read()
        lsblk_dict = _parse_lsblk_output(data)
        assert expected == lsblk_dict
