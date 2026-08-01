import { useState } from "react";

function UploadForm({ onAnalyze }) {
    const [resumeFile, setResumeFile] = useState(null);
    const [jdFile, setJdFile] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!resumeFile || !jdFile) {
            alert("Please select both PDF files.");
            return;
        }

        onAnalyze(resumeFile, jdFile);
    };

    return (
        <div className="card">

            <h2>Upload Documents</h2>

            <form onSubmit={handleSubmit}>

                <label>
                    Resume (PDF)
                </label>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) => setResumeFile(e.target.files[0])}
                />

                <label>
                    Job Description (PDF)
                </label>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) => setJdFile(e.target.files[0])}
                />

                <button type="submit">
                    Analyze Resume
                </button>

            </form>

        </div>
    );
}

export default UploadForm;