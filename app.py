from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        time = request.form["time"]
        task = request.form["task"]
        tasks.append({"time": time, "task": task})
        tasks.sort(key=lambda x: x["time"])  # เรียงตามเวลา
        return redirect("/")

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
