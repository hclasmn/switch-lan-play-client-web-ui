FROM python:alpine
WORKDIR /play
COPY ./ /play
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]