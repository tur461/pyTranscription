#!/bin/bash

echo "Running frontend.."

echo "Note: ensure you are using python 3 or above"

echo "after this works, open http://localhost:8888/index.html in browser" 

cd frontend
python -m http.server 8888

