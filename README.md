# Ohio DOT Camera and Incident Mapper 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![dotenv](https://img.shields.io/badge/dotenv-000000?style=for-the-badge&logo=dotenv&logoColor=green) ![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=python&logoColor=white) [![OHGO API](https://img.shields.io/badge/OHGO_API-28A745?style=for-the-badge&logoColor=white)](https://www.ohgo.com)


<p align="center">
  <img src="https://github.com/ericmaddox/odot-camera-and-incident-mapper/blob/main/media/odot_image_camera.JPG" width="300" />
  <img src="https://github.com/ericmaddox/odot-camera-and-incident-mapper/blob/main/media/odot_image_incident.JPG" width="320" />
</p>


## Description
`ODOT Camera and Incident Mapper` is a Python script that fetches camera and incident data from the Ohio Department of Transportation (ODOT) API, and visualizes the data on an interactive map using the Folium library. This tool helps monitor highway conditions and visualize traffic incidents in Ohio.

## Features
- Fetch camera data from [ODOT API](https://www.ohgo.com/) ([Camera Data Documentation](https://publicapi.ohgo.com/docs/v1/cameras)).
- Fetch incident data (accidents) from [ODOT API](https://www.ohgo.com/) ([Incident Data Documentation](https://publicapi.ohgo.com/docs/v1/incidents)).
- Visualize cameras and incidents on an interactive map.
- Use environment variables to store API keys securely.

## Prerequisites
- Python 3.x
- `requests` library
- `folium` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/odot-camera-and-incident-mapper.git
    cd odot-camera-and-incident-mapper
    ```

2. Install the required libraries:
    ```bash
    pip install requests folium python-dotenv
    ```

3. Create a `.env` file in the root directory and add your ODOT API key:
    ```env
    OHGO_API_KEY=your_api_key_here
    ```

## Usage

1. Run the script:
    ```bash
    python odot_camera_and_incident_mapper.py
    ```

2. The script will fetch camera and incident data, and save the generated map as `ohgo_cameras_incidents_map.html`.

## Script Details

### Fetching Data
- The script fetches camera data using the provided [ODOT API](https://www.ohgo.com/) URLs ([Camera Data Documentation](https://publicapi.ohgo.com/docs/v1/cameras)).
- The script fetches incident data using the provided [ODOT API](https://www.ohgo.com/) URLs ([Incident Data Documentation](https://publicapi.ohgo.com/docs/v1/incidents)).
- It handles pagination to ensure all data is retrieved.

### Plotting Data on Map
- Cameras are plotted on the map with blue markers.
- Incidents are plotted on the map with red markers.
- Detailed information is provided in the popups for each marker.

## Files
- `odot_camera_and_incident_mapper.py`: The main script file.
- `.env`: File to store environment variables (not included in version control).
- `ohgo_cameras_incidents_map.html`: The generated map file.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy mapping!
