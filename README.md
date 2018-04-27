# Project Title

The idea of this project is a simple web application for the dog breed classifier developed in my dog-project. Caveat: This is very rudimentary code and its not heavily tested. This is also my first web development project, so there will be a lot of things to improve and I am also happy to receive suggestions. But I am not sure how strongly I am going to develop this project in future.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them

For this project, I used:
Keras 2.1.5: `conda install -c conda-forge keras`

Tensorflow 1.5.1: `conda install -c conda-forge tensorflow`

Flask 0.12.2: `pip install Flask`

### Installing

Clone the repository and navigate to the downloaded folder.
```	
git clone https://github.com/gro1m/dogbreed_flask
cd dog-project
```

## Running the tests
No tests for this system.

## Deployment
Follow the guidelines on http://flask.pocoo.org/docs/0.12/tutorial/packaging/, but set `export FLASK_DEBUG=0`.
So, in essence:
```
pip install --editable .
cd dogbreed_flask
export FLASK_APP=dogbreed_flask
export FLASK_DEBUG=0
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

I acknowledge that the html code is mainly from Ibrahim Mokdad's repository https://github.com/ibrahimokdadov/upload_file_python and has been minorly adapted to my use case. The dogbreed_detector.py is the main function and uses the model from https://github.com/gro1m/dog-project.