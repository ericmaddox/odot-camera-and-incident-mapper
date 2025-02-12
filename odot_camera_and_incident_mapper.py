import os
import requests
import folium
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('OHGO_API_KEY')

# API URLs for fetching camera and incident data
CAMERA_API_URL = 'https://publicapi.ohgo.com/api/v1/cameras'
INCIDENT_API_URL = 'https://publicapi.ohgo.com/api/v1/incidents'

# Pagination setup
PAGE_SIZE = 20000
PAGE = 1
TOTAL_PAGES = 1

# Function to fetch camera data
def fetch_camera_data(page=1):
    response = requests.get(
        CAMERA_API_URL,
        headers={'Authorization': f'APIKEY {api_key}'},
        params={'page': page, 'page-size': PAGE_SIZE}
    )
    
    if response.status_code == 200:
        data = response.json()
        cameras = data.get('results', [])
        return cameras, data
    else:
        print(f"Error fetching camera data: {response.status_code}")
        return [], None

# Function to fetch incident data
def fetch_incident_data(page=1):
    response = requests.get(
        INCIDENT_API_URL,
        headers={'Authorization': f'APIKEY {api_key}'},
        params={
            'page': page,
            'page-size': PAGE_SIZE,
            'incidentType': 'accident',
            'status': 'active'
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        incidents = data.get('results', [])
        return incidents, data
    else:
        print(f"Error fetching incident data: {response.status_code}")
        return [], None

# Fetch all cameras with pagination
def fetch_all_camera_data():
    global PAGE, TOTAL_PAGES
    PAGE = 1  # Reset PAGE
    TOTAL_PAGES = 1  # Reset TOTAL_PAGES
    
    all_cameras = []
    
    while PAGE <= TOTAL_PAGES:
        cameras, data = fetch_camera_data(PAGE)
        
        if cameras:
            all_cameras.extend(cameras)
            print(f"Fetched page {PAGE} with {len(cameras)} cameras.")
            
            if data:
                TOTAL_PAGES = data.get('totalPageCount', 1)
            
            PAGE += 1
        else:
            break

    return all_cameras

# Fetch all incidents with pagination
def fetch_all_incident_data():
    global PAGE, TOTAL_PAGES
    PAGE = 1  # Reset PAGE
    TOTAL_PAGES = 1  # Reset TOTAL_PAGES
    
    all_incidents = []
    
    while PAGE <= TOTAL_PAGES:
        incidents, data = fetch_incident_data(PAGE)
        
        if incidents:
            all_incidents.extend(incidents)
            print(f"Fetched page {PAGE} with {len(incidents)} incidents.")
            
            if data:
                TOTAL_PAGES = data.get('totalPageCount', 1)
            
            PAGE += 1
        else:
            break

    return all_incidents

# Create map and plot cameras and incidents
def plot_on_map(cameras, incidents):
    map = folium.Map(location=[39.8283, -82.6272], zoom_start=6)

    # Plot cameras (blue markers)
    for camera in cameras:
        latitude = camera.get('latitude')
        longitude = camera.get('longitude')
        location = camera.get('location')
        description = camera.get('description')
        camera_views = camera.get('cameraViews', [])
        
        if latitude and longitude:
            camera_data = f"""
            <b>{location}</b><br>
            <b>Description:</b> {description}<br>
            <b>Camera Views:</b><br>
            """
            for view in camera_views:
                camera_data += f"Direction: {view.get('direction', 'Unknown')}<br>"
                camera_data += f"Small Image: <img src='{view.get('smallUrl', 'No URL available')}' width='100'><br>"
                camera_data += f"Large Image: <img src='{view.get('largeUrl', 'No URL available')}' width='200'><br>"
                camera_data += f"Main Route: {view.get('mainRoute', 'No route information')}<br>"
            
            folium.Marker(
                location=[latitude, longitude],
                popup=folium.Popup(camera_data, max_width=400),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(map)

    # Plot incidents (red markers)
    for incident in incidents:
        latitude = incident.get('latitude')
        longitude = incident.get('longitude')
        description = incident.get('description')
        
        if latitude and longitude:
            incident_data = f"""
            <b>Description:</b> {description}<br>
            """
            folium.Marker(
                location=[latitude, longitude],
                popup=folium.Popup(incident_data, max_width=400),
                icon=folium.Icon(color='red', icon='exclamation-sign')
            ).add_to(map)

    map.save('ohgo_cameras_incidents_map.html')
    print("Map saved as ohgo_cameras_incidents_map.html")

# Main function
if __name__ == '__main__':
    print("Fetching camera data...")
    cameras = fetch_all_camera_data()

    print("Fetching incident data...")
    incidents = fetch_all_incident_data()

    if cameras or incidents:
        print(f"Total cameras fetched: {len(cameras)}")
        print(f"Total incidents fetched: {len(incidents)}")
        plot_on_map(cameras, incidents)
    else:
        print("No camera or incident data found.")
