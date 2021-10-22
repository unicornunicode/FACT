from fact.target import (
    TargetEndpoint,
    SSHAccessInfo,
    SSHProxyInfo,
    SSHAccessInfoOptional,
)


if __name__ == "__main__":
    username = "your_remote_username"
    host = ["127.0.0.1"]
    port = 22
    remote_image_path = "/dev/loop2"
    save_location = "/home/user/Desktop/machine1.gz"
    file_io = open(save_location, "wb")

    client_info = SSHAccessInfo(username, host, port)
    optional_info = SSHAccessInfoOptional()
    proxy_info = SSHProxyInfo()

    target = TargetEndpoint(client_info, proxy_info, optional_info)
    target.collect_image(remote_image_path, file_io)
    file_io.close()
