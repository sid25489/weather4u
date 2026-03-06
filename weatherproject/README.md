# Weather 4 U 🌤️

Weather 4 U is a modern, dynamic Django-based web application that provides real-time weather information and stunning visual backgrounds for any city in the world. 

[👉 **Live Demo**](#) *(Add your deployed link here once hosted!)*

## ✨ Features

- **Real-time Weather Data**: Fetches accurate and up-to-date weather data including:
  - Temperature (in Celsius)
  - Weather Condition & Descriptions
  - Humidity (%)
  - Wind Speed (m/s)
  - Feels Like Temperature
  - Atmospheric Pressure (hPa)
- **Dynamic Backgrounds**: Uses the Wikipedia API to automatically search for the requested city and display a beautiful, high-quality image of the location as the app's background.
- **Beautiful UI**: Modern, sleek interface with glassmorphism effects, FontAwesome icons, and smooth transitions built purely with HTML and CSS.
- **Error Handling**: Gracefully handles invalid city names or API errors with user-friendly error messages.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, Vanilla CSS3, Google Fonts (Outfit)
- **APIs Used**:
  - [OpenWeatherMap API](https://openweathermap.org/api) (for weather data)
  - [Wikipedia API](https://en.wikipedia.org/w/api.php) (for dynamic city background images)

## 🚀 Getting Started (Local Development)

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd weather4u/weatherproject
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django requests
   # or if you have a requirements.txt file:
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000`.

## 🌍 Deployment

You can deploy this Django project for free using platforms like:
1. **Render** or **Railway** (requires setting up Gunicorn and a database like PostgreSQL).
2. **PythonAnywhere** (great for standard Django apps).
3. **Vercel** (with Serverless configuration).

To add your own live link, just replace the `#` link placeholder at the top of this document after deployment!

---
*Built with ❤️ using Django*
