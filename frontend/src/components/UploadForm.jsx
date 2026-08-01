import { useState } from "react";
import api from "../services/api";

function UploadForm({ setResult }) {
    const [resumeText, setResumeText] = useState("");
    const [jobDescription, setJobDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await api.post("/match", {
                resume_text: resumeText,
                job_description: jobDescription,
            });

            setResult(response.data);
        } catch (error) {
            console.error(error);
            alert("Failed to analyze resume.");
        }
    };

    return (
        <form className="card" onSubmit={handleSubmit}>

            <h2>Resume</h2>

            <textarea
                className="textarea"
                placeholder="Paste your resume here..."
                rows="8"
                value={resumeText}
                onChange={(e) => setResumeText(e.target.value)}
            />

            <h2>Job Description</h2>

            <textarea
                className="textarea"
                placeholder="Paste the job description here..."
                rows="8"
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
            />

            <button className="button" type="submit">
                Analyze Resume
            </button>

        </form>
    );
}

export default UploadForm;