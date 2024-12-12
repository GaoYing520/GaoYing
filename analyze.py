import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Chinese font display
plt.rcParams['font.sans-serif'] = ['SimHei']  # For displaying Chinese labels correctly
plt.rcParams['axes.unicode_minus'] = False  # For displaying minus signs correctly


def load_data():
    """Load datasets from IMDb and Douban"""
    douban_df = pd.read_csv('douban_data.csv')
    imdb_df = pd.read_csv('imdb_data.csv')
    return douban_df, imdb_df


def compare_average_ratings(douban_df, imdb_df):
    """Compare average ratings between IMDb and Douban"""
    douban_avg = douban_df['Rating'].astype(float).mean()
    imdb_avg = imdb_df['Rating'].astype(float).mean()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=['Douban', 'IMDb'], y=[douban_avg, imdb_avg], palette='viridis')
    plt.title('Comparison of Average Ratings between IMDb and Douban')
    plt.ylabel('Average Rating')
    plt.ylim(0, 10)
    for index, value in enumerate([douban_avg, imdb_avg]):
        plt.text(index, value + 0.1, f'{value:.2f}', ha='center')
    plt.show()


def find_overlapping_movies(douban_df, imdb_df):
    """Find movies that appear on both platforms"""
    douban_titles = set(douban_df['Title'])
    imdb_titles = set(imdb_df['Title'])
    overlap = douban_titles.intersection(imdb_titles)
    print(f"Number of overlapping movies: {len(overlap)}")
    print("List of overlapping movies:")
    for title in overlap:
        print(title)


def analyze_release_year_distribution(douban_df, imdb_df):
    """Analyze distribution of release years"""
    plt.figure(figsize=(12, 6))
    sns.histplot(douban_df['Year'], color='blue', label='Douban', kde=True, stat="density", linewidth=0)
    sns.histplot(imdb_df['Year'], color='red', label='IMDb', kde=True, stat="density", linewidth=0)
    plt.title('Comparison of Release Year Distribution between IMDb and Douban')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


def compare_genre_distributions(douban_df, imdb_df):
    """Compare genre distributions"""

    # Assuming the dataset has a 'Genre' column
    def preprocess_genres(df):
        genres = df['Genre'].dropna().str.split('/')
        genres = genres.explode()
        genres = genres.str.strip()
        return genres

    douban_genres = preprocess_genres(douban_df)
    imdb_genres = preprocess_genres(imdb_df)

    top_douban = douban_genres.value_counts().head(10)
    top_imdb = imdb_genres.value_counts().head(10)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.barplot(x=top_douban.values, y=top_douban.index, ax=axes[0], palette='Blues_d')
    axes[0].set_title('Top 10 Genres in Douban Movies')
    axes[0].set_xlabel('Count')
    axes[0].set_ylabel('Genre')

    sns.barplot(x=top_imdb.values, y=top_imdb.index, ax=axes[1], palette='Reds_d')
    axes[1].set_title('Top 10 Genres in IMDb Movies')
    axes[1].set_xlabel('Count')
    axes[1].set_ylabel('Genre')

    plt.tight_layout()
    plt.show()


def identify_top_directors(douban_df, imdb_df):
    """Identify Top 10 Directors with the most appearances"""
    douban_directors = douban_df['Director'].dropna().str.split('/').explode().str.strip()
    imdb_directors = imdb_df['Director'].dropna().str.split(',').explode().str.strip()

    top_douban_directors = douban_directors.value_counts().head(10)
    top_imdb_directors = imdb_directors.value_counts().head(10)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.barplot(x=top_douban_directors.values, y=top_douban_directors.index, ax=axes[0], palette='Greens_d')
    axes[0].set_title('Top 10 Directors in Douban')
    axes[0].set_xlabel('Number of Appearances')
    axes[0].set_ylabel('Director')

    sns.barplot(x=top_imdb_directors.values, y=top_imdb_directors.index, ax=axes[1], palette='Oranges_d')
    axes[1].set_title('Top 10 Directors in IMDb')
    axes[1].set_xlabel('Number of Appearances')
    axes[1].set_ylabel('Director')

    plt.tight_layout()
    plt.show()


def main():
    douban_df, imdb_df = load_data()
    compare_average_ratings(douban_df, imdb_df)
    find_overlapping_movies(douban_df, imdb_df)
    analyze_release_year_distribution(douban_df, imdb_df)
    compare_genre_distributions(douban_df, imdb_df)
    identify_top_directors(douban_df, imdb_df)


if __name__ == "__main__":
    main()