from flask import Flask, render_template
from utils import load_candidtates, get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill


app = Flask(__name__)

@app.route("/")
def candidates_main():
    candidates_data = load_candidtates()
    return render_template('list.html', candidates = candidates_data)

@app.route("/candidate/<int:cand_id>")
def candidates_uid(cand_id):
    candidates_data = load_candidtates()
    candidate = get_candidate_by_id(cand_id, candidates_data)
    if not candidate:
        return "Нет такого кандидата"
    return render_template('single.html', candidate = candidate)

@app.route("/search/<cand_name>")
def candidates_search(cand_name):
    candidates_data = load_candidtates()
    candidates = get_candidate_by_name(cand_name, candidates_data)
    if not candidates:
        return "Нет такого кандидата"
    return render_template('search.html', candidates = candidates)


@app.route("/skill/<skill_name>")
def candidates_search_by_skill(skill_name):
    candidates_data = load_candidtates()
    candidates = get_candidate_by_skill(skill_name, candidates_data)
    if not candidates:
        return "Нет такого кандидата"
    return render_template('search.html', candidates = candidates)

app.run()
