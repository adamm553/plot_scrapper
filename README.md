Parcel Data Scraper
===================

Overview
--------

This Python script is designed to scrape parcel data from the [ULDK GUGiK website](https://uldk.gugik.gov.pl) based on city names and parcel numbers. It fetches data for parcel numbers starting from 1 and continues until a `"-1"` response is received, indicating that no more data is available for that city. The retrieved data is saved into a CSV file.

Requirements
------------

-   Python 3.x
-   `requests` library (for making HTTP requests)
-   `csv` module (standard library for CSV file handling)

You can install the required library using pip if it's not already installed:

`pip install requests`

Script Functions
----------------

### `fetch_parcel_data(city, parcel_number)`

-   **Description**: Fetches parcel data from the ULDK GUGiK API for a given city and parcel number.
-   **Parameters**:
    -   `city` (str): The name of the city.
    -   `parcel_number` (int): The parcel number to query.
-   **Returns**: A dictionary containing:
    -   `city`: The city name.
    -   `parcel_number`: The queried parcel number.
    -   `data`: The response data from the API. If no data is found, it returns `'-1'`.

### `scrape_data(cities, output_file)`

-   **Description**: Scrapes data for each city and writes the results to a CSV file.
-   **Parameters**:
    -   `cities` (list): A list of city names to query.
    -   `output_file` (str): The name of the CSV file where data will be saved.

### `main()`

-   **Description**: Defines the list of cities and the output file name, then calls `scrape_data` to perform the scraping operation.

Usage
-----

1.  **Modify the Script**: Update the `cities` list in the `main()` function to include the names of the cities you want to scrape.

2.  **Run the Script**: Execute the script using Python:

    `python script_name.py`

    Replace `script_name.py` with the filename of your script.

3.  **Check the Output**: The script will generate a CSV file named `data.csv` (or whatever name you specify) in the same directory. This file will contain the scraped parcel data.

Example
-------

If the `cities` list in the `main()` function is set to `['Stara Wieś']`, the script will:

-   Query parcel numbers starting from 1 for the city "Stara Wieś".
-   Continue querying until it receives a `"-1"` response.
-   Save all retrieved data into `data.csv`.

Notes
-----

-   Ensure you have the correct permissions and API access to use the ULDK GUGiK API.
-   The script assumes that the response from the API will be in text format. Adjust parsing as necessary if the API response format changes.
