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
<img width="1257" alt="Screenshot 2024-06-02 at 11 33 34 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/8da52ec4-cd36-4a0e-890f-bb8d689ecf67">
<img width="690" alt="Screenshot 2024-06-02 at 11 33 24 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/29e8bc75-5174-46ce-b453-2bbfc1e140a1">
<img width="1501" alt="Screenshot 2024-06-02 at 11 33 12 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/3e1f28cf-3df8-4771-89b8-2e3a5abf16ef">
<img width="1500" alt="Screenshot 2024-06-02 at 11 32 43 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/043ff8e9-4524-4d56-8e4d-23e49cad7af6">
<img width="1494" alt="Screenshot 2024-06-02 at 11 32 27 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/134f984c-74f4-4031-8aa4-1d9a64189655">
<img width="1487" alt="Screenshot 2024-06-02 at 11 31 44 PM" src="https://github.com/tyrainman427/AAHC/assets/61444675/7ecc7631-46a2-45a7-8a8e-49ae6344a631">


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


