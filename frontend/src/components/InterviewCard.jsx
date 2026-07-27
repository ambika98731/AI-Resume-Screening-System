function InterviewCard({ interview }) {
    if (!interview || !interview.questions) return null;

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
            <h2>Interview Questions</h2>

            {Object.entries(interview.questions).map(([skill, questions]) => (
                <div key={skill} style={{ marginBottom: "20px" }}>
                    <h3>{skill.toUpperCase()}</h3>

                    <ol>
                        {questions.map((question, index) => (
                            <li key={index}>{question}</li>
                        ))}
                    </ol>
                </div>
            ))}
        </div>
    );
}

export default InterviewCard;