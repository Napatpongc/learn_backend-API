from flask import Flask,jsonify

app = Flask(__name__)
books = [
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":1,"title":"Book 1","author":"Author 1"},
]
@app.route("/")
def greet():
    return "<p>Welcome to Book Management Systems</p>"

@app.route("/books")
def get_all_books():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)