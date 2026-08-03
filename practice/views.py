import json

def mSkills(skillProfile, requiredSkill):
    can = {skill.lower() for skill in skillProfile}
    job_req ={skill.lower() for skill in requiredSkill}

    match = can.intersection(job_req)

    percentage = (len(match) / len(job_req)) * 100

    return {
        "percent" : percentage(round,2)
    }

def MJobs():
    with open("profile.json") as f:
        skillProfile = json.load(f)

    with open("unique_jobs.json") as f:
        requiredSkill = json.load(f)

    result = []

    for job in requiredSkill:
        job.split(",")

        mSkills(
            skillProfile["skills"],
            job["tagsAndSkills"]
        )
        result.append({
            "job title" : job["title"]
        })
    for res in result:
        print(res)

MJobs()