from flask import Flask, render_template
from utils import *

app = Flask(__name__, template_folder='template')


@app.route("/")
def index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = get_candidate_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skills(skill):
    candidates = get_candidate_by_skill(skill)
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


app.run(debug=True)
