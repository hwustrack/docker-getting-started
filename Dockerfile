FROM python:3.8

ADD script.py /
 
CMD [ "python", "./script.py" ]