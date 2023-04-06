## FlowerCare App

<img width="746" alt="flowerapp" src="https://user-images.githubusercontent.com/102157344/230329946-7ed9359c-0452-4883-a81a-c92244ffe58f.png">

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
