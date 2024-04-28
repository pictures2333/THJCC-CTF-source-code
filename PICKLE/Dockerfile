FROM python

WORKDIR /app
COPY . .

RUN pip3 install flask
RUN pip3 install flask-session
RUN pip3 install requests

RUN useradd -m -d /home/ctfuser -s /bin/bash ctfuser

RUN chown -R ctfuser:ctfuser /app && \
    chmod -R 550 /app && \
    chmod -R 770 /app/uploads

USER ctfuser

CMD ["python3", "main.py"]

EXPOSE 10008
