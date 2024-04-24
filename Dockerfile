FROM python
WORKDIR /project
COPY . /project
COPY Random.txt /project/
RUN pip install nltk
CMD ["python3","project.py"]