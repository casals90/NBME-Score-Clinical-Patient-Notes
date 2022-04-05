NBME - Score Clinical Patient Notes
==============================

Identify Key Phrases in Patient Notes from Medical Licensing Exams.

Kaggle competition link https://www.kaggle.com/competitions/nbme-score-clinical-patient-notes/overview.

Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization

## Notebook prototyping setup

For prototyping purposes, the notebook setup can be used. The setup for
the prototyping system involves building the docker image, preparing the
volumes and running the Jupyter service.


### Docker image

From the root of the project do the following:

```commandline
docker build -f Dockerfile -t jupyter_environment .
```
With this we have obtained a docker image which will take all necessary
source files, and will offer a Jupyter lab service synchronised with them.


#### Check the volumes

The system needs to interact with some folders in order to be able to take 
necessary data, transform, store results, train and predict models.

From the root folder, the volumes are mounted as follows:

```yaml
    volumes:
      - ./src:/home/jovyan/work/src
      - ./notebooks:/home/jovyan/work/notebooks
      - ./data/external:/data/external
      - ./data/interim:/data/interim
      - ./data/processed:/data/processed
      - ./data/raw:/data/raw
      - ./reports:/reports
```

For prototyping purposes, it is not advisable to change the above
volumes for consistency across projects.


### Start/shutdown the system

When ready, start the system from the root folder as follows:

```commandline
docker-compose -f docker-compose.yml up
```

Shutdown the system as follows:

```commandline
docker-compose -f docker-compose.yml down
```


### Notebook

The notebook service is accessible by default through the port 8888. It
requires an access token, which is displayed when the system starts. The
main notebook entry can be accessed by directly entering the link shown in
the console.

E.g.

```
http://127.0.0.1:8888/lab?token=14fc7403fe4d8dfab812d2cc5a960879f687f8ecaf3aa8f6
```
