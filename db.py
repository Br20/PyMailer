import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

# Create database connection and cursor.
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary = True)
    return g.db, g.c

# Close database
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Init database with set of instructions
def init_db():
    db,c = get_db()
    for i in instructions:
        print(i)
        c.execute(i)
    db.commit()

#Create custom command to create database
@click.command('init_db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized')

#Initialize app
def init_app(app):
    app.teardown_appcontext(close_db) #When app is turn down, execute close_db
    app.cli.add_command(init_db_command) #Adding custom command to CLI