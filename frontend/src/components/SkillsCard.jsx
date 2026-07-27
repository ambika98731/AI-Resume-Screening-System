function SkillsCard({ matching }) {
    if (!matching) return null;

    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "20px",
                marginTop: "20px",
                backgroundColor: "#ffffff",
            }}
        >
            <h2>Skills Analysis</h2>

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    gap: "40px",
                }}
            >
                <div style={{ flex: 1 }}>
                    <h3>✅ Matched Skills</h3>

                    <ul>
                        {matching.matched_skills.length > 0 ? (
                            matching.matched_skills.map((skill, index) => (
                                <li key={index}>{skill}</li>
                            ))
                        ) : (
                            <li>No matched skills</li>
                        )}
                    </ul>
                </div>

                <div style={{ flex: 1 }}>
                    <h3>❌ Missing Skills</h3>

                    <ul>
                        {matching.missing_skills.length > 0 ? (
                            matching.missing_skills.map((skill, index) => (
                                <li key={index}>{skill}</li>
                            ))
                        ) : (
                            <li>No missing skills</li>
                        )}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default SkillsCard;