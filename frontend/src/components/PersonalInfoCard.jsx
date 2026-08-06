function PersonalInfoCard({ personalInfo }) {
    if (!personalInfo) return null;

    return (
        <div className="card">
            <h2>Personal Information</h2>

            <p><strong>Name:</strong> {personalInfo.name || "Not Found"}</p>

            <p><strong>Email:</strong> {personalInfo.email || "Not Found"}</p>

            <p><strong>Phone:</strong> {personalInfo.phone || "Not Found"}</p>

            <p><strong>LinkedIn:</strong> {personalInfo.linkedin || "Not Found"}</p>

            <p><strong>GitHub:</strong> {personalInfo.github || "Not Found"}</p>

            <p><strong>Location:</strong> {personalInfo.location || "Not Found"}</p>
        </div>
    );
}

export default PersonalInfoCard;