# Postgres Pub-Sub

Playing around with the magic of Postgres found [here](https://layerci.com/blog/postgres-is-the-answer/).

This project listens to two different messages from the Postgres DB.

## Getting Started

* Create a database named `dump`, you can name it anything but make sure you change the name in the script below.

* Run the command below to execute the `sample.psql` sql file. Replace the `username` with your DB username also. Also run the command in the root of the project.

```bash
psql --username=testuser --password --dbname=dump --file=sample.psql
```

* Once that is successful, open the `dump` DB in your favorite database GUI - I recommend [Postico](https://eggerapps.at/postico/) or [TablePlus](https://tableplus.com/).

![PosticoScreenShot](https://github.com/BolajiOlajide/postgres-pub-sub/blob/master/pg_pubsub.png?raw=true)

## Installation

You can decide to run the Python script or Node script or both. They both listen to two different events so to enjoy the sweetness, you should run both. Python script requires a python3 interpreter.

* Install the python dependencies with the command

```sh
pip install -r requirements.txt
```

* Install the node dependencies with the command

```sh
yarn
```

* Start the python script with the command

```sh
python3 main.py
```

* Start the node script with the command

```sh
node index.js
```

### PubSub in action

The Python script listens to an event called `ci_jobs_status_channel` which is triggered when you insert or update the status of a row in the table `ci_jobs`.

The node script listens to an event called `new_stuff` which is triggered when you insert or update an id of a row in the table `ci_jobs`.

![PGPubsub in Action](https://github.com/BolajiOlajide/postgres-pub-sub/blob/master/pgpubsub.gif?raw=true)
