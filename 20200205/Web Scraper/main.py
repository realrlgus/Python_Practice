from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_sof_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()
jobs = sof_jobs + indeed_jobs
save_to_file(jobs)
