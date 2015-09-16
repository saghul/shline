
def add_nvm_segment():
    import os
    import subprocess

    try:
        output = subprocess.check_output(['bash', '-c', '. .nvm/nvm.sh; nvm current'])
    except (OSError, subprocess.CalledProcessError):
        return

    version = output.rstrip()
    if version == 'system':
        return

    shline.append(' node: %s ' % version, Color.NVM_FG, Color.NVM_BG)

add_nvm_segment()
