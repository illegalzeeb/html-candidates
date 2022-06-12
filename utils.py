import json

def load_candidtates() -> list[dict]:
    """
    Читает файл candidates.json, возвращает как список словарей candidates_data
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        cand_data = json.load(file)
    return cand_data


def get_candidate_by_id(cand_id, cand_data) -> dict:
    """
    Возвращает одного кандидата по id
    """
    for person in cand_data:
        if person['id'] == cand_id:
            return person
        else:
            pass

def get_candidate_by_name(cand_name, cand_data) -> list[dict]:
    """
    Возвращает одного кандидата по имени
    """
    person_list = []
    for person in cand_data:
        if person['name'] == cand_name:
            person_list.append(person)
        else:
            pass
    return person_list


def get_candidate_by_skill(cand_skill, cand_data) -> list[dict]:
    """
    Возвращает список кандидатов по наличию навыка
    """
    person_list = []
    for person in cand_data:
        if cand_skill in person['skills'].lower().split(", "):
            person_list.append(person)
        else:
            pass
    return person_list