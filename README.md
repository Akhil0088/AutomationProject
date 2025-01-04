# Trending News Application

This is a web application that displays trending news across multiple categories, fetched dynamically from an external API. The application allows users to filter news by category and load more articles seamlessly. It is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

---

## Features

- **Filter News by Category**: Select from a wide range of categories such as Sports, Business, Technology, etc.
- **Dynamic News Loading**: Fetch additional news articles dynamically without reloading the page using AJAX.
- **Responsive Design**: The app is designed to work on various screen sizes, ensuring a smooth user experience.
- **Modern UI**: An elegant and minimalistic user interface with smooth transitions and hover effects.

---

## Technologies Used

### Frontend
- **HTML5**: For the structure of the application.
- **CSS3**: For styling, including modern techniques like Flexbox and CSS transitions.
- **JavaScript (ES6)**: For dynamic functionalities, including fetching data from the backend and updating the UI.
- **Bootstrap (Optional)**: If needed for further responsive design.

### Backend
- **Flask**: A lightweight Python web framework to serve the application and handle API requests.
- **Python**: The primary programming language used for the backend.

### API
- **Inshorts API**: The news is fetched from the Inshorts API based on the selected category.

---

## Installation and Setup

Follow these steps to set up and run the application locally:

### Prerequisites

- Python 3.7 or above installed on your system.
- A package manager like `pip` to install Python dependencies.

### Steps

1. **Clone the Repository**  
   Clone this repository to your local machine:

2. Set up a Virtual Environment (Optional)
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Run the Application
    python news_app.py

5. Open the Application
    http://127.0.0.1:5000

-------------------------------------------------------------------------------------------

#Usage Instructions

Home Page: The home page displays trending news for the default category (Sports).
Filter News: Use the dropdown to filter news by category and click the Filter button to fetch results.
Load More: Click the "Load More" button to fetch additional news articles for the selected category.
Read Full News: Each article includes a "Read More" link, which redirects you to the full news article on the original source.


-------------------------------------------------------------------------------------------

#How It Works

Backend:
The Flask app serves the main HTML page (index.html) and handles API requests for loading news.
A Python function (fetch_news) fetches news data from the Inshorts API using the selected category and page number.

Frontend:
The frontend renders news articles dynamically using data fetched from the Flask backend.
JavaScript fetches additional news articles via an AJAX call when the "Load More" button is clicked.


-------------------------------------------------------------------------------------------

#Future Enhancements

Search Functionality: Add a search bar to find news articles based on keywords.
User Authentication: Allow users to log in and save their favorite articles.
Pagination: Improve the "Load More" feature by adding pagination controls.
Error Handling: Enhance error handling for better user feedback in case of API failures.
