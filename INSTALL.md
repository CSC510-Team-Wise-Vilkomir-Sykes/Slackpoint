# How to set up everything

## Required applications
1. Download and install [Python](https://www.python.org/downloads/)
   - Python 3.13 was used for this project, but older versions may work as well.

2. Download and install [Postgres](https://www.postgresql.org/download/)
   - Note the password you set for the postgres user, you will need it later in .env

3. (for local development) Download and install [ngrok](https://ngrok.com/download)
   - This is used to expose your local server to the internet for Slack to interact with it.

4. (optional) Download and install [pgAdmin 4](https://www.pgadmin.org/download/) if not already installed by postgres or whichever database management tool you prefer.


## Setting up the code locally
1. Clone the repository
   - via HTTPS: `git clone https://github.com/CSC510-Team-Wise-Vilkomir-Sykes/Slackpoint.git`
   - via SSH: `git clone git@github.com:CSC510-Team-Wise-Vilkomir-Sykes/Slackpoint.git`

2. Navigate to the project directory
   - `cd Slackpoint`

3. (optional but highly recommended) Create a virtual environment
   - `pip install virtualenv`
   - `python -m venv slackpoint_venv`
   - `source slackpoint_venv/bin/activate` (Linux/Mac/WSL)
   - `slackpoint_venv\Scripts\activate` (Windows)

4. Install the required packages
   - `pip install -r requirements.txt`
   - *In the event psycopg2 fails to install, you may need to install it manually
     - Follow the instructions [here](https://github.com/psycopg/psycopg2) to install it manually using setup.py

5. Rename the .env.example file to .env
   - `mv .env.example .env` (Linux/Mac/WSL)
   - `ren .env.example .env` (Windows)

6. Setup database
   - Add the password you set for the postgres user to the .env file
     - For now, ignore the rest of the file as that is done in the Slack section


## Setting up ngrok
1. Create an account on ngrok
   - Go to [ngrok](https://dashboard.ngrok.com/signup) and create an account

2. Get your authtoken
   - Go to [ngrok](https://dashboard.ngrok.com/get-started/setup) and copy your authtoken
   - Run `ngrok authtoken <your authtoken>`

3. Setup a subdomain
   - Go to [ngrok](https://dashboard.ngrok.com/endpoints/domains) and setup a subdomain
   - This will allow you to have a consistent URL for your server otherwise it will change every time you run ngrok


## Setting up Slack

0. Create a new Slack workspace
   - Go to [Slack](https://slack.com/get-started#/create) and create a new workspace

1. Create a new Slack app
   - Go to [Slack API](https://api.slack.com/apps) and click on "Create New App"
   - Name your app and select the workspace you want to use
   - Click on "Create App"

2. Navigate to Interactivity & Shortcuts in the sidebar
   - Enable interactivity and enter the ngrok URL you got earlier followed by `/slack/interactive-endpoint` in the "Request URL" field
     - For example: `https://enter-your-subdomain.ngrok-free.app/slack/interactive-endpoint`
   - Click on Save Changes

3. Navigate to Slash Commands in the sidebar
   - Click on "Create New Command"
   - Enter the commands, request URLs, and short description for each of the commands in the application:
     - Command: `/COMMAND`
     - Request URL: `https://enter-your-subdomain.ngrok-free.app/ENDPOINT`
     - Short Description: `DESCRIPTION`

4. Navigate to OAuth & Permissions in the sidebar and scroll down to Scopes
   - Add the following Bot Token Scopes:
     - `channels:join`
     - `channels:read`
     - `chat:write`
     - `commands`

5. Navigate to OAuth & Permissions in the sidebar
   - Click on "Install to Workspace"
   - Click on "Allow"

6. Navigate to OAuth & Permissions in the sidebar
   - Copy the Bot User OAuth Token and add it to the .env file
     - `SLACK_BOT_TOKEN=xoxb-...`

7. Navigate to Basic Information in the sidebar
   - Copy the Signing Secret and add it to the .env file
     - `SLACK_SIGNING_SECRET=...`
   - Copy the Verification Token and add it to the .env file
     - `VERIFICATION_TOKEN=...`


## Running the code

1. Start the ngrok server
   - `ngrok http --url=enter-your-subdomain.ngrok-free.app 5000`

2. (first time only) Setup the database
   - `flask shell`
   - Run `db.create_all()`
   - Run `quit()`

3. Start the Flask server
   - `flask run`