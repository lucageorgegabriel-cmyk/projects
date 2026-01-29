from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <h1>Simple Adder 🧮</h1>
    <form action="/add" method="post">
      <label>First number:</label><br>
      <input name="a" type="number" step="any" required><br><br>

      <label>Second number:</label><br>
      <input name="b" type="number" step="any" required><br><br>

      <button type="submit">Add</button>
    </form>
    """

@app.post("/add")
def add():
    a = float(request.form["a"])
    b = float(request.form["b"])
    result = a + b
    return f"""
    <h1>Result ✅</h1>
    <p>{a} + {b} = <b>{result}</b></p>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
