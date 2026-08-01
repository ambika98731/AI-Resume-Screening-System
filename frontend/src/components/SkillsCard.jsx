function SkillsCard({ matching }) {
    if (!matching) return null;

    return (
        <div className="card">
            <h2>Skills Analysis</h2>

                <div className="two-column">

                <div className="column">

                    <h3>✅ Matched Skills</h3>

                    <ul>

                        {matching.matched_skills.map((skill) => (
                            <li
                                key={skill}
                                className="skill-good"
                            >
                                {skill}
                            </li>
                        ))}

                    </ul>

                </div>

                <div className="column">

                    <h3>❌ Missing Skills</h3>

                    <ul>

                        {matching.missing_skills.map((skill) => (
                            <li
                                key={skill}
                                className="skill-bad"
                            >
                                {skill}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

    

export default SkillsCard;