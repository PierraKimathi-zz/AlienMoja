from flask import Flask
from flask import render_template
import csv
import string
import json
import folium

app = Flask('_name_')
app.debug = True

gps_list = []

@app.route('/')
def read_csv():

	m = folium.Map(
    location=[1.2921, 36.8219],
    zoom_start=20,
	) 

	with open('Device+GPS.csv') as csv_file:

	    csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
	    
	    line_count = 0

	    for row in csv_reader:
			folium.Marker(
    		location=[float(row['lat'].replace('\'','')),float(row['lng'])],
    		popup='SB location',
    		icon=folium.Icon(icon='cloud')
		).add_to(m)

	m.save('index.html')
	m