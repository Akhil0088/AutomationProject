from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Categories for the dropdown
categories = [
    "national",
    "business",
    "sports",
    "world",
    "politics",
    "technology",
    "startup",
    "entertainment",
    "miscellaneous",
    "hatke",
    "science",
    "automobile"
]

# Function to fetch news data from a specific page
def fetch_news(category, page_num=1):
    
    if page_num == 1:
        api_url = f"https://inshorts.com/api/en/search/trending_topics/{category}"
    else:
        api_url = f"https://inshorts.com/api/en/search/trending_topics/{category}?page={page_num}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Route to render the main page
@app.route("/", methods=["GET", "POST"])
def home():
    selected_category = request.args.get("category", "sports")  # Default category
    current_page = 1  # Initial page load fetches the first page

    # Fetch news data for the selected category 
    news_data = fetch_news(selected_category, current_page)
    news_items = news_data.get("data", {}).get("suggested_news", []) if news_data else []

    # Prepare the news for rendering
    news_list = []
    for item in news_items:
        news_obj = item.get("news_obj", {})
        news_list.append({
            "hash_id": news_obj.get("hash_id", ""),
            "title": news_obj.get("title", "No Title"),
            "caption": news_obj.get("content", "No Caption"),
            "image_url": news_obj.get("image_url", ""),
            "url": news_obj.get("source_url", ""),
        })

    return render_template(
        "index.html",
        news=news_list,
        categories=categories,
        selected_category=selected_category,
        current_page=current_page
    )

# Route to fetch additional news dynamically
@app.route("/load_more", methods=["POST"])
def load_more():
    category = request.json.get("category", "sports")
    page_num = request.json.get("page", 2)  

    # Fetch news data for the specified page
    news_data = fetch_news(category, page_num)
    news_items = news_data.get("data", {}).get("suggested_news", []) if news_data else []

    # Prepare the news for returning
    news_list = []
    for item in news_items:
        news_obj = item.get("news_obj", {})
        news_list.append({
            "hash_id": news_obj.get("hash_id", ""),
            "title": news_obj.get("title", "No Title"),
            "caption": news_obj.get("content", "No Caption"),
            "image_url": news_obj.get("image_url", ""),
            "url": news_obj.get("source_url", ""),
        })

    return jsonify(news_list)  # Return the news items as JSON

if __name__ == "__main__":
    app.run(debug=True)
