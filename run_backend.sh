#!/bin/bash

echo "running python server.."

export FLASK_APP=main_run
export FLASK_ENV=development
flask run

