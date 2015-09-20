
def add_shlvl_segment():
    import os

    if 'TMUX' in os.environ:
        return

    try:
        shlvl = int(os.getenv('SHLVL', 0))
    except ValueError:
        return

    if shlvl > 1:
        shline.append(' SH: %s ' % shlvl, Color.SHLVL_FG, Color.SHLVL_BG)

add_shlvl_segment()
