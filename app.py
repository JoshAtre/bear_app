from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load data from CSV into a dictionary
def load_bear_data():
    bear_data = {}
    with open('race_to_bear.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            bear_data[row[0]] = {'bear': row[1], 'image': row[2]}
    return bear_data

# Route to handle form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    bear_data = load_bear_data()
    selected_race = request.form.get('race', '')  # Get the selected race from the form
    bear = bear_data.get(selected_race)  # Get the corresponding bear based on the selected race
    return render_template('index.html', bear=bear, selected_race=selected_race)


if __name__ == '__main__':
    app.run(debug=True)