# Dog Breed Classifier Web App

The idea of this project is a simple web application for the dog breed classifier developed in my dog-project. Caveat: This is very rudimentary code and its not heavily tested. This is also my first web development project, so there will be a lot of things to improve and I am also happy to receive suggestions. But I am not sure how strongly I am going to develop this project in future.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Instructions

1. Clone the repository and navigate to the project folder:
```	
git clone https://github.com/gro1m/dogbreed_flask
cd dogbreed_flask
```
2. Set up a virtual environment (called `test-env` here as an example):
```
conda create --name test-env python=3.6 anaconda
```
3. Install the project requirements located in the bash script requirements.sh:
```
./requirements/requirements.sh
```
4. Execute setup.py:
```
pip install --editable .
```
5. Set environment variables:
```
export FLASK_APP=dogbreed_flask
export FLASK_DEBUG=0
```
6. Run the flask application:
```
flask run 
```
7. Navigate to `http://localhost:5000/` in a web-browser.
8. Choose an image file on your computer by pressing the first button and then press the `Upload!` button.
9. Wait and then see the classification of the image by the dog breed classifier.

__NOTE:__ FLASK_DEBUG=0 has to be set, as otherwise issues with loading a keras model occur, which is discussed and observed by spearsem on https://github.com/keras-team/keras/issues/5640.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

I acknowledge that the html code is mainly from Ibrahim Mokdad's repository https://github.com/ibrahimokdadov/upload_file_python and has been minorly adapted to my use case. The dogbreed_detector.py is the main function and uses the model from https://github.com/gro1m/dog-project.