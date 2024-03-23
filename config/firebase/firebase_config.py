import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

private = {
    "type": "service_account",
    "project_id": os.getenv('PROJECT_ID'),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_SECURE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-570kp%40mystats-9a1b4.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(private)
firebase_admin.initialize_app(cred)
db = firestore.client()