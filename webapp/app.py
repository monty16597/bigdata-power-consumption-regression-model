from flask import Flask, request, jsonify, render_template
ZONES = ['zone_1', 'zone_2', 'zone_3']
import pickle
import pandas as pd
# load model from pickle file
models = {}
for zone in ZONES:
    with open(f'power_consumption_model_{zone}.pkl', 'rb') as file:
        models[zone] = pickle.load(file)

def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df['hour'] = df.index.hour
    df['minute'] = df.index.minute
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['day'] = df.index.month
    df['year'] = df.index.year
    df['season'] = df['month'] % 12 // 3 + 1
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df.astype(float)


app = Flask(__name__)

# Route for root URL to render index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_data', methods=['POST'])
def submit_data():
    try:
        temperature = float(request.form.get('temperature'))
        humidity = float(request.form.get('humidity'))
        wind_speed = float(request.form.get('wind_speed'))
        general_diffuse_flows = float(request.form.get('general_diffuse_flows'))
        diffuse_flows = float(request.form.get('diffuse_flows'))
        zone = request.form.get('zone')
        datetime = request.form.get('timestamp')

        data = {
            'datetime': datetime,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'general_diffuse_flows': general_diffuse_flows,
            'diffuse_flows': diffuse_flows
        }
        df = pd.DataFrame([data])
        df = df.set_index('datetime')
        df.index = pd.to_datetime(df.index)
        df = create_features(df)
        _predict = models[zone].predict(df)
    except Exception as e:
        print(e)
        return jsonify({'data': data, 'prediction': None, 'error': str(e)})

    return jsonify({'data': data, 'prediction': float(_predict[0]), 'error': None})


if __name__ == '__main__':
    app.run(debug=True)
