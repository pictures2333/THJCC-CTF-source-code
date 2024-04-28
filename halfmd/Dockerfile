FROM python

WORKDIR /app
COPY . .

RUN apt update
RUN apt install -y cron
RUN pip3 install flask
RUN pip3 install flask-session

RUN cp /app/cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

RUN chmod 777 /app/run.sh

CMD ["bash", "run.sh"]

EXPOSE 10009
