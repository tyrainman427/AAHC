# Project Title: Home Care Portal

## Overview
This app is a keeps tracks of Employees, Clients and New Hire Applications. Users can keep track of patients records and documentation. You can leave notes on each client as well.

## Technologies Used
- Django
- HTML/CSS
- JavaScript 
- Python
- AWS S3 Buckets

## Screenshots (if applicable)


## Demo
N/A

## Installation
1. **Download the repository:**

2. **Set up a virtual environment or install dependencies:**
- Create a virtual environment:
  ```
  python3 -m venv env
  ```
- Activate the virtual environment:
  - On Windows:
    ```
    env\Scripts\activate
    ```
  - On macOS and Linux:
    ```
    source env/bin/activate
    ```
- Install dependencies:
  ```
  pip3 install -r requirements.txt
  ```

## Configuration
4. **Set up environment variables:**
- Create a `.env` file in the project directory and add necessary environment variables:
  ```
  DEBUG=True
  SECRET_KEY=your_secret_key
  DATABASE_URL=your_database_url
  # Add other configuration variables as needed
  ```
- Update `settings.py` to load environment variables:
  ```python
  from dotenv import load_dotenv

  load_dotenv()
  ```

## Database Setup
 **Run migrations:**
 ```
  python3 manage.py makemigrations
  python3 manage.py migrate
 ```


## Usage
1. **Run the development server:**


2. **Access the project in your web browser at `http://localhost:8000`**

## What I Learned
This was a challenging project as I made multiple models and had to connect them all together to work and make sure each part of the app can communicate with eachother. I had to make notifications for Announcements which
was challenging as well and to this day I still need to work on this a little more. Using AWS for the first time was not too hard and I was able to store client documents and notes securely in S3 buckets.

## Challenges Faced
Most of them I explained earlier this was just one of those projects that was touch as a early coder but I made it work.

## Future Improvements
No plans at this moment unless it was needed.

## Contact Information
tyraineytech@gmail.com


