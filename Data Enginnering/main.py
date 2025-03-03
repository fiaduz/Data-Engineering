import pandas as pd

def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def preprocess_data(df):
    df = df.drop_duplicates()

    columns = ['City', 'Name', 'Google review rating', 'time needed to visit in hrs', 
               'Entrance Fee in INR', 'Number of google review in lakhs']
    
    if not all(col in df.columns for col in columns):
        raise ValueError("Missing required columns in dataset.")


    for col in columns[2:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df.dropna()

def rank_places(df, city):
    city_data = df[df['City'].str.lower() == city.lower()].copy()

    if city_data.empty:
        return f"No travel places found in {city}."

    city_data['Score'] = (
        (city_data['Google review rating'] / city_data['Google review rating'].max()) * 0.4 +
        (1 - city_data['time needed to visit in hrs'] / city_data['time needed to visit in hrs'].max()) * 0.3 +
        (1 - city_data['Entrance Fee in INR'] / city_data['Entrance Fee in INR'].max()) * 0.2 +
        (city_data['Number of google review in lakhs'] / city_data['Number of google review in lakhs'].max()) * 0.1
    )

    return city_data.sort_values(by='Score', ascending=False)[['Name', 'Google review rating', 
                                                               'Entrance Fee in INR', 
                                                               ]]

def main():
    df = load_dataset("Top Indian Places to Visit.csv")
    if df is None:
        return

    df = preprocess_data(df)
    city = input("Enter the city name: ").strip()
    
    ranked_places = rank_places(df, city)
    print(ranked_places.head(10) if isinstance(ranked_places, pd.DataFrame) else ranked_places)

if __name__ == "__main__":
    main()
