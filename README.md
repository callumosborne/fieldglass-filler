# Fieldglass Filler

It will automatcially fill in the fieldglass as working 8 standard hours a day for 5 days a week, 9am until 5pm. It will then submit it for approval.

### Within mac terminal:

```bash
git clone https://github.com/callum-osborne/fieldglass-filler
```

```bash
cd fieldglass-filler
```

Install this Mac OS package, it allows python to control the browser.
```bash
brew install geckodriver
```

### Install library:

```bash
pip install selenium
```

Put your username and password into the login.txt file:
* replace usernameHere with your username
* replade passwordHere with your password

### Run the python script:
If you run into an error with an import run python3...

```bash
python run.py
```

or 

```bash
python3 run.py
```

