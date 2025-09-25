import re
from flask import Flask, request, jsonify, render_template
import mysql
from db import get_connection
import google.generativeai as genai
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/user", methods=["POST"])
def add_user():
    data = request.json
    name = data["name"]
    skills = ",".join(data.get("skills", []))
    learning_path = data.get("learning_path", "")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, skills, learning_path) VALUES (%s, %s, %s)",
        (name, skills, learning_path),
    )
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({"message": "User added successfully", "user_id": user_id}), 201


@app.route("/recommend/<int:user_id>", methods=["GET"])
def recommend(user_id):
    # Configure Gemini API
    genai.configure(api_key="")
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    # Fetch user data from DB
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT skills, learning_path,name,id FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user_skills = user["skills"].split(",") 
    name = user["name"]
    learning_path = user["learning_path"]

    prompt = f"""
    You are an AI career coach.
    I will give you a list of technical skills that a user already has.
    Optionally, I may also provide a preferred learning path (like "Data Science", "Web Development", or "Cloud").

    Your task:
    - Suggest ONE most valuable next skill.
    - Always return both the Learning Path and the Skill in JSON format.
    - If the Learning Path is provided, keep it and only suggest the skill.
    - If the Learning Path is empty, suggest both a suitable Learning Path and a Skill.
    - If both User Skills and Learning Path are empty, suggest both a suitable Learning Path and a starting Skill.

    Format strictly as JSON:
    {{
        "learning_path": "<learning_path>",
        "recommendation": "<skill>"
    }}

    User skills: {user_skills}
    Learning path: {learning_path}
    """
    print(prompt)
    response = model.generate_content(prompt)

    response = model.generate_content(prompt)

    raw_output = response.text.strip()
    print(raw_output)
    cleaned = re.sub(r"^```(?:json)?|```$", "", raw_output, flags=re.MULTILINE).strip()

    result = json.loads(cleaned)
    print(result["learning_path"])
    print(result["recommendation"])

    return jsonify({
    "id":[user_id],  
    "name" : [name], 
    "learning_path": result["learning_path"],
    "next-skill": result["recommendation"],
    "skills" : [user_skills]
    })

@app.route("/skills/<int:user_id>", methods=["GET"])
def skills(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT skills, learning_path, name, id FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    print(user)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_skills = user["skills"].split(",") if user["skills"] else []
    learning_path = user["learning_path"]
    name = user["name"]
    return jsonify({
    "id":[user_id],  
    "name" : [name], 
    "learning_path": [learning_path],
    "skills" : [user_skills]
    })


@app.route("/add_skills/<int:user_id>", methods=["POST"])
def add_skills(user_id):
    data = request.json
    new_skill = data.get("skills")            # always a string
    learning_path = data.get("learning_path") # optional

    if not new_skill:
        return jsonify({"error": "No skill provided"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)  # dictionary=True for MySQL, adjust if using another DB

        # Fetch current skills
        cursor.execute("SELECT skills FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Convert skills string to list, handle empty skills
        current_skills = user["skills"].split(",") if user["skills"] else []

        # Strip spaces and avoid duplicate
        current_skills = [s.strip() for s in current_skills]
        if new_skill not in current_skills:
            current_skills.append(new_skill)

        # Convert back to comma-separated string
        skills_str = ",".join(current_skills)

        # Update DB
        cursor.execute(
            "UPDATE users SET skills=%s, learning_path=%s WHERE id=%s",
            (skills_str, learning_path, user_id)
        )
        conn.commit()

        return jsonify({
            "message": "Skill added successfully",
            "user_id": user_id,
            "skills": current_skills,
            "learning_path": learning_path
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)