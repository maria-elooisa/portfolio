let currentProjectIndex = 0;
const projects = document.querySelectorAll('.projects');

function showProject(index) {
    projects.forEach((project, i) => {
        project.style.display = i === index ? 'flex' : 'none';
    });
}

function prevProject() {
    currentProjectIndex = (currentProjectIndex > 0) ? currentProjectIndex - 1 : projects.length - 1;
    showProject(currentProjectIndex);
}

function nextProject() {
    currentProjectIndex = (currentProjectIndex < projects.length - 1) ? currentProjectIndex + 1 : 0;
    showProject(currentProjectIndex);
}

// Inicializar a visualização do primeiro projeto
showProject(currentProjectIndex);

// Função da sessão Skills
function toggleDescription(card) {
    card.classList.toggle('flipped');
}