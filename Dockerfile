FROM python

RUN pip install flask
RUN mkdir /app

COPY app/  /app/

expose 5000

WORKDIR /app
# ENTRYPOINT ["python"]
CMD ["./run.sh"]
