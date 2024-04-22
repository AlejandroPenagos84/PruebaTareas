import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import TaskForm from "./pages/TaskForm";
import Homepage from "./pages/Homepage";
import NavBar from "./components/NavBar";
function App() {
  return (
    <>
      <BrowserRouter>
        <div className="container mx-auto px-10">
          <NavBar/>
          <Routes>
            <Route path="/" element={<Homepage />} />
            <Route path="/tasks/new" element={<TaskForm />} />
            <Route path="/tasks/:id" element={<TaskForm />} />
          </Routes>
        </div>
      </BrowserRouter>
    </>
  );
}

export default App;
