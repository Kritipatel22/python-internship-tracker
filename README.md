# Internship & Job Application Tracker (Python + MySQL)

A command-line based application to manage internship and job applications using Python and MySQL.  
Built to track deadlines, statuses, companies, and insights in one place.

---

## 🚀 Features

### Core Functionalities
- Add, view, update, and delete applications  
- Search by company, status, and title keyword  
- Sort by deadline, company name, or status  
- Export all applications to CSV  
- Dashboard summary with insights  

### Technical Enhancements
- Input validation for clean data  
- Complete logging (`tracker.log`) for debugging  
- Colored CLI interface for better readability  
- Modular code structure (`app.py`, `db.py`)  

---

## 🛠 Tech Stack
- **Python**
- **MySQL**
- **mysql-connector-python**
- **Colorama**
- **Tabulate**
- **CSV handling**
- **Logging module**

---

## 📂 Project Structure
```
python-internship-tracker/
│
├── app.py              # Main CLI application
├── db.py               # Database functions and connection
├── tracker.log         # Log file (auto-generated)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository
git clone https://github.com/Kritipatel22/python-internship-tracker.git

cd python-internship-tracker

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ MySQL Setup
Create the database and table:

```
sql
CREATE DATABASE internship_tracker;

USE internship_tracker;

CREATE TABLE applications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    company VARCHAR(100),
    status VARCHAR(50),
    deadline DATE,
    link TEXT,
    notes TEXT
);

```

### 4️⃣ Update database credentials
Inside db.py:

user="root",
password="YOUR_PASSWORD",

▶️ Running the Application

python app.py

```

### This Application can:

1.Manage applications

2.View summaries

3.Export to CSV

4.Track logs

5.Validate inputs

```

👤 Developer

Kriti Patel
MSc IT @ DAIICT
