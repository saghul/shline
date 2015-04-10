

def add_darcs_segment():
    import os
    import re
    import subprocess

    env = {"LANG": "C", "HOME": os.getenv("HOME")}

    def get_darcs_status():
        has_modified_files = False
        has_missing_files = False
        try:
            output = subprocess.check_output(['darcs', 'whatsnew', '-s', '--look-for-adds'], env=env)
        except subprocess.CalledProcessError:
            pass
        else:
            for line in output.split('\n'):
                modified_files = re.findall(r"M (.*)", line)
                missing_files = re.findall(r"a (.*)", line)
                if line == 'No changes!':
                    continue
                if missing_files:
                    has_missing_files = True
                if modified_files:
                    has_modified_files = True
        return has_modified_files, has_missing_files

    try:
        output = subprocess.check_output(['darcs', 'show', 'repo'], env=env)
    except (subprocess.CalledProcessError, OSError):
        return

    repo_info = {}
    for line in output.split('\n'):
        if line == '':
            continue
        name, var = line.partition(": ")[::2]
        repo_info[name.strip()] = var

    if repo_info['Type'] != 'darcs':
        return

    bg = Color.REPO_CLEAN_BG
    fg = Color.REPO_CLEAN_FG
    has_modified_files, has_missing_files = get_darcs_status()
    repo_type = "%s(%s)" % (repo_info['Type'], repo_info['Format'])
    if has_modified_files or has_missing_files:
        bg = Color.REPO_DIRTY_BG
        fg = Color.REPO_DIRTY_FG
        extra = ''
        if has_missing_files:
            extra += '+'
        repo_type += (' ' + extra if extra != '' else '')
    return shline.append(' %s %s ' % (shline.branch, repo_type), fg, bg)

add_darcs_segment()

