FROM python

RUN pip install flask selenium
RUN mkdir /app

COPY app/  /app/

expose 5000

WORKDIR /app
# ENTRYPOINT ["python"]
CMD ["./run.sh"]
