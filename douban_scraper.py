import requests
from bs4 import BeautifulSoup
import csv
import re
import time


def get_english_title(info_text):
    # Match English title: usually within parentheses after the first Chinese title or other titles
    eng_title_match = re.search(r'(?<=\s)([A-Za-z0-9\s:\'\",.&!-]+)(?=\s|$|\()', info_text)
    if eng_title_match:
        return eng_title_match.group(1).strip()
    return None


def clean_director_name(director):
    # Extract the English name of the director
    eng_name_match = re.search(r'([A-Za-z\s.-]+)', director)
    if eng_name_match:
        return eng_name_match.group(1).strip()
    return director


def scrape_douban():
    url = "https://movie.douban.com/top250"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    movie_data = []

    for page in range(0, 10):
        try:
            response = requests.get(f"{url}?start={page * 25}", headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue

        for movie in soup.find_all('div', class_='item'):
            try:
                # Get all title information
                title_element = movie.find('div', class_='hd')
                all_titles = [t.text.strip() for t in title_element.find_all('span', class_='title')]
                other_title = movie.find('span', class_='other').text if movie.find('span', class_='other') else ''

                # Get rating
                rating = movie.find('span', class_='rating_num').text

                # Get detailed information
                info = movie.find('div', class_='bd').p.text.strip()

                # Extract English title
                english_title = None
                # First check if there's English in other titles
                eng_title_match = get_english_title(other_title)
                if eng_title_match:
                    english_title = eng_title_match
                # If not found, search in detailed information
                if not english_title:
                    eng_title_match = get_english_title(info)
                    if eng_title_match:
                        english_title = eng_title_match

                # If still not found, use the first title
                if not english_title:
                    english_title = all_titles[0]

                # Extract director
                director_match = re.search(r'Director: ([^\\n]*?)(?=\s+Starring|$)', info)
                director = director_match.group(1).strip() if director_match else 'Unknown'
                director = clean_director_name(director)

                # Extract year
                year_match = re.search(r'(\d{4})', info)
                year = year_match.group(1) if year_match else 'Unknown'

                movie_data.append([english_title, rating, director, year])
                print(f"Fetched: {english_title}")

            except AttributeError as e:
                print(f"Parsing error: {e}")
                continue

        time.sleep(2)  # Increase delay to 2 seconds to avoid being blocked

    # Save as CSV file
    try:
        with open('douban_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Rating', 'Director', 'Year'])
            writer.writerows(movie_data)
        print("Douban data has been saved as douban_data.csv")
    except IOError as e:
        print(f"File write failed: {e}")


if __name__ == '__main__':
    scrape_douban()