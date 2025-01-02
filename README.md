# HyperNews Portal

The HyperNews Portal is a Django-based web application designed to manage and display news articles. Users can view a list of news articles, search for specific articles, and create new articles.

## Features

- View a list of news articles with their titles and creation dates.
- Search for news articles by title.
- Create new news articles with a title and text content.
- Redirect from the "Coming Soon" page to the news list.

## Project Structure

- `news/`: Contains the main Django app for the news portal.
  - `views.py`: Contains the view functions for handling requests and rendering templates.
  - `templates/`: Contains HTML templates for rendering news content.
  - `news.json`: Stores the news articles data in JSON format.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd HyperNews-Portal

2.
Install Dependencies:

Ensure you have Python and pip installed. Then, install the required packages:
pip install -r requirements.txt
3.
Run the Server:

Start the Django development server:
python manage.py runserver
4.
Access the Application:

Open your web browser and go to http://localhost:8000/news/ to view the news portal.


Usage
View News Articles: Navigate to the /news/ endpoint to see a list of news articles.
Search Articles: Use the search bar to find articles by title.
Create Articles: Go to /news/create/ to add a new article.
Redirect from Coming Soon: Accessing the root URL / will redirect you to the news list.
