FROM python:alpine3.13
WORKDIR /app
COPY MainScores.py ./
COPY Scores.txt ./
EXPOSE 8777
RUN pip install Flask
CMD ["python" , "MainScores.py"]
