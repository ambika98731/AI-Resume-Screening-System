function ProjectsCard({ projects }) {
    if (!projects || projects.length === 0) {
        return null;
    }

    return (
        <div className="card">

            <h2>Projects</h2>

            {projects.map((project, index) => (

                <div
                    key={index}
                    className="project-card"
                >

                    <h3>{project.title}</h3>

                    <p>{project.description}</p>

                </div>

            ))}

        </div>
    );
}

export default ProjectsCard;