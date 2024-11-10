const taskList = document.getElementById("taskList");

        function addTask() {
            const taskInput = document.getElementById("taskInput");
            const taskText = taskInput.value.trim();
            if (taskText === "") {
                alert("Please enter a task.");
                return;
            }

            const taskItem = document.createElement("li");
            const taskContent = document.createElement("span");
            taskContent.textContent = taskText;
            taskItem.appendChild(taskContent);

            const completeButton = document.createElement("button");
            completeButton.textContent = "Complete";
            completeButton.onclick = () => taskItem.classList.toggle("completed");

            const deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.onclick = () => taskList.removeChild(taskItem);

            taskItem.appendChild(completeButton);
            taskItem.appendChild(deleteButton);
            taskList.appendChild(taskItem);
            taskInput.value = "";
        }

        function filterTasks(filter) {
            const tasks = taskList.getElementsByTagName("li");
            for (let task of tasks) {
                if (filter === "all") {
                    task.style.display = "";
                } else if (filter === "completed") {
                    task.style.display = task.classList.contains("completed") ? "" : "none";
                } else if (filter === "pending") {
                    task.style.display = task.classList.contains("completed") ? "none" : "";
                }
            }
        }