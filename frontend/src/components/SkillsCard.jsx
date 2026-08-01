function SkillsCard({ matching }) {
    if (!matching) return null;

    return (
        <div className="card">

            <h2>Skills Analysis</h2>

            <div className="two-column">

                <div className="column">

                    <h3>✅ Matched Skills</h3>

                    <div className="skill-container">

                        {matching.matched_skills.length > 0 ? (
                            matching.matched_skills.map((skill) => (
                                <span
                                    key={skill}
                                    className="skill-chip skill-good"
                                >
                                    {skill}
                                </span>
                            ))
                        ) : (
                            <p>No matched skills.</p>
                        )}

                    </div>

                </div>

                <div className="column">

                    <h3>❌ Missing Skills</h3>

                    <div className="skill-container">

                        {matching.missing_skills.length > 0 ? (
                            matching.missing_skills.map((skill) => (
                                <span
                                    key={skill}
                                    className="skill-chip skill-bad"
                                >
                                    {skill}
                                </span>
                            ))
                        ) : (
                            <p className="success-text">
                                🎉 No missing skills!
                            </p>
                        )}

                    </div>

                </div>

            </div>

        </div>
    );
}

export default SkillsCard;