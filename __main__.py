import sys
from amdgraphicsfix import assert_is_root, force_symlink, make_directory, move_supress_error, mount_file_system, \
    set_nvram


DIR = sys.path[0]
RESOURCE_DIR = DIR + "resources/"
brightness_kexts = ["AMDLegacySupport.kext/",
                    "AMDLegacyFrameBuffer.kext/",
                    "AMD6000Controller.kext/",
                    "AMDShared.kext/",
                    "AMDFrameBuffer.kext/"]

SYSTEM_KEXT_DIR = "/System/Library/Extensions/"
AMD_KEXTS_DIR = RESOURCE_DIR + "amd_kexts/"


assert_is_root()
mount_file_system()
set_nvram()
# Move all amd kexts
make_directory(AMD_KEXTS_DIR)
move_supress_error(SYSTEM_KEXT_DIR + "AMD*.* ", AMD_KEXTS_DIR)

# Restore brightness kexts
for kext in brightness_kexts:
    move_supress_error(AMD_KEXTS_DIR + kext, SYSTEM_KEXT_DIR)


force_symlink(DIR, "/")

# login hooks
force_symlink(RESOURCE_DIR + "force-iGPU-boot.sh", "/")
force_symlink(RESOURCE_DIR + ".login-hook.sh", "/Users/Shawn/")
