import os


def assert_is_root():
    user = os.popen("whoami").read()
    print(user)
    assert user == "root\n"


def mount_file_system():
    os.system("/sbin/fsck -fy")
    os.system("/sbin/mount -uw /")


def set_nvram():
    os.system("nvram fa4ce28d-b62f-4c99-9cc3-6815686e30f9:gpu-power-prefs=%01%00%00%00")


def force_symlink(source, dest):
    os.system("ln -fs " + source + " " + dest)


def move_supress_error(source, dest):
    os.system("mv " + source + " " + dest + " 2>/dev/null")


def make_directory(dest):
    os.system("mkdir " + dest)
