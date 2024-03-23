import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

private = {
    "type": "service_account",
    "project_id": "mystats-9a1b4",
    "private_key_id": "b792b92ca11cf3acd4e0c67756dd3997ffa51eba",
    "private_key": os.getenv("FIREBASE_SECURE_KEY"),
    "client_email": "firebase-adminsdk-570kp@mystats-9a1b4.iam.gserviceaccount.com",
    "client_id": "100274967463510339747",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-570kp%40mystats-9a1b4.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(private)
firebase_admin.initialize_app(cred)
db = firestore.client()