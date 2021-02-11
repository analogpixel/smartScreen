docker:
	docker build -t smartscreen .

run:
	docker run --rm -d smartscreen

all: docker
