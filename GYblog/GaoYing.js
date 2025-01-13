document.addEventListener('DOMContentLoaded', function() {
    // Dynamic skill addition for About page
    const skillsContainer = document.getElementById('skills-container');
    if (skillsContainer) {
        const skills = [
            'Programming Languages',
            'Data Analysis',
            'Research Methodologies',
            'Project Management'
        ];

        skills.forEach(skill => {
            const skillBadge = document.createElement('span');
            skillBadge.classList.add('badge', 'bg-primary', 'me-2', 'mb-2');
            skillBadge.textContent = skill;
            skillsContainer.appendChild(skillBadge);
        });

        skillsContainer.style.opacity = '1';
    }

    // Dynamic homework list generation
    const homeworkList = document.getElementById('homework-list');
    if (homeworkList) {
        const homeworkItems = [
            { title: 'Data Analysis Project', description: 'Comprehensive analysis of social media trends', date: 'Spring 2024' },
            { title: 'Programming Assignment', description: 'Machine learning algorithm implementation', date: 'Winter 2024' }
        ];

        homeworkItems.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('col-md-4');
            card.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${item.title}</h5>
                        <p class="card-text">${item.description}</p>
                        <p class="text-muted">${item.date}</p>
                    </div>
                </div>
            `;
            homeworkList.appendChild(card);
        });

        homeworkList.style.opacity = '1';
    }

    // Dynamic labs list generation
    const labsList = document.getElementById('labs-list');
    if (labsList) {
        const labItems = [
            { title: 'Machine Learning Lab', description: 'Exploring neural network architectures', date: 'Spring 2024' },
            { title: 'Data Visualization Lab', description: 'Creating interactive dashboards', date: 'Winter 2024' }
        ];

        labItems.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('col-md-4');
            card.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${item.title}</h5>
                        <p class="card-text">${item.description}</p>
                        <p class="text-muted">${item.date}</p>
                    </div>
                </div>
            `;
            labsList.appendChild(card);
        });

        labsList.style.opacity = '1';
    }
});