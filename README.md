# PyMailer

This project is a mailer made in Python using the Flask microframework.

## Requirements

- Python 3.x
- virtualenv

## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/Br20/PyMailer.git](https://github.com/Br20/PyMailer.git)
    cd PyMailer

2. Create a virtual environment:
    
    ```bash
    python -m venv venv

3. Activate the virtual environment:
    
    ```bash
    . venv/bin/activate 
    
4. Install the dependencies:
    
    ```bash
    pip install -r requirements.txt
    

## Uso

1. Create account in https://sendgrid.com/en-us, define a secure mail and  generate an API_KEY (Save it very well).

2. Set some environment variables:
    
    Create a .env file to set the environment variables necessary for the application to function. These are:
        
        - FLASK_DATABASE_USER  
        - FLASK_DATABASE_PASSWORD
        - FLASK_DATABASE
        - FLASK_DATABASE_HOST
        - SENDGRID_API_KEY  <!-- Key generada en la web de sendgrip -->
        - FROM_EMAIL <!-- dirección de correo de donde se enviaran los mails -->
        
    In addition to this, you must define the flask starting point and the environment used

    ```bash
    export FLASK_APP=.
    export FLASK_ENV=development

3. Start the application

    ```bash
    flask run
    
4. View sent emails:

    Open a web browser and go to http://127.0.0.1:5000
    All sent emails will be displayed there along with a search bar to filter emails by content.

5. Send a new email:

    Clicking on the button in the top right corner or going to http://127.0.0.1:5000/create will display the email sending screen.
    Once the data is complete, press send and it will redirect to the email list.