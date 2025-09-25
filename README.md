# Talent Bridge
## Skills Recommendation Service (Flask + MySQL)

---

## 🚀 Overview
Talent Bridge is a web-based skill recommendation service that allows users to manage their skills and get AI-powered suggestions for the next skill to learn. It uses Flask for the backend, MySQL for database management, and integrates the Gemini AI API for skill recommendations.

---

## 🛠️ Tech Stack
- Python (Flask)
- MySQL
- HTML/CSS/JS for frontend
- Gemini AI API (Google Generative AI)
- Pytest (for testing)

---

## 📂 Endpoints

### 1. Add User
`POST /user`  
Adds a new user to the database.

**Request Body:**
```json
{
  "name": "Alice",
  "skills": ["Python", "Java"],
  "learning_path": "Data Science"  // optional
}
````

**Response:**

```json
{
  "message": "User added successfully",
  "user_id": 1
}
```

---

### 2. Get Recommendations

`GET /recommend/<user_id>`
Fetches the next recommended skill for the user along with the learning path.

**Response:**

```json
{
  "id": [1],
  "name": ["Alice"],
  "learning_path": "Data Science",
  "next-skill": "Flask",
  "skills": ["Python", "Java"]
}
```

---

### 3. Get User Skills

`GET /skills/<user_id>`
Fetches the current skills and learning path of a user.

**Response:**

```json
{
  "id": [1],
  "name": ["Alice"],
  "learning_path": ["Data Science"],
  "skills": ["Python", "Java"]
}
```

---

### 4. Add Skill to Existing User

`POST /add_skills/<user_id>`
Adds a new skill to the existing user’s skill set.

**Request Body:**

```json
{
  "skills": ["Flask"],           // can be multiple skills
  "learning_path": "Data Science" // optional
}
```

**Response:**

```json
{
  "message": "Skills added for user 1",
  "skills": ["Python", "Java", "Flask"]
}
```

---

## 💻 Frontend

* Users can **add a new user**, **view current skills**, and **get recommendations**.
* The frontend provides an **“Add This Skill”** button that automatically updates the user’s skill set in the database.

---

## 🖼️ Visual Flow Diagram

```text
   +-----------+        +-----------+        +-----------+
   | Add User  | -----> |  MySQL DB | -----> | Gemini AI |
   +-----------+        +-----------+        +-----------+
         |                                    |
         |                                    |
         +----------> Frontend (HTML/JS) <----+
```

---

## 📸 Example Screenshots

**1️⃣ Add User Page**
![Add User](screenshots/add_user.png)

**2️⃣ Get Recommendations Page**
![Get Recommendations](screenshots/recommendation.png)

**3️⃣ Add Skill to Existing User**
![Add Skill](screenshots/add_skill.png)

> Replace the paths `screenshots/add_user.png` etc. with your actual screenshot files in a `screenshots/` folder.

---

## ⚡ Features

* AI-powered skill recommendation using Gemini API.
* Add and manage multiple skills per user.
* Interactive frontend with real-time updates.
* Full CRUD support for user skills.

---

## 📌 Setup Instructions

1. Clone the repository:

```bash
git clone <repo-url>
cd talent-bridge
```

2. Create a MySQL database and update `db.py` with your credentials.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open `http://127.0.0.1:5000/` in your browser.

---

## 📖 Future Enhancements

* User authentication and authorization.
* Display skill progression charts on the frontend.
* Email notifications for recommended skills.
* Integration with LinkedIn or GitHub for automatic skill import.

---

## 📝 License

This project is open-source and free to use.

```



