## FlowerCare App
### [Live Site](https://grisha-careers-website-v4.onrender.com/)

<img width="1061" alt="Grisha careers" src="https://user-images.githubusercontent.com/102157344/229812394-83742af3-5ea1-4f3d-ab20-aecfeac52cd1.png">

## Introduction
This is a code repository for creating a company website page with a full display of available vacancies.

You can register and submit an application, as well as constantly monitor its status.

Anyone with Administrator rights can update the status of submitted applications.





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
