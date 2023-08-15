from flask import Flask, render_template, request, jsonify
import geopy.distance

app = Flask(__name__)

# 假設計程車費用為每公尺 $5
TAXI_RATE_PER_M = 5

def calculate_distance(start_coordinates, end_coordinates):
    # 使用 geopy 库计算两个坐標點之间的实际距离
    return geopy.distance.distance(start_coordinates, end_coordinates).m

def calculate_taxi_fare(distance_in_meters):
    # 假設計程車每公尺收費 $5，則計算車費
    return int(distance_in_meters * TAXI_RATE_PER_M /100)

@app.route('/')
def index():
    google_maps_api_key = "AIzaSyDrhi06AlU3qplUYFXA4PtNerrYklmMINk"  # 將這裡替換成您的 Google Maps API 金鑰
    return render_template('map.html', api_key=google_maps_api_key)

@app.route('/calculate_distance/<string:start_lat>/<string:start_lng>/<string:end_lat>/<string:end_lng>')
def calculate_distance_route(start_lat, start_lng, end_lat, end_lng):
    start_lat = float(start_lat)
    start_lng = float(start_lng)
    end_lat = float(end_lat)
    end_lng = float(end_lng)

    start_coordinates = (start_lat, start_lng)
    end_coordinates = (end_lat, end_lng)
    
    # 計算實際道路距離
    distance_in_meters = calculate_distance(start_coordinates, end_coordinates)

    # 計算車費
    taxi_fare = calculate_taxi_fare(distance_in_meters)

    return jsonify({'distance': round(distance_in_meters, 2), 'taxi_fare': taxi_fare+90})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
