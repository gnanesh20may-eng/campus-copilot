import React, { useState } from "react";
import UploadPage from "./pages/Upload";
import ChatPage from "./pages/Chat";
import DepartmentSelector from "./components/DepartmentSelector";

const subgroupsByDepartment = {
  Admissions: ["Undergraduate", "Graduate", "Financial Aid"],
  Academics: ["Courses", "Schedules", "Policies"],
  "Student Life": ["Housing", "Clubs", "Events"],
};

export default function App() {
  const [route, setRoute] = useState("upload"); // default to upload for quick ingestion
  const [department, setDepartment] = useState(Object.keys(subgroupsByDepartment)[0]);
  const [subgroup, setSubgroup] = useState(subgroupsByDepartment[department][0]);

  function handleDepartmentChange(nextDepartment) {
    setDepartment(nextDepartment);
    setSubgroup(subgroupsByDepartment[nextDepartment][0]);
  }

  return (
    <div className="container">
      <div className="header">
        <h1>Campus Copilot</h1>
        <div className="nav">
          <button
            className={`button ${route === "upload" ? "primary" : ""}`}
            onClick={() => setRoute("upload")}
          >
            Upload
          </button>
          <button
            className={`button ${route === "chat" ? "primary" : ""}`}
            onClick={() => setRoute("chat")}
          >
            Chat
          </button>
        </div>
      </div>

      <div className="card">
        {route === "chat" && (
          <DepartmentSelector
            department={department}
            subgroup={subgroup}
            onDepartmentChange={handleDepartmentChange}
            onSubgroupChange={setSubgroup}
            subgroupsByDepartment={subgroupsByDepartment}
          />
        )}
        {route === "upload" ? <UploadPage /> : <ChatPage department={department} subgroup={subgroup} />}
      </div>
    </div>
  );
}
