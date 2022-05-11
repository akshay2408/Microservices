# Mircroservices
This repository is contained three diff microservices Warehouse, Accounting, Sales with single database created a single API that seamlessly exposes the data of these three microservices: using FastAPi

# README
This README covers setup instructions for running system locally.

## Fast API
FastAPI is a modern, high-performance, web framework, which comes with tons of cool features like auto-documentation based on OpenAPI and built-in serialization and validation library.I think FastAPI is a great choice for building microservices in Python is:
 - Auto documentation
 - Async/Await support
 - Built-in validation and serialization
 - 100% type annotated so autocompletion works great

## Steps to run services locally using docker
#### Build image
- docker build -t api .
#### Run Docker
- docker run -p 80:80
## Api Details:
```
  endpoint : http://31.171.250.30/get_all_microservice_data/
  request-method: GET
  response: {"accounting":["list of accounting data"],"warehouse":["list of warehouse data"],"sales":["list of sales data"]} 
```

## Command to run test cases
- `python -m pytest`