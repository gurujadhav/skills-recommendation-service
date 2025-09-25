import google.generativeai as genai

genai.configure(api_key="AIzaSyCh6m3BL5fg7u4-b3iIpK7lNByqpLoSvB4")

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """You are an AI career coach. 
I will give you a list of technical skills that a user already has. 
Optionally, I may also provide a preferred learning path (like "Data Science", "Web Development", or "Cloud"). 

Your task:
- Suggest ONE most valuable next Programming skill.
- Always return both the Learning Path and the Programming Skill.
- If the Learning Path is provided, keep it and only suggest the Programming skill.
- If the Learning Path is empty, suggest both a suitable Learning Path and a Programming Skill.
- If both User Programming Skills and Learning Path are empty, suggest both a suitable Learning Path and a starting Skill.

Format your response strictly as:
Learning Path: <learning_path>
Skill: <skill>

User skills: None
Learning path: None
"""
response = model.generate_content(prompt)
print(response.text.strip())
