from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class HealthCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    status_code = db.Column(db.Integer, nullable=True)
    is_up = db.Column(db.Boolean, nullable=False)
    response_time_ms = db.Column(db.Float, nullable=True)
    error_message = db.Column(db.String(255), nullable=True)
    checked_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
