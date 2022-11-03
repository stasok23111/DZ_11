import json


file_name = "candidates.json"



def load_candidates_from_json(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate(i_d):
    return load_candidates_from_json(file_name)[i_d - 1]


def get_candidates_by_skill(skill_name):
    candidates = []
    for i in load_candidates_from_json(file_name):
        if skill_name.lower() in i["skills"].lower():
            candidates.append(i)
    return candidates


def get_candidates_by_name(candidate_name):
    candidates = []
    for i in load_candidates_from_json(file_name):
        if candidate_name.lower() in i["name"].lower():
            candidates.append(i)
    return candidates




