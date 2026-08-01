function InterviewCard({ interview }) {
    if (!interview || !interview.questions) return null;

    return (
        <div className="card">

            <h2>Interview Questions</h2>

            <div className="interview-grid">

                {Object.entries(interview.questions).map(([skill, questions]) => (

                    <div
                        key={skill}
                        className="interview-skill-card"
                    >

                        <h3 className="interview-skill-title">
                            {skill.toUpperCase()}
                        </h3>

                        <ol className="question-list">

                            {questions.map((q, index) => (

                                <li
                                    key={index}
                                    className="question-item"
                                >
                                    {q}
                                </li>

                            ))}

                        </ol>

                    </div>

                ))}

            </div>

        </div>
    );
}

export default InterviewCard;