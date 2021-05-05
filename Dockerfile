FROM python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /basecode
COPY ./requirements.txt /basecode
RUN pip install -r requirements.txt
COPY . /basecode