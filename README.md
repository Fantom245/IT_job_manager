![Logo of the project](https://raw.githubusercontent.com/jehna/readme-best-practices/master/sample-logo.png)

# IT_job_manager
> Best tasks manager

The project was created to simplify the workflow in companies. Create projects, add teams to them and assign tasks to employees.

## Installation / Getting Started

Follow these steps to quickly get the project up and running and start working with the blog platform:

1. Clone the project repository:

    ```bash
    git clone https://github.com/Fantom245/IT_job_manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd IT_job_manager
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:

    ```bash
    DJANGO_SETTINGS_MODULE=it_job_manager.settings.dev python manage.py migrate
    ```

5. Run the server:

    ```bash
    DJANGO_SETTINGS_MODULE=it_job_manager.settings.dev python manage.py runserver
    ```

After that, you can access the application at: `http://127.0.0.1:8000/`.

If you need to go to the admin panel, use the command:

    ```bash
    DJANGO_SETTINGS_MODULE=it_job_manager.settings.dev python manage.py loaddata dump.json
    ```
And use to log in
> username: admin.user
> password: asas24800

## Building

If your project requires additional steps to build or configure the environment after code changes, you can use the provided `build.sh` script.

1. Make the script executable (if it's not already):

    ```bash
    chmod +x build.sh
    ```

2. Run the script:

    ```bash
    ./build.sh
    ```

### What happens here:
- `chmod +x build.sh` makes the script executable if it wasn't already.
- `./build.sh` runs the script, which automatically executes the necessary commands to set up the environment, apply migrations, collect static files, etc.

This script may include steps like applying migrations, installing dependencies, setting up environment variables, or any other project-specific configuration tasks.

### Deploying / Publishing

To deploy this project to a production server, follow these steps:

1. Set up the production environment and install the necessary dependencies on the server:

    ```bash
    pip install -r requirements.txt
    ```

2. Set the Django settings to production:

    ```bash
    export DJANGO_SETTINGS_MODULE=it_job_manager.settings.production
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Collect static files for production:

    ```bash
    python manage.py collectstatic --noinput
    ```

5. Restart your web server (for example, Gunicorn or uWSGI):

    ```bash
    sudo systemctl restart gunicorn
    ```

6. Make sure everything is up and running by visiting your project URL.

## Features

This project offers the following features:

* User registration and authentication
* Creating, editing, and deleting blog posts
* Commenting on posts
* Categorizing posts into different categories
* Admin interface for managing posts and users
* Search functionality to find posts by title or content

If you want to extend the functionality, you can also:

* Add user profiles with the ability to upload avatars
* Implement a tagging system for posts
* Add support for rich text formatting in posts


## Link to deployed project
https://it-job-manager.onrender.com/
