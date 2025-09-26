      // Add User
      document.getElementById("userForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const name = document.getElementById("name").value;
        const skills = document.getElementById("skills").value.split(",");
        const learning_path = document.getElementById("learning_path").value;

        const response = await fetch("/user", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, skills, learning_path })
        });

        const data = await response.json();
        document.getElementById("addUserResult").innerHTML = `<p>User Added! ID: ${data.user_id}</p>`;
      });

      // Get Recommendations
      document.getElementById("recommendForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const userId = document.getElementById("recommendUserId").value;

        if (userId <= 0) {
          document.getElementById("recommendResult").innerHTML = `<p class="error">User ID should be greater than 0.</p>`;
          return;
        }

        const response = await fetch(`/recommend/${userId}`);
        const data = await response.json();

        if (data.learning_path === undefined) {
          document.getElementById("recommendResult").innerHTML = `<p class="error">User with ID ${userId} not found.</p>`;
        } else {
          document.getElementById("recommendResult").innerHTML = `
            <p><b>Learning Path:</b> ${data.learning_path}</p>
            <p><b>Next Skill:</b> ${data["next-skill"]} 
              <button onclick="addSkill(${userId}, ${data.learningPath}, '${data["next-skill"]}')">Add Skill</button>
            </p>
            <p><b>Current Skills:</b> ${data.skills.join(", ")}</p>
          `;
        }
      });

      // Add recommended skill to user
      async function addSkill(userId, learningPath, skill) {
        // const response = await fetch(`/skills/${userId}`);
        // const data = await response.json();
        // let currentSkills = data.skills;
        // currentSkills.push(skill);

        // const learningPath = data.learning_path[0] || "";
        // console.log(currentSkills)
        const update = await fetch(`/add_skills/${userId}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ skills: skill, learning_path: learningPath })
        });

        const updated = await update.json();
        alert("Skill added successfully!");
        // Optionally refresh recommendation section
        document.getElementById("recommendForm").dispatchEvent(new Event("submit"));
      }

      // Get User Details
      document.getElementById("userDetailsForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const userId = document.getElementById("detailsUserId").value;

        const response = await fetch(`/skills/${userId}`);
        const data = await response.json();

        if (data.skills === undefined) {
          document.getElementById("userDetailsResult").innerHTML = `<p class="error">User not found.</p>`;
        } else {
          document.getElementById("userDetailsResult").innerHTML = `
            <p><b>User ID:</b> ${userId}</p>
            <p><b>Name:</b> ${data.name[0]}</p>
            <p><b>Learning Path:</b> ${data.learning_path[0]}</p>
            <p><b>Skills:</b> ${data.skills.join(", ")}</p>
          `;
        }
      });
