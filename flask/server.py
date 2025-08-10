from flask import Flask, make_response, request

# Create an instance of the Flask class
app = Flask(__name__)

# Sample data
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Root route
@app.route("/")
def index():
    return "hello world"

# Route for "no content"
@app.route("/no_content")
def no_content():
    return {"message": "No content found"}, 204

# Route for explicit message
@app.route("/exp")
def index_explicit():
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp

# Route for name search
@app.route("/name_search")
def name_search():
    """Find a person in the database based on the provided query parameter.

    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If the argument 'q' is missing
        422: If the argument 'q' is present but invalid (e.g., empty or numeric)
    """
    # Get the 'q' query parameter from the request URL
    query = request.args.get("q")

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to search for a matching person
    for person in data:
        # Check if the query string is present in the person's first name (case-insensitive)
        if query.lower() in person["first_name"].lower():
            # Return the matching person as a JSON response with a 200 OK status code
            return person, 200

 # If no matching person is found, return a JSON response with a message and a 404 Not Found
    return {"message": "Person not found"}, 404

@app.route("/count")
def count():
    try:
        # Attempt to return the count of items in 'data' as a JSON response
        return {"data count": len(data)}, 200
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if person["id"] == str(id):
            # Return the matching person as a JSON response with a 200 OK status code
            return person
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return {"message": "person not found"}, 404

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if person["id"] == str(id):
            # Remove the person from the 'data' list
            data.remove(person)
            # Return a JSON response with a message confirming deletion and a 200 OK status code
            return {"message": f"Person with ID {id} deleted"}, 200
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return {"message": "person not found"}, 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
