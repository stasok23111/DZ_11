from flask import Flask, render_template
from utils import *



app = Flask(__name__)


@app.route('/')
def candidates():

    return render_template('list.html')


@app.route('/candidate/<int:uid>')
def profile_candidate(uid):
    data = get_candidate(uid)
    img = data["picture"]
    return render_template('card.html', data=data, img=img)


@app.route('/search/<candidate_name>')
def search_name(candidate_name):
    data = get_candidates_by_name(candidate_name)
    len_data = len(data)
    return render_template('search.html', data=data, len_data=len_data)

@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    data = get_candidates_by_skill(skill_name)

    return render_template('skill.html', data=data, skill_name=skill_name)



app.run()
