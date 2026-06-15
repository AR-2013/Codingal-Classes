import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error! The file 'imdb_top_1000.csv' was not found.")
    raise SystemExit

# Extract unique genres cleanly
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    for _ in range(3): 
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print()

def get_sentiment(p):
    if p > 0:
        return "Positive 😀"
    elif p < 0:
        return "Negative 🥺"
    else:
        return "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df.copy()
    
    # Filter by genre if provided
    if genre:
        d = d[d["Genre"].str.contains(genre, case=False, na=False)]
        
    # Filter by minimum IMDB rating if provided
    if rating is not None:
        d = d[d["IMDB_Rating"] >= float(rating)]
        
    if d.empty:
        return None
        
    # Shuffle the dataset and set up conditions
    d = d.sample(frac=1).reset_index(drop=True)
    need_nonneg = bool(mood)  # If mood is specified, prefer positive sentiment overview
    out = []
    
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): 
            continue
            
        pol = TextBlob(ov).sentiment.polarity
        
        # If mood is requested, ensure the overview sentiment is non-negative (>= 0)
        if (not need_nonneg) or pol >= 0:
            title = r.get("Series_Title", "Unknown Title")
            genre_val = r.get("Genre", "N/A")
            rating_val = r.get("IMDB_Rating", "N/A")
            sentiment_label = get_sentiment(pol)
            
            out.append({
                "title": title,
                "genre": genre_val,
                "rating": rating_val,
                "sentiment": sentiment_label
            })
            
            if len(out) == n: 
                break
                
    return out if out else None

def show(recs, search_criteria):
    if not recs:
        print(Fore.RED + f"\nNo suitable movie recommendations found for {search_criteria}.")
        return
        
    print(Fore.YELLOW + f"\n🍿 AI analysed movie recommendations for: {search_criteria} 🍿")
    for i, movie in enumerate(recs, 1):
        print(f"\n{Fore.CYAN}[{i}] {movie['title']}")
        print(f"   {Fore.WHITE}• Genre: {movie['genre']}")
        print(f"   {Fore.WHITE}• IMDB Rating: {movie['rating']}")
        print(f"   {Fore.WHITE}• Overview Sentiment: {movie['sentiment']}")

# --- CLI / Interactive Loop ---
def main():
    print(Fore.GREEN + "=========================================")
    print(Fore.GREEN + "       AI Movie Recommendation System     ")
    print(Fore.GREEN + "=========================================")
    
    while True:
        print(Fore.WHITE + "\nSelect an option:")
        print("1. Get recommendations based on Genre/Mood/Rating")
        print("2. Exit")
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            genre_input = input("Enter Genre (e.g., Drama, Action) or press Enter to skip: ").strip()
            genre_filter = genre_input if genre_input != "" else None
            
            mood_input = input("Do you want a 'positive' mood/vibes? (yes/no): ").strip().lower()
            mood_filter = True if mood_input == 'yes' else None
            
            rating_input = input("Enter minimum IMDB Rating (e.g., 7.5) or press Enter to skip: ").strip()
            rating_filter = float(rating_input) if rating_input != "" else None
            
            print(Fore.YELLOW + "Fetching recommendations", end="")
            dots()
            
            recs = recommend(genre=genre_filter, mood=mood_filter, rating=rating_filter, n=5)
            
            criteria_desc = f"Genre: {genre_filter or 'Any'}, Positive Mood: {bool(mood_filter)}, Min Rating: {rating_filter or 'None'}"
            show(recs, criteria_desc)
            
        elif choice == '2':
            print(Fore.GREEN + "\nThank you for using the AI Movie Recommendation System! Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()