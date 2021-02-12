docker:
	docker build -t smartscreen .

start:
	docker run --rm -d --name=smartscreen -p 9786:9786 smartscreen

stop:
	docker kill smartscreen

bash:
	docker exec -it smartscreen bash

all: docker
