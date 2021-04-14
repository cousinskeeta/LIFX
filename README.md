# LIFX
This is repo uses the Python, Flask and the LIFX API to control different requests sent to my wifi-enabled lights. 

I deployed the web application here: [My LIFX App](http://lifxapp.pythonanywhere.com/)
 
To run locally just download the repo, navigate to directory with requirements and app.py file via terminal, and follow the steps below: 

1. Set up virtualenv
    1. pip install virtualenv
    2. virtualevn venv
    3. source venv/bin/activate
2. Install requirements in the venv
    1. python -m pip install -r requirements.txt
3. Run the app using Flask microservices:
    1. python -m flask run
4. Open localhost in browser:
    1. Running on http://127.0.0.1:5000/ 
