from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # belajar looping
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
   # coditioning / if-else
    suasana = "sedih" 
    
    return render_template("index.html", value = hari, suasana = suasana)

if __name__ == "__main__":
    app.run(debug=True)