### PRE-REQUISITES

- `docker` and `docker-compose` to be already installed on the system
- valid alpha vantage API key


##### Running the project
- run `./setup.sh` from the root of the project to setup necessary environments.
- Add your alpha vantage API key in `.env` file
- run `docker-compose build` from the root of this project to build the project image
- run `docker-compose up` from the root of this project to start the project

##### API endpoints
- `curl -X GET 0.0.0.0:8000/api/v1/quotes` will give you the quotes it has stored in the system
- `curl -X POST 0.0.0.0:8000/api/v1/quotes` will fetch the latest quotes for BTC-USD exchange rates.