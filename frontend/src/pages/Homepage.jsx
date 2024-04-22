import { useEffect, useState } from "react";
import TaskList from "../components/TaskList";
import { fetchTasks } from "../api/task";

function Homepage() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchTasks()
      .then((res) => {
        setTasks(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return <TaskList tasks={tasks} />;
}

export default Homepage;
