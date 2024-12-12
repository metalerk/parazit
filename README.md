# Parazit

![parazit_log](/_assets/parazit_logo.jpg)

Reverse shell generator.

This project was created for the GDL BSides 2020 conference.

[BSides GDL 2020 Conference Video](https://www.facebook.com/BSidesGDL/videos/376897363393242)

# Quickstart
## Install (Linux/OSX)

**Dependencies**
- Python 3.7+
- virtualenv
- netcat

For install open a terminal and type the following commands:

```sh
virtualenv -p python3 env/
source env/bin/activate
pip install requirements.txt
```

### Generating client
```sh
python app.py
```

You'll find the standalone executable inside the just created directory `dist` named as `client`.

Type in your machine:
```sh
nc -l 4444
```
Run the standalone executable in the client machine.
<br/>
If everything went fine, a banner with client machine system info will be displayed.    