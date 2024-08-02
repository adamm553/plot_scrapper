import requests
import csv

def fetch_parcel_data(city, parcel_number):
    url = f"https://uldk.gugik.gov.pl/?request=GetParcelByIdOrNr&id={city} {parcel_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        response_text = response.text.strip()
        
        if response_text == "-1":
            return {'city': city, 'parcel_number': parcel_number, 'data': '-1'}
        else:
            return {
                'city': city,
                'parcel_number': parcel_number,
                'data': response_text
            }
    else:
        return {'city': city, 'parcel_number': parcel_number, 'data': '-1'}

def scrape_data(cities, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['city', 'parcel_number', 'data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for city in cities:
            parcel_number = 1  
            
            while True:
                data = fetch_parcel_data(city, parcel_number)
                
                if data['data'] != '-1':
                    print("Data Found:")
                    print(f"City: {data['city']}")
                    print(f"Parcel Number: {data['parcel_number']}")
                    print(f"Data: {data['data']}")
                    
                    writer.writerow(data)
                    
                    parcel_number += 1
                else:
                    print(f"Data not found for Parcel Number {parcel_number} in City {city}. Trying next parcel number...")
                    parcel_number += 1 
                
            print(f"Finished checking for city: {city}\n")
    
    print("Finished checking all cities.")

def main():
    cities = ['Stara Wieś']  # Update with your city names
    
    output_file = 'parcel_data.csv'

    scrape_data(cities, output_file)

if __name__ == "__main__":
    main()
