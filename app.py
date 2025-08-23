from flask import Flask, request, jsonify, render_template
from scraper.scraper import scrape_amazon_results

app = Flask(__name__)

# API endpoint
@app.route("/api/scrape", methods=["GET"])
def api_scrape():
    query = request.args.get("query")
    limit = request.args.get("limit", 10, type=int)

    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    try:
        data = scrape_amazon_results(query, limit)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Web interface
@app.route("/", methods=["GET", "POST"])
def home():
    products = None
    error = None

    if request.method == "POST":
        query = request.form.get("query")
        limit = int(request.form.get("limit", 10))

        if query:
            try:
                products = scrape_amazon_results(query, limit)
            except Exception as e:
                error = str(e)
        else:
            error = "Please enter a search term."

    return render_template("index.html", products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True)
