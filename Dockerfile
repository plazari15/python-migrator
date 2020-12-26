FROM python:3.9

ARG ENV=prod

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN if [ "$ENV" = "travisci" ]; then python -m pip install pytest ; fi

COPY . .