function InterviewCard({ interview }) {
    if (!interview || !interview.questions) return null;

    return (
        <div className="card">

            <h2>Interview Questions</h2>

            {Object.entries(interview.questions).map(([skill, questions]) => (
                <div key={skill}>
                    <h3>{skill.toUpperCase()}</h3>

                    <ol>
                        {questions.map((q, index) => (
                            <li key={index}>{q}</li>
                        ))}
                    </ol>
                </div>
            ))}
        </div>
    );
}

export default InterviewCard;