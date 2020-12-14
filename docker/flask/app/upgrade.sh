export DB_USER=root
export DB_PASSWORD=root
export DB_HOST=175.30.0.4
export DB_PORT=3306

export FLASK_ENV=development
export FLASK_APP=./main.py

flask db migrate
flask db upgrade