import csv
import requests
import time

API_KEY = 'a393d224'  # Please replace with your OMDb API key

def fetch_top_250_ids():
    # Predefined list of IMDb Top 250 movie IDs
    top_250_ids = [
        "tt0111161", "tt0068646", "tt0071562", "tt0468569", "tt0050083",
        "tt0108052", "tt0167260", "tt0110912", "tt0060196", "tt0120737",
        "tt0109830", "tt1375666", "tt0167261", "tt0080684", "tt0137523",
        "tt0102926", "tt0038650", "tt0054215", "tt0120815", "tt0081505",
        "tt0099685", "tt0073486", "tt0047478", "tt0114369", "tt0076759",
        "tt0118799", "tt0120586", "tt0078788", "tt0034583", "tt0253474",
        "tt0086190", "tt0103064", "tt0056058", "tt0211915", "tt0110413",
        "tt0095765", "tt0021749", "tt0105236", "tt1211837", "tt0082971",
        "tt0105695", "tt0095327", "tt0087843", "tt0043014", "tt0037884",
        "tt0169547", "tt0080745", "tt0075148", "tt0044079", "tt0032553",
        "tt0050825", "tt0032138", "tt0081398", "tt0056592", "tt0051201",
        "tt0112573", "tt0095327", "tt0209163", "tt0064116", "tt0114709",
        "tt0089881", "tt0049366", "tt0047296", "tt0012349", "tt8041270",
        "tt0075314", "tt0021749", "tt0095327", "tt0172495", "tt0133093", "tt0114814", "tt0107290", "tt0119698",
        "tt0045152", "tt0053125", "tt0062622", "tt0066921", "tt0070735",
        "tt0317248", "tt0405508", "tt0361748", "tt0347149", "tt0266543",
        "tt0082690", "tt0116282", "tt0266697", "tt0993846", "tt0434409",
        "tt0119217", "tt0361748", "tt0978762", "tt1853728", "tt0172493",
        "tt0469494", "tt0090605", "tt0198781", "tt0242519", "tt0097576",
        "tt0353969", "tt0116231", "tt0118849", "tt0120177", "tt0029583",
        "tt0245712", "tt0435761", "tt0139239", "tt0947810", "tt1130884",
        "tt1305806", "tt0476964", "tt0118715", "tt0119488", "tt0319061",
        "tt0167404", "tt0363163", "tt0077416", "tt0091763", "tt0070047",
        "tt0177944", "tt0457430", "tt0050212", "tt0758758", "tt0116136",
        "tt0118694", "tt0892769", "tt1291584", "tt0113277", "tt1145857",
        "tt1201607", "tt0120815", "tt1950186", "tt1895587", "tt1659337",
        "tt0338013", "tt0268978", "tt2084970", "tt2278388", "tt1028532",
        "tt0180093", "tt0372784", "tt0264464", "tt0491203", "tt0358273",
        "tt0477348", "tt0165831", "tt0161262", "tt0387898", "tt0120735",
        "tt0315733", "tt0430674", "tt0457429", "tt0414993", "tt0162661",
        "tt0413267", "tt0265086", "tt0367652", "tt0303461", "tt0354549",
        "tt0181875", "tt0816442", "tt0790636", "tt2278443", "tt2267998",
        "tt0040897", "tt0053604", "tt0055630", "tt0055031", "tt0036868",
        "tt0040522", "tt0040897", "tt0045152", "tt0046911", "tt0050212",
        "tt0050976", "tt0052357", "tt0055630", "tt0089881", "tt0090605",
        "tt0093407", "tt0097059", "tt0097576", "tt0107207", "tt0110413",
        "tt0116231", "tt0118694", "tt0119488", "tt0120735", "tt0121765",
        "tt0139239", "tt0153930", "tt0167404", "tt0180093", "tt0182245",
        "tt0187664", "tt0192445", "tt0198781", "tt0204946", "tt0209163",
        "tt0212346", "tt0241527", "tt0244316", "tt0245712", "tt0266697",
        "tt0268978", "tt0289879", "tt0295178", "tt0303461", "tt0325980",
        "tt0330373", "tt0338013", "tt0347149", "tt0363163", "tt0367652",
        "tt0372784", "tt0387898", "tt0405508", "tt0414993", "tt0434409",
        "tt0476964", "tt0491203", "tt0816442", "tt0892769", "tt0978762",
        "tt1028532", "tt1130884", "tt1145857", "tt1291584", "tt1305806",
        "tt1381404", "tt1500187", "tt1659337", "tt1853728", "tt1895587",
        "tt1950186", "tt2084970", "tt2278388", "tt2278443", "tt2267998",
        "tt0117014", "tt0107846", "tt1392214", "tt0107456", "tt0046268",
        "tt0074958", "tt0081622", "tt3315342", "tt0061184", "tt0092005",
        "tt0382932"
    ]
    return top_250_ids

def fetch_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=short&r=json"
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('Response') == 'True':
                    return {
                        'Title': data.get('Title', 'N/A'),
                        'Year': data.get('Year', 'N/A'),
                        'Rating': data.get('imdbRating', 'N/A'),
                        'Director': data.get('Director', 'N/A')
                    }
                else:
                    print(f"Error: {data.get('Error')} (ID: {imdb_id})")
            else:
                print(f"Attempt {attempt + 1}/{max_retries} failed, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed, exception: {e}")

        time.sleep(retry_delay)
    return None

def scrape_imdb():
    top_250_ids = fetch_top_250_ids()
    movie_data = []

    for imdb_id in top_250_ids:
        details = fetch_movie_details(imdb_id)
        if details:
            movie_data.append([
                details['Title'],
                details['Rating'],
                details['Director'],
                details['Year']
            ])
            print(f"Fetched: {details['Title']}")
        else:
            print(f"Failed to get data for ID {imdb_id}")

    # Save as CSV file
    with open('imdb_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Rating', 'Director', 'Year'])
        writer.writerows(movie_data)

    print("IMDb data has been saved as imdb_data.csv")

if __name__ == '__main__':
    scrape_imdb()