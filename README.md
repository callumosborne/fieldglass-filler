# Fieldglass Filler

It will automatcially fill in the fieldglass as working 8 standard hours a day for 5 days a week, 9am until 5pm. It will then submit it for approval.

### Within a Mac or Linux terminal:

```bash
git clone https://github.com/callum-osborne/fieldglass-filler
```

```bash
cd fieldglass-filler
```

Install this package, it allows python to create its own browser. 

For Mac OS:
```bash
brew install geckodriver
```

For Linux systems:
```bash
sudo apt-get install firefox-geckodriverr
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

