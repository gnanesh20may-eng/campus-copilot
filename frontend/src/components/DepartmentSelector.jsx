import React from "react";

export default function DepartmentSelector({
  department,
  subgroup,
  onDepartmentChange,
  onSubgroupChange,
  subgroupsByDepartment,
}) {
  const subgroupOptions = subgroupsByDepartment[department] || [];

  return (
    <div style={{ display: "grid", gap: 12, marginBottom: 24 }}>
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
        <label style={{ display: "flex", flexDirection: "column", flex: "1 1 220px" }}>
          Department
          <select
            value={department}
            onChange={(e) => onDepartmentChange(e.target.value)}
            style={{ padding: 10, borderRadius: 8, border: "1px solid #d1d5db" }}
          >
            {Object.keys(subgroupsByDepartment).map((dept) => (
              <option key={dept} value={dept}>
                {dept}
              </option>
            ))}
          </select>
        </label>

        <label style={{ display: "flex", flexDirection: "column", flex: "1 1 220px" }}>
          Subgroup
          <select
            value={subgroup}
            onChange={(e) => onSubgroupChange(e.target.value)}
            style={{ padding: 10, borderRadius: 8, border: "1px solid #d1d5db" }}
          >
            {subgroupOptions.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
      </div>
      <p className="small">
        Select the department and subgroup that should guide the chat context.
      </p>
    </div>
  );
}
