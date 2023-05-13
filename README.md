Project Description

Project Description:
This project is a Django-based web application that provides weather and news data. It utilizes external APIs to collect data and stores it in a database. The application exposes an API for retrieving weather and news information.

    Weather Data Collection:
    The project includes a data collection functionality implemented in collect_data.py. This script collects weather data from the OpenWeatherMap API for a list of cities. It fetches the current temperature and weather conditions for each city and stores the data in the database using the Weather model. The temperature is converted from Kelvin to Celsius before storage.

    News Data Collection:
    The data collection script also fetches news data from the NewsAPI. It retrieves top business news articles from the United States and stores them in the database using the News model. Each article's title, description, source, and author (if available) are stored.

    Collect Data Command: The collect_data.py script fetches weather data from the OpenWeatherMap API and news data from the NewsAPI. It saves the collected data into the database, ensuring that the weather and news information is up to date. The command can be executed manually or scheduled to run periodically.

    API Endpoints: The project provides two API endpoints for accessing the weather and news data:

        GET /api/weather/: Retrieves weather data. It supports filtering by city and minimum temperature. Example queries:
            Retrieve weather data for all cities: GET /api/weather/
            Retrieve weather data for a specific city: GET /api/weather/?city=London
            Retrieve weather data with minimum temperature greater than or equal to 20 degrees Celsius: GET /api/weather/?temperature__gte=20

        GET /api/news/: Retrieves news data. It supports filtering by source and author. Example queries:
            Retrieve all news articles: GET /api/news/
            Retrieve news articles from a specific source: GET /api/news/?source=CNN
            Retrieve news articles written by a specific author: GET /api/news/?author=John Doe

    Swagger UI: The project includes Swagger UI, which provides an interactive documentation interface for the API endpoints. It allows you to explore the available endpoints, their parameters, and responses. You can access the Swagger UI at the following URLs:
        Weather API: http://localhost:8000/swagger-ui/?url=/api/schema/weather/
        News API: http://localhost:8000/swagger-ui/?url=/api/schema/news/

    Logging: The project has logging functionality added, which helps in tracking and troubleshooting various events and errors. Logging statements are inserted at critical points in the code, allowing you to monitor the execution flow and capture important information.

    Testing: The project includes unit tests to ensure the correctness of the implemented functionality. Tests cover the models, API views, and the collect data command. They can be run using the Django test framework to validate the expected behavior of the components.

Please note that the Swagger UI URLs provided above assume that the project is running on localhost at port 8000. Adjust the URLs accordingly if your project is running on a different host or port.
