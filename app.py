from flask import Flask, render_template, request
from prediction import get_label_prediction
from get_car_data import get_data_by_label

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')  #creates a Flask application instance named app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/dropdown')
def dropdown():
    return render_template('dropdown.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    description = request.form['description']
    # Perform further analysis with the description here
    predicted_label = get_label_prediction(description)
    recommended_vehicles = get_data_by_label(predicted_label[0])

    return render_template('recommended.html', recommended_vehicles=recommended_vehicles[:10])

@app.route('/analyze_dropdown', methods=['POST'])
def analyze_dropdown():
    
    usage = request.form['usage']
    experience = request.form['experience']
    efficiency = request.form['efficiency']
    terrain = request.form['terrain']
    cargo = request.form['cargo']
    safety = request.form['safety']
    transmission = request.form['transmission']
    long_trips = request.form['long_trips']
    profession = request.form['profession']
    business_travel = request.form['business_travel']
    tech_preference = request.form['tech_preference']
    towing = request.form['towing']
    ev_interest = request.form['ev_interest']

    # Combine the preferences into a single string for prediction
    preferences = f" {usage} {experience} {efficiency} {terrain} {cargo} {safety} {transmission} {long_trips} {profession} {business_travel} {tech_preference} {towing} {ev_interest}"
    predicted_label = get_label_prediction(preferences)
    recommended_vehicles = get_data_by_label(predicted_label[0])

    return render_template('recommended.html', recommended_vehicles=recommended_vehicles[:10])

if __name__ == '__main__':
    app.run(debug=True)
