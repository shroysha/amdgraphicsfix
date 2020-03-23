import os
import sys

user = os.popen("whoami").read()
print(user)
assert user == "root\n"

# Mount file system
os.system("/sbin/fsck -fy")
os.system("/sbin/mount -uw /")

# Set nvram
os.system("nvram fa4ce28d-b62f-4c99-9cc3-6815686e30f9:gpu-power-prefs=%01%00%00%00")

# Make symlink to this project in root
DIR = sys.path[0]


def force_symlink(source, dest):
    os.system("ln -fs " + source + " " + dest)


force_symlink(DIR, "/")

# Move login hooks
force_symlink(DIR + "/force-iGPU-boot.sh", "/")
force_symlink(DIR + "/.login-hook.sh", "/Users/Shawn/")

# Move all amd kexts
SYSTEM_KEXT_DIR = "/System/Library/Extensions/"
AMD_KEXTS_DIR = DIR + "/amd_kexts/"
os.system("mkdir " + AMD_KEXTS_DIR)


def move_without_error(source, dest):
    os.system("mv " + source + " " + dest + " 2>/dev/null")


move_without_error(SYSTEM_KEXT_DIR + "/AMD*.* ", AMD_KEXTS_DIR)

# Restore brightness
restore_kexts = ["/AMDLegacySupport.kext/",
                 "/AMDLegacyFrameBuffer.kext/",
                 "/AMD6000Controller.kext/",
                 "/AMDShared.kext/",
                 "/AMDFrameBuffer.kext/"]

for kext in restore_kexts:
    move_without_error(AMD_KEXTS_DIR + kext, SYSTEM_KEXT_DIR)
