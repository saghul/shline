
def add_jobs_segment():
    if powerline.args.jobs > 0:
        powerline.append(' %d ' % powerline.args.jobs, Color.JOBS_FG, Color.JOBS_BG)

add_jobs_segment()
