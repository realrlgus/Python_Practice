import csv


def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="UTF8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
