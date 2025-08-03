# Database configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/prediction_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = '#4321Mayuri@#'
JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
