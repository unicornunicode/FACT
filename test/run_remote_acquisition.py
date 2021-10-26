from fact.target import (
    TargetEndpoint,
    SSHAccessInfo,
    SSHProxyInfo,
    SSHAccessInfoOptional,
)

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    username = "your_remote_username"
    host = ["127.0.0.1"]
    port = 22
    test_keywords = [""]

    client_info = SSHAccessInfo(username, host, port)
    optional_info = SSHAccessInfoOptional()
    proxy_info = SSHProxyInfo()

    target = TargetEndpoint(client_info, proxy_info, optional_info)

    if "image" in test_keywords:
        save_location = "/home/user/Desktop/lsblk_data_remote"
        remote_image_path = "/dev/sda"

        file_io = open(save_location, "wb")
        target.collect_image(remote_image_path, file_io)
        file_io.close()

    if "lsblk" in test_keywords:
        dic = target.get_all_available_disk()
        print(dic)
