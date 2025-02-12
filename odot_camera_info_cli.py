import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("OHGO_API_KEY")

# API endpoint URL
API_URL = "https://publicapi.ohgo.com/api/v1/cameras"

# Set the region filter (modify based on your preference, e.g., "cleveland")
REGION = "cleveland"

# Set pagination size
PAGE_SIZE = 50
PAGE = 1  # Start from page 1

def fetch_camera_data():
    if not API_KEY:
        print("Error: API key not found in environment variables.")
        return
    
    # Set the authorization header
    headers = {
        'Authorization': f"APIKEY {API_KEY}"
    }
    
    # Set query parameters with region filter and pagination
    params = {
        'region': REGION,  # You can change this to another region or a list of regions
        'page-size': PAGE_SIZE,
        'page': PAGE
    }
    
    # Send GET request to the OHGO API with the authorization header and query parameters
    response = requests.get(API_URL, headers=headers, params=params)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        try:
            # Parse JSON response
            data = response.json()

            # Check if 'results' is present and it's a list
            if 'results' in data and isinstance(data['results'], list):
                cameras = data['results']
                print(f"Total Cameras Found: {len(cameras)}")
                
                # Iterate through the cameras and print details
                for camera in cameras:
                    if isinstance(camera, dict):
                        print(f"Camera ID: {camera.get('id', 'N/A')}")
                        print(f"Location: {camera.get('location', 'N/A')}")
                        print(f"Latitude: {camera.get('latitude', 'N/A')}")
                        print(f"Longitude: {camera.get('longitude', 'N/A')}")
                        print(f"Description: {camera.get('description', 'N/A')}")

                        # Check if 'cameraViews' exists and is a list
                        if 'cameraViews' in camera and isinstance(camera['cameraViews'], list):
                            for view in camera['cameraViews']:
                                if isinstance(view, dict):
                                    print(f"    Camera View Direction: {view.get('direction', 'N/A')}")
                                    print(f"    Small Image URL: {view.get('smallUrl', 'N/A')}")
                                    print(f"    Large Image URL: {view.get('largeUrl', 'N/A')}")
                                    print(f"    Main Route: {view.get('mainRoute', 'N/A')}")
                                    print("=" * 40)
                        else:
                            print("    No camera views found.")
            else:
                print("No camera data found in the response.")
        except ValueError:
            print("Error: Unable to parse JSON response.")
    elif response.status_code == 401:
        # Handle unauthorized errors by displaying the error message
        print("Error: Unauthorized request. Please check your API key.")
        try:
            error_data = response.json()
            if 'errorDescription' in error_data:
                print(f"Error Description: {error_data['errorDescription']}")
        except ValueError:
            print("Error: Unable to parse error response.")
    else:
        # Handle other status codes and errors
        print(f"Error: Unable to fetch camera data. Status code {response.status_code}")
        try:
            error_data = response.json()
            if 'errorDescription' in error_data:
                print(f"Error Description: {error_data['errorDescription']}")
        except ValueError:
            print("Error: Unable to parse error response.")

if __name__ == "__main__":
    fetch_camera_data()
