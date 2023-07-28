import csv
import requests
print('List with duplicates')

url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = [recording["sp"] for recording in data["recordings"]]
        print(species_list)
else:
    print("Error.")


print('List without duplicates')


url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"]
                            for recording in data["recordings"]})
        print(species_list)
else:
    print("Error.")


print(' List without duplicates in the csv file')


url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"]
                            for recording in data["recordings"]})

        # Specify the file path for the CSV file
        csv_file_path = "species_list.csv"

        # Write the species_list to the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Species"])  # Write header row
            # Write species names row by row
            writer.writerows([[species] for species in species_list])

        print("Success.")
else:
    print("Error.")
