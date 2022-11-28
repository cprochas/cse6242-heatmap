import pandas as pd
from flask import Flask, render_template, request, flash
from folium import Map
from folium.plugins import HeatMap

app = Flask(__name__)
app.secret_key = "cse6242"
data = pd.read_csv('US_Accidents_Dec21_updated.csv')


@app.route("/")
def index():
    accident_map = Map(
        location=[33.7488, -84.3877],
        zoom_start=8,
        tiles='OpenStreetMap'
    )
    accident_map.save("templates/maps.html")
    return render_template("index.html")

@app.route('/maps', methods=["POST", "GET"])
def maps():
    # severity_level = str(request.form['severity1'])
    # filtered_data = data[data.Severity == severity_level]
    filtered_data = data[data.Severity == 1]
    accident_map_f = Map(
        location=[33.7488, -84.3877],
        zoom_start=8,
        tiles='OpenStreetMap'
    )
    coordinates_f = list(map(list, zip(filtered_data['Start_Lat'][:1000], filtered_data['Start_Lng'][:1000])))
    HeatMap(coordinates_f).add_to(accident_map_f)
    accident_map_f.save('templates/maps.html')
    return render_template('maps.html')

#
#
# # @app.route("/heatmap", methods=["POST", "GET"])
# # def filter():
# #     flash("Sev level: " +str(request.form['severity1']))
# #
# #     return render_template("index.html")
#
#
#
# # add filters
#
# # severity level
# # weather
# # time of day
# # year
#
#
if __name__ == '__main__':
    app.run(debug=True)
