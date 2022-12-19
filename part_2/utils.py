import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_all():
    return load_candidates()


def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_candidate_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates


def get_candidate_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result
