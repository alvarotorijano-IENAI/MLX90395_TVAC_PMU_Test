import os
import subprocess
from SCons.Script import Import
from platformio.package.manager.tool import ToolPackageManager

Import("env")

def after_build(source, target, env):
    # Path to the ELF file
    elf_path = target[0].get_abspath()
    dump_path = os.path.join(env["PROJECT_DIR"], "dump.s")

    print(">>> Running avr-objdump...")

    # Locate avr-objdump inside PlatformIO toolchain
    toolchain_mgr = ToolPackageManager()
    toolchain_dir = toolchain_mgr.get_package("toolchain-atmelavr").path
    objdump = os.path.join(toolchain_dir, "bin", "avr-objdump.exe")

    cmd = [objdump, "-h", "-S", elf_path]

    # Execute and write output to dump.s
    with open(dump_path, "w") as f:
        subprocess.run(cmd, stdout=f)

    print(f">>> Dump created at: {dump_path}")

# Hook: run after firmware.elf is built
env.AddPostAction("$BUILD_DIR/${PROGNAME}.elf", after_build)