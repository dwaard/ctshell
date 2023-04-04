# Template project for Python projects
Uses Docker, environment variables and logging.

## Docker
Docker is used for running the code inside a container.

### Building

docker build -t ctc .

### Running

For CMD:
```
docker run -it --rm --name ctc -v %cd%:/app -v \\wsl.localhost\Ubuntu-20.04\home\waar0003\temp:/submissions -w="/app" ctc python main.py
```

For Powershell:
```
docker run -it --rm --name ctc -v ${pwd}:/app -v \\wsl.localhost\Ubuntu-20.04\home\waar0003\temp:/submissions -w="/app" ctc python main.py
```

## Environment variables
