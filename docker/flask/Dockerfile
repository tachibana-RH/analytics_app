FROM python:3.7

WORKDIR /code

# ADD entrypoint.sh /code/entrypoint.sh
ADD app/ /code

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/code/"
ENV FLASK_APP "/code/main.py"

# CMD ["/code/entrypoint.sh"]