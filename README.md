# Starlink-Latency-Analysis

## Project Overview
**Collaborators:** Harris Greenstein, Maheer Aeron, Matthew Cafiero, Joshua Church, and Skyler Krouse.

### Project Goal
The primary objective was to analyze the variability in the latency of Starlink's satellite network across different times and locations. Utilizing RIPE Atlas probes connected to Starlink terminals, we systematically pinged these probes to a common site over a 24-hour period, aiming to understand the factors influencing latency.

### Key Findings from the Report

- **Inefficient Ground Station Routing:** Satellites could often be found connnecting to ground stations over 2,500 miles further than the nearest station especially in areas like Alaska that would heavily benefit from this service. The latency differences when routing inefficiently caused significant and measureable latency.
- **Geographical Variability:** Significant differences in latency were observed based on the probe's location, with rural areas generally exhibiting higher latencies.
- **Lack of Transparency:** Starlink's marketing does not adequately communicate the variability and potential inconsistencies in services and at the time of the project labeled the entire United States as equal and adequate coverage. The outliers observed in rural areas and Alaska call for a significant improvement in transparency of service expectations based on much finer regional information than country-wide. 
- **Inconsistent with Promises:** The advertised latency of 25 ms was rarely met across the network, with most probes not reaching this figure at any point.


## Full Report
- **Access the Report:** [Available Here](https://harrisgreenstein.com/assets/starlinkReport-65588e38.pdf)

## Installation and Running Guide

### Prerequisites
- Python 3.x
- Requests library (`pip install requests`)
- Folium library for `map.py` (`pip install folium`)

### Setting Up Your Environment
1. **Clone the Repository:** Download the project files from the GitHub repository.

   ```bash
   git clone https://github.com/hgreenstein/Starlink-Latency-Analysis.git
   ```
2. **Install Dependencies:** Ensure Python 3.x is installed, and install the required Python libraries.
   
    ```bash
    pip install requests
    pip install folium  # Required for map.py
    ```
### Configuring and Running Scripts

#### `starlinkProbes.py`
- **Purpose:** Fetches all online RIPE Atlas probes for a specific ASN (Autonomous System Number), such as 14593 for Starlink.
- **Running the Script:**
  1. Run `python starlinkProbes.py`.
  2. The script will output the ID, country code, and description of each connected Starlink probe.
  3. It also prints the total number of connected Starlink probes at the end.

#### `measurements.py`
- **API Key:** Add your RIPE Atlas API key in `measurements.py`. Replace `{Redacted For Security}` with your key.
- **Running the Script:**
  - **Ping Measurements:**
    1. Uncomment the `startMeasurement` function call at the bottom of `measurements.py`.
    2. Input the probe IDs of your choice.
    3. Run `python measurements.py` to start the ping measurements.
  - **Traceroute Analysis:**
    1. Uncomment the `startTraceroute` function call.
    2. Input the probe IDs as with the ping measurements.
    3. Run `python measurements.py` to execute traceroute analysis.
  - **Fetching Results:**
    1. Uncomment `getResults` and input the measurement ID.
    2. Run `python measurements.py` to retrieve results.

### Running `map.py`
- Run `python map.py` to generate a map visualization of probe locations using Folium. Ensure you have the necessary data for mapping.

### Additional Information
- The `measurements.py` script contains various scenarios for running measurements (e.g., 24-hour pings, shorter period pings, traceroutes). These are all commented out at the bottom of the file. Based on your requirements, uncomment the appropriate lines and run the script as mentioned above.
- For further details on each function and how to modify the scripts for different scenarios, refer to the comments within the scripts and the full project report.

### Important Files

#### [starlinkProbes.py](/starlinkProbes.py)
Retrieves all available RIPE Atlas probes matching Starlink's IPv4 addresses. The script was critical in establishing the base dataset for our analysis, as detailed in the 'Methodology' section of the report.

#### [measurements.py](/measurements.py)
Handles multiple key aspects of data collection and analysis:
- **Ping Tests:** Conducts regular ping requests every 15 minutes for a 24-hour cycle, as outlined in the 'Data Collection' section of the report.
- **Traceroute Analysis:** Performs traceroutes to bing.com to assess latency factors, explained in the 'Analysis' chapter of the report.
- **Data Correlation:** Correlates measurements with satellite positions, aiding in the interpretation of latency variations, as discussed in the 'Results' section.

#### [map.py](/map.py)
Used to generate visual maps of probe locations using Folium. This script was instrumental in visualizing the geographical distribution of latency, which is a key aspect of the 'Geographic Analysis' section in the report.

## Conclusions
Our analysis highlights the need for improved transparency from Starlink regarding the performance of their network, especially in terms of latency variability and the factors affecting it. The complete findings, along with the methodology and detailed data, are available in the full report.
