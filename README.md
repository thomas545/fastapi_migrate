FastAPI Migrations
=============

FastAPI Migrations is an extension that handles SQLAlchemy database migrations for FastAPI applications using Alembic. The database operations are provided as command-line arguments under the `fastmigrate` command.


Requirements
------------
- fastapi >= 0.78.0
- SQLAlchemy >= 1.4.37
- alembic >= 1.8.0
- typer >= 0.4.1

Installation
------------

Install FastAPI Migrations with `pip`:

    pip install fastapi_migrations

Example
-------

Steps to handles database migrations through FastAPI Migrations:
- Use `fastmigrate init` to generate the template and inialize the alembic template
- don't forget to import meta data to `env.py` file
- follow the FastAPI instructions to set the database configurations [reference](https://fastapi.tiangolo.com/advanced/sql-databases-peewee/)



Create the database or enable migrations if the database already exists with the following command:

    $ fastmigrate init

You can then generate an initial migration:

    $ fastmigrate migrate
    
The migration script needs to be reviewed and edited, as Alembic currently does not detect every change you make to your models. In particular, Alembic is currently unable to detect indexes. Once finalized, the migration script also needs to be added to version control.

Then you can apply the migration to the database:

    $ fastmigrate upgrade
    
Then each time the database models change repeat the `migrate` and `upgrade` commands.

To sync the database in another system just refresh the `migrations` folder from source control and run the `upgrade` command.

To see all the commands that are available run this command:

    $ fastmigrate --help

Resources
---------

- [Documentation]()
- [pypi]() 
