from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    cards = [ 
        {
            "bg" : "bg-secondary",
            "img" :  url_for('static', filename='images/card1.svg'),
            "title" : "UI/UX Design",
            "description" : "Etiam sed vulputate nisl, eu elementum arcu. Vivamus dignissim tortor in tellus dictum pellentesque.",
            "btn_color" : "text-primary"
        },
        {
            "bg" : "bg-red",
            "img" : url_for('static', filename='images/card2.svg'),
            "title" : "Mobile App Design",
            "description" : "Etiam sed vulputate nisl, eu elementum arcu. Vivamus dignissim tortor in tellus dictum pellentesque.",
            "btn_color" : "text-purpule"
        },
        {
            "bg" : "bg-light",
            "img" : url_for('static', filename='images/card3.svg'),
            "title" : "Front-end Development",
            "description" : "Etiam sed vulputate nisl, eu elementum arcu. Vivamus dignissim tortor in tellus dictum pellentesque.",
            "btn_color" : "text-dark"
        }
]
    return render_template("index.html", cards=cards)
