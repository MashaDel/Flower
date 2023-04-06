## FlowerCare App

<img width="761" alt="Снимок экрана 2023-04-06 в 11 50 11" src="https://user-images.githubusercontent.com/102157344/230328991-864cba6a-1379-4932-8dcf-6755c02e0065.png">

## Introduction
  This is a code repository for creating a house flower care widget.

  Thanks to this application, the user can look at which side of the world it is preferable to place the flower selected by the User, when it is better to water it, depending on the date of the last watering (which the User sets himself) and in which month flowering can be expected.





## How to prepare and run App

### Prerequisites

#### macOS

1. Install the latest version of `python-tk`

```bash
brew install python-tk@3.11 
```

1. Clone the repo and change to the repo directory

```bash
cd /tmp && git clone https://github.com/<user>/<repo>.git && cd /tmp/<repo>
```

1. Create Python virtual environment, update `pip`, and install dependencies

```bash
python3 -m venv ./venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip pip install -r requirements.txt
```

### Run App

* Use the following command to run the App

```bash
/tmp/<repo>/venv/bin/python /tmp/<repo>/app.py
