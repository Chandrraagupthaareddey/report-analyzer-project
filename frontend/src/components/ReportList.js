import React, { useState } from 'react';
import './ReportList.css'; // Import CSS for styling

// Functional component to render the list of reports
function ReportList() {
  // State to store uploaded file and report data
  const [file, setFile] = useState(null);
  const [reports, setReports] = useState([]);

  // Function to handle file upload
  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    setFile(uploadedFile);

    // Parse and process the uploaded file here (e.g., read content, send to backend)
    // Update the 'reports' state with parsed report data
    // Example:
    // fetch('/upload', {
    //   method: 'POST',
    //   body: uploadedFile
    // }).then(response => response.json())
    //   .then(data => setReports(data.reports))
  };

  return (
    <div className="report-list">
      <h2>Medical Reports</h2>
      {/* File upload input */}
      <input type="file" accept=".pdf" onChange={handleFileUpload} />

      {/* Render uploaded reports */}
      <ul>
        {reports.map((report, index) => (
          <li key={index}>
            <h3>{report.title}</h3>
            <p>Date: {report.date}</p>
            <p>Status: {report.status}</p>
            {/* Add more details as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReportList;