# 🎬 Movie Recommender System

A machine learning-powered movie recommendation engine built with **Streamlit** and **Python**. This application analyzes movie data to suggest films you might enjoy based on content similarity.

---

## 📋 Project Overview

The Movie Recommender System uses collaborative filtering and content-based recommendation algorithms to help users discover movies tailored to their preferences. The application features an interactive web interface powered by Streamlit, making it easy for anyone to explore personalized movie recommendations.

---

## ✨ Features

- **Interactive Web Interface**: User-friendly Streamlit dashboard for exploring recommendations
- **Content-Based Filtering**: Recommends movies based on plot, genre, cast, and crew similarities
- **Movie Search**: Search for any movie in the database to get recommendations
- **Movie Metadata Display**: View detailed information about recommended movies
- **Top Recommendations**: Get top N movie suggestions based on similarity scores
- **TMDB Dataset**: Uses The Movie Database (TMDB) dataset with 5,000+ movies

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application (runs the web interface) |
| `main.py` | Core recommendation logic and data processing |
| `Movie-recommender-system.ipynb` | Jupyter notebook with exploratory data analysis and testing |
| `tmdb_5000_movies.csv` | Dataset containing movie metadata (titles, genres, plot, etc.) |
| `tmdb_5000_credits.csv` | Dataset containing cast and crew information |
| `requirement.txt` | Python package dependencies |
| `Procfile` | Deployment configuration for cloud platforms |
| `setup.sh` | Setup script for initialization |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8 or higher** installed on your system
- **Git** (optional, for cloning the repository)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd Movie-recommender-system
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   
   **On Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install required packages**:
   ```bash
   pip install -r requirement.txt
   ```

   This will install:
   - `streamlit` - Web app framework
   - `pandas` - Data manipulation
   - `numpy` - Numerical computing
   - `scikit-learn` - Machine learning algorithms

---

## 🎯 Running the Application

### Run Locally

1. Make sure your virtual environment is activated (see step 3 in Installation)

2. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:8501
   ```

4. **Start using the application**:
   - Search for your favorite movie
   - Get personalized recommendations
   - Explore movie details and metadata

### Using Jupyter Notebook

To explore the data and recommendation algorithms in detail:

```bash
jupyter notebook Movie-recommender-system.ipynb
```

---

## 🔍 How It Works

1. **Data Loading**: The system loads movie metadata from CSV files
2. **Feature Engineering**: Creates feature vectors from movie attributes (genres, cast, crew, keywords)
3. **Similarity Calculation**: Computes similarity between movies using cosine similarity
4. **Recommendation Generation**: Returns top N movies most similar to the selected movie
5. **Display Results**: Shows recommendations with details in the Streamlit interface

---

## 📊 Dataset Information

The project uses **TMDB 5000 Movies Dataset**:
- **Movies**: 5,000+ movies with comprehensive metadata
- **Features Included**: Title, Genre, Plot, Release Date, Cast, Crew, Budget, Revenue, etc.
- **Time Period**: Various movie release years

---

## 🛠️ Development & Customization

### Modifying Recommendation Algorithm

Edit `main.py` to:
- Adjust similarity metrics
- Add weighted features
- Implement different algorithms

### Customizing the UI

Edit `app.py` to:
- Change layout and styling
- Add new features or filters
- Modify the display format

### Adding More Data

Replace or append to CSV files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🌐 Future Deployment

### Option 1: Deploy to Streamlit Cloud (Recommended for Beginners)

1. Push your project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign up with your GitHub account
4. Click "New app" and connect your GitHub repository
5. Streamlit Cloud will automatically deploy your app

### Option 2: Deploy to Heroku

1. Install Heroku CLI
2. Create a Heroku account
3. In your project directory:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```
4. Your app will be live at `your-app-name.herokuapp.com`

### Option 3: Deploy to AWS/DigitalOcean

1. Set up an instance on your chosen platform
2. Clone the repository
3. Install dependencies
4. Run: `streamlit run app.py --server.port 80`

### Deployment Checklist

- [ ] Update `requirement.txt` with exact package versions
- [ ] Set `logger.setLevel()` to INFO in production (not DEBUG)
- [ ] Add environment variables for sensitive data
- [ ] Test the app locally before deployment
- [ ] Set up a Procfile for cloud deployments (already included)

---

## 📝 Example Usage

```python
# Search for "The Dark Knight"
# The app will recommend similar movies like:
# - The Dark Knight Rises
# - Batman Begins
# - The Prestige
# - Inception
```

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

## 📄 License

This project is open source and available under the MIT License.

---

## ❓ Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'streamlit'`  
**Solution**: Make sure you've activated your virtual environment and installed requirements with `pip install -r requirement.txt`

**Problem**: `Port 8501 already in use`  
**Solution**: Run on a different port with `streamlit run app.py --server.port 8502`

**Problem**: CSV files not found  
**Solution**: Ensure CSV files are in the same directory as `app.py`

---

## 📧 Questions & Support

For issues or questions, please open an issue in the GitHub repository or contact the project maintainer.

---

**Happy Movie Watching! 🍿**
