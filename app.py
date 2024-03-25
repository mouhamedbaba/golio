import json
import uuid
from flask import Flask, Response, jsonify, render_template, url_for, make_response
from flask import request
app = Flask(__name__)
import datetime

LOREM = "Etiam sed vulputate nisl, eu elementum arcu. Vivamus dignissim tortor in tellus dictum pellentesque."



@app.route("/")
def index():
    print(request.user_agent.platform)
    CARDS = [ 
        {
            "bg" : "bg-secondary",
            "img" :  url_for('static', filename='images/card1.svg'),
            "title" : "UI/UX Design",
            "description" : LOREM,
            "btn_color" : "text-primary"
        },
        {
            "bg" : "bg-red",
            "img" : url_for('static', filename='images/card2.svg'),
            "title" : "Mobile App Design",
            "description" : LOREM,
            "btn_color" : "text-purpule"
        },
        {
            "bg" : "bg-light",
            "img" : url_for('static', filename='images/card3.svg'),
            "title" : "Front-end Development",
            "description" : LOREM,
            "btn_color" : "text-dark"
        }
]

    SELECTED_CARDS = [
    {
    "img" : url_for('static', filename='images/ui/project1.jpg'),
    "title" : "E-tutor - education & online LMS"
    },
    {
    "img" : url_for('static', filename='images/ui/project2.jpg'),
    "title" : "Pagoupon - Properties Agency Website"
    },
    {
    "img" : url_for('static', filename='images/ui/project3.jpg'),
    "title" : "Find workspace - Mobile app design"
    }
]

    
    TESTI_CARDS = [
        {
            "name" : "Devon Lane",
            "job" : "CEO & Founder of Gilio",
            "img" : url_for('static', filename='images/ui/Photo.png'),
            "bg" : "bg-green"
        },
        {
            "name" : "Kristin Watson",
            "job" : "UI Designer",
            "img" : url_for('static', filename='images/ui/Photo2.png'),
            "bg" : "bg-rose"
        }, 
        {
            "name" : "Jacob Jones",
            "job" : "Product Designer",
            "img" : url_for('static', filename='images/ui/Photo3.png'),
            "bg" : "bg-yellow"
        },
        {
            "name" : "Esther Howard",
            "job" : "Front-end Developer",
            "img" : url_for('static', filename='images/ui/Photo4.png'),
            "bg" : "bg-blue"
        }
    ]
    
    TRUSTED_BY = [
        {
            "name" : "Lenovo",
            "img" : url_for('static', filename='images/ui/LogoL.png')
        },
        {
            "name" : "Amazon",
            "img" : url_for('static', filename='images/ui/Logoa.png')
        },
        {
            "name" : "Youtube",
            "img" : url_for('static', filename='images/ui/Logoy.png')
        },
        {
            "name" : "Slack",
            "img" : url_for('static', filename='images/ui/Logos.png')
        },
        {
            "name" : "Microsoft",
            "img" : url_for('static', filename='images/ui/Logom.png')
        }
    ]
    
    FOOTER_LINKS = [
        {
            "title" : "Quick Links",
            "list" : [
                "Portfolio",
                "About",
                "Services",
                "Pracing Plan",
                "Contact"
            ]
        },
        {
            "title" : "Services",
            "list" : {
            "UI/UX Design",
            "Branding",
            "Illustration",
            "Design Concept",
            "App Design"
            }
        },
        {
            "title" : "Product",
            "list" : [
                "Figma",
                "Adobe",
                "Dribbble",
                "Behance",
                "Themeforest"
            ]
        }
    ]
    
    return render_template("index.html", cards=CARDS, selected_cards=SELECTED_CARDS, testi_cards=TESTI_CARDS, trusted_by=TRUSTED_BY, footer_links=FOOTER_LINKS)


@app.route("/page_2")
def p_2():
    return render_template("page_2.html")

@app.route("/super_page")
def s_p():
    return render_template("super_page.html")