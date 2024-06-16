from flask import Flask, render_template, request, session, redirect, url_for
from prediction import get_label_prediction
from get_car_data import get_data_by_label, save_history, save_vehicle_history, get_history_username, get_all_vehicle_ids_from_history_id, get_car_by_id
from login import store_user, check_password

app = Flask(__name__, static_url_path='/static')  #creates a Flask application instance named app
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    print(session)
    if 'user' not in session:
        return render_template('index.html')
    else:
        return redirect(url_for('home'))

@app.route('/home')
def home():
    username = ""
    if 'user' in session:
        username = session['user']

    return render_template('home.html', username = username)

@app.route('/register-page')
def register_page():
    return render_template('register_page.html', error="")

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if username != "" and password != "":
        result = store_user(username, password)
        if result == False:
            return render_template('register_page.html', error="Username already exist!")

        return redirect(url_for('index'))
    return render_template('register_page.html', error="Username and password cannot be empty!")

@app.route('/login-page')
def login_page():
    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def loging():
    username = request.form['username']
    password = request.form['password']

    if check_password(username, password):
        session['user'] = username
        return redirect(url_for('home'))

    return render_template('login_page.html')

@app.route('/history')
def history_page():
    history_ids = get_history_username(session['user'])
    return render_template('histories.html',history_ids = history_ids)


# Delete route
@app.route('/get_history/<int:history_id>', methods=['GET'])
def get_history_by_id(history_id):
    # Code to delete the item with the given ID
    # For demonstration purposes, let's remove the item from default_data
    vehicles_ids= get_all_vehicle_ids_from_history_id(history_id)
    ids = [item[0] for item in vehicles_ids]

    result = []
    for vehicle_id in ids:
        result.extend(get_car_by_id(vehicle_id))

    return render_template('recommended.html', recommended_vehicles=result)

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

    if 'user' in session:
        historyid = save_history(session['user'])
        save_vehicle_history(historyid,recommended_vehicles)

    return render_template('recommended.html', recommended_vehicles=recommended_vehicles)

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

    if 'user' in session:
        historyid = save_history(recommended_vehicles, session['user'])
        save_vehicle_history(historyid,recommended_vehicles)

    return render_template('recommended.html', recommended_vehicles=recommended_vehicles)

if __name__ == '__main__':
    app.run(debug=True)