import json
import uuid
from flask import Flask, Response, jsonify, render_template, url_for, make_response
from flask import request
from config.firebase import firebase_config as fbs
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

@app.route("/register_site")
def register_site() :
    sites_ref = fbs.db.collection("Sites").document("Golio")
    site = sites_ref.get()
    data = {"message" : "exist_deja"}
    res = make_response(data)
    if site.exists:
        return res
    else :
        data = {
                "SiteId" : "Golio",
                "Name" : "Golio",
                "Url" : "golio.vercel.app",
                "Date_creation" :  datetime.datetime.today(),
                "Autre" : {}
            }
        sites_ref.set(data)
        res = make_response(data)
        return res
@app.route("/register_user")
async def register_user() :
    cookie = request.cookies.get("visiteur_id")
    path = request.args.get("path", "/register_user")
    url = request.args.get("url", "golio.vercel.app")
    page_title = request.args.get("page_title", "Acceuil")
    
    if  cookie == None:
        visiteur_ref = fbs.db.collection("Visiteurs").document()
        visiteur = {
            "SiteId" : "Golio",
            "Date_Visite" : datetime.datetime.today(),
            "heure_Visite" : datetime.datetime.now(),
            "Adress_ip" : request.remote_addr,
            "navigateur" : request.user_agent.browser,
            "système_exploitation" : request.user_agent.platform
        }
        visiteur_ref.set(visiteur)
        
        page_vistee = {
            "path" : path,
            "VisiteurId" : visiteur_ref.id,
            "SiteId" : "Golio",
            "url" : url,
            "page_title" : page_title,
            "date_visite" : datetime.datetime.today(),
            "Nombre_vistie" : 1            
        }
        page_ref =  fbs.db.collection("Pages_visitees").document()
        page_ref.set(page_vistee)

        res = {
            "message" : "page set and user set",
            "page_id" : page_ref.id
        }
        response = make_response(res)
        response.set_cookie("visiteur_id", visiteur_ref.id)
        
        print("firstly added ")
        return response
    else :
        list_page = request.args.get("list_page_id")
        print("list_page" , list_page.split(','))
        page_exist = False
        for page_id in list_page.split(',') :
            if page_id == "" :
                continue
            print("Page_id : ", page_id)
            page_vistee_ref =  fbs.db.collection("Pages_visitees").document(page_id)
            page_vistee = page_vistee_ref.get()
            if page_vistee.exists :
                pages_dict = page_vistee.to_dict()
                nbv =  pages_dict["Nombre_vistie"]
                print("path_by_js", path)
                print("path_by_fbase", pages_dict["path"])
                if path == pages_dict["path"] :
                    page_exist = True
                    page_vistee_ref.update({"Nombre_vistie" : nbv + 1})
                    print("updated")
                    p_id = None
                    break
        if page_exist == False :
            print("le path n'est pas enrigitrees")
            page_vistee = {
            "path" : path,
            "VisiteurId" : cookie,
            "SiteId" : "Golio",
            "url" : url,
            "page_title" : page_title,
            "date_visite" : datetime.datetime.today(),
            "Nombre_vistie" : 1       
        }
            page_ref =  fbs.db.collection("Pages_visitees").document()
            page_ref.set(page_vistee)
            p_id = page_ref.id
        res = {
            "message" : "page set and user set",
            "page_id" : p_id
            }
        response = make_response(res)
        return response


@app.route("/page_2")
def p_2():
    return render_template("page_2.html")

@app.route("/super_page")
def s_p():
    return render_template("super_page.html")