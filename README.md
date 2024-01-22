#Instructions

##run following commands:

```
    chmod +x run_frontend.sh
    chmod +x run_backend.sh
```

##Open a terminal and run:

```
    ./run_backend.sh
```

##Open another terminal and run:

```
    ./run_frontend.sh
```

###Open a web browser on the url provided by above the command when run. Keep console open to check if any errors occur like CORS error.If any cors or https error happens in console, then you have to use ngrok

##For ngrok, use:

```
    ngrok http 5000
```
###Copy the https url generated by ngrok into the frontend/js/main.js file and refresh the browser.
