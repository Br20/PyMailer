from flask import  (Blueprint, render_template, request, flash, redirect, url_for, current_app)
from .db import get_db
#import sendgrid
#from sendgrid.helpers.mail import *

bp = Blueprint('mail', __name__, url_prefix="/")

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute(
        'SELECT * FROM email'
    )
    mails = c.fetchall()
    print(mails)
    return render_template('mails/index.html', mails=mails)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        addr = request.form['addr_to']
        subject = request.form['email-subject']
        content = request.form['email-content']
        errors = []
        if not addr:
            errors.append('Destination address is required.')
        if not subject:
            errors.append('Subject is required.')
        if not content:
            errors.append('Content is required.')

        if len(errors) == 0:
            db,c = get_db()
            c.execute(
                'INSERT INTO email (addr_to, subject, content) VALUES (%s,%s,%s)',(addr, subject, content)
            )
            db.commit()
            send(addr, subject, content)
            return redirect(url_for('mail.index'))
        else:
            for error in errors:
                flash(error)
    return render_template('mails/create.html')

'''
def send(to, subject, content):
    sg = SendGridAPIClient(api_key=current_app.config['SENDGRID_API_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(to)
    content = Content('text/plain',content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response)
'''