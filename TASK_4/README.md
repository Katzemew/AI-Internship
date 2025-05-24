# TASK_NO_4 
# Content-Based Movie Recommendation System

Welcome to the **Content-Based Movie Recommendation System** — a Python-powered system that recommends movies based on metadata like cast, director, keywords, and genres. This system uses natural language processing and cosine similarity to find movies similar to a given title.

## How to Use

1. Clone or download this repository to your local machine.

2. Make sure you have Python 3.x installed along with required libraries (`pandas`, `scikit-learn`, `numpy`).

3. Navigate to the project directory.

4. Run the notebook or script to build the recommendation engine and test movie recommendations.

## Features

* **Metadata-based recommendations**: Uses cast, director, genres, and keywords for similarity.
* **Text preprocessing**: Cleans and normalizes text data for consistent comparisons.
* **Vectorization**: Transforms text data into numerical vectors using `CountVectorizer`.
* **Similarity calculation**: Uses cosine similarity to find closest movies.
* **Interactive recommendations**: Easily get top N movie recommendations by title.
* **Handles missing or inconsistent data** with cleaning functions.

## Sample Usage

```python
print(get_recommendations("The Dark Knight Rises", cosine_sim2))
print(get_recommendations("The Avengers", cosine_sim2))
````

These will output lists of movies similar to the given titles.

## Requirements

* Python 3.x
* pandas
* numpy
* scikit-learn

### Install Requirements

Run this in your terminal:

```bash
pip install pandas numpy scikit-learn
```

## Project Structure

```bash
├── TASK_4/
│   ├── Movie_Recommendation.ipynb  # Your Colab notebook
│   ├── README.md                   # This README file
├── data/
│   ├── tmdb_5000_movies.csv       # Movies dataset
│   ├── tmdb_5000_credits.csv      # Credits dataset
├── requirements.txt               # (Optional) List of Python packages
```

## Implementation Details

* Parses JSON fields like cast, crew, genres using `ast.literal_eval`.
* Extracts director name from crew data.
* Cleans text by removing spaces and converting to lowercase.
* Combines features into a single text “soup” for each movie.
* Vectorizes “soup” with `CountVectorizer` (stop words removed).
* Calculates cosine similarity matrix for all movies.
* Provides a lookup function to recommend similar movies by title.

## Future Improvements

* Add more sophisticated NLP models (TF-IDF, Word2Vec, or transformers).
* Integrate user ratings for a hybrid recommendation system.
* Build a web app or API for interactive movie recommendations.
* Improve handling of multi-language and missing data.
* Add visualization of recommendation results.

## Credits

* Developed following the tutorial on Analytics Vidhya:
  [Movies Recommendation System using Python](https://www.analyticsvidhya.com/blog/2022/08/movies-recommendation-system-using-python/)
* Built with Python, pandas, and scikit-learn.
* Thanks to the open-source community for datasets and libraries.

---

Feel free to open issues or contribute improvements!

```

---