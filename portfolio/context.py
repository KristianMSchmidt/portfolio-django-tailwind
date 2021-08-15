context = {
    "skills": {
        "python": {
            "title": "Python development",
            "description": (
                "I've built countless projects in Python, spanning from AI game agents "
                "to neural networks and backend development. You'll see examples of my work in Python "
                "in the projects section and on my github profile."
            ),
            "img": {
                "width": "120",
                "height": "120",
                "url": "img/120px-Python-logo-notext.png",
            },
        },
        "django": {
            "title": "Full stack web development",
            "description": (
                "I use web frameworks such as Django and Flask to build web projects with Python "
                "backends. Using these frameworks makes it easy to follow proven design patterns such as MVC. "
                "See exampes in the projects section."
            ),
            "img": {"width": "230", "url": "img/django-logo.png"},
        },
        "php": {
            "title": "PHP development",
            "description": (
                "Before learning Django, I made full-stack web applications in the LAMP stack (Linux, Apache, MySql and PHP). "
                "For an example, see my Bugtracker project below"
            ),
            "img": {"width": "200", "url": "img/php-logo-vector.svg"},
        },
        "frontend": {
            "title": "Front end development",
            "description": (
                "I use HTML, CSS, Javascript and Bootstrap to build responsive websites. I also use CSS prepocessors such as Sass. "
                "You'll see examples of my front end skills in all my projects in the projects section."
            ),
            "img": {"width": "120", "url": "img/csshtmljs.jpeg"},
        },
        "database": {
            "title": "Data base development",
            "description": (
                "I have experience designing and queriyng relational databases using both raw SQL "
                "and object relational mappers. See examples of both in the projects section."
            ),
            "img": {"width": "120", "url": "img/sql.png"},
        },
        "tailwind": {
            "title": "Tailwind CSS development",
            "description": (
                "In some of my later projects, including this portfolio, I've used the nice CSS framework Tailwind CSS. "
                "Tailwind CSS makes development faster and gives nice aesthetic results."
            ),
            "img": {"width": "160", "url": "img/tailwind-css-logo.svg"},
        },
        "numpy": {
            "title": "Scientific computing",
            "description": (
                "I have written thousands of lines of code in scientific Python libraries such as Numpy, "
                "Matplotlib, Pandas, Tensorplow and Pytorch. These projects are from before I started "
                "doing web development, so you won't find live applications here. But the code is available on GitHub."
            ),
            "img": {"width": "200", "url": "img/numpy.png"},
        },
    },
    "projects": {
        "bugtracker_php": {
            "title": "Bug Tracker - PHP",
            "subtitle": "A ticket tracking system",
            "bg_color": "bg-red-200",
            "category": "Web Application",
            "project_id": "bugtracker_php",
            "github_url": "https://github.com/KristianMSchmidt/bug_tracker",
            "external_url": "https://www.kristianmschmidt.com/bugtracker/view/pages/demo_login.php",
            "stack": "PHP, SQL, JavaScript, CSS, Sass, HTML",
            "deployment": "Hostinger",
            "description": (
                "This is a ticket tracking system that could be used by e.g. a sofware company to "
                "keep track of reported bugs and issues related to their software. The program features "
                "authorization and authentication, multi-role demo-login and an automated notification system. "
                "I've built this project from scratch, including relational database design and a responsive "
                "front end. The back end is built with (object-oriented) PHP, raw SQL and a MySql-database. "
                "The front end is built with vanilla HTML, CSS, Sass and JavaScript. "
                "If you only visit once, I recommend that you log in as 'Demo Admin'."

            ),
        },
        "portfolio": {
            "title": "This Portfolio",
            "subtitle": "What you see right now",
            "bg_color": "bg-blue-100",
            "category": "Web Application (Single-page)",
            "project_id": "portfolio",
            "github_url": "https://github.com/KristianMSchmidt/portfolio-django-tailwind-heroku",
            "external_url": "/",
            "stack": "Django, Python, JavaScript, Tailwind CSS, HTML",
            "deployment": "Heroku",
            "description": (
                "Though this website is mostly static, I've used Django on the backend to include re-usable "
                "components and to set up the email backend. "
                "The portfolio is built as a single-page application using Javascript. "
                "I've made the styling and responsive layout using Tailwind CSS. "
            ),
        },
        "bugtracker_django": {
            "title": "Bug Tracker - Django",
            "subtitle": "A ticket tracking system",
            "bg_color": "bg-pink-100",
            "category": "Web Application",
            "project_id": "bugtracker_django",
            "github_url": "https://github.com/KristianMSchmidt/django-bugtracker",
            "external_url": "https://django-bugtracker.herokuapp.com/",
            "stack": "Django, Python, JavaScript, HTML, Bootstrap, htmx, Docker, FactoryBoy",
            "deployment": "Heroku (Docker)",
            "description": (
                "This is a ticket tracking system that could be used by e.g. a sofware company to keep track of "
                "reported bugs and issues related to their software. The program features authorization and authentication, "
                "multi-role demo-login and an automated notification system. I am building this project from scratch, "
                "including relational database design and a responsive front end. "
                "The back end is built with Django and Python. The front end is built with "
                "vanilla HTML, htmx, CSS, Bootstrap and JavaScript. When the implementation is done, it will feature throughout unit testing, pagination, CRUD-operations, a postgresql database with "
                "One-To-Many and Many-To-Many relations, password reset via email, search functionality and much more. "
                "If you only visit once, I recommend that you log in as 'Demo Admin'."
            ),
        },
        "twentyfortyeight": {
            "title": "2048 Game",
            "subtitle": "Strong AI player",
            "bg_color": "bg-yellow-100",
            "category": "Web Application",
            "project_id": "twentyfortyeight",
            "github_url": "https://github.com/KristianMSchmidt/2048-game-",
            "external_url": "https://kristianmschmidt.pythonanywhere.com/twentyfortyeight",
            "stack": "Python, Flask, Html, JavaScript, CSS, SCSS",
            "deployment": "PythonAnywhere (PaaS)",
            "description": (
                "Web app with an AI-player for the 2048-game. "
                "The AI-player uses minimax-search with pruning. "
                "The search is guided by a heuristics function that to each board position assigns a score reflecting the quality of the position. "
                "The game is indeterministic by nature: After each move by the player, the computer randomly selects a free position to place "
                "a new tile: 90% of these new tiles will have value 2, while 10% will have value 4. "
                "During the mini-max search, the minimizing and maximazing agents are choosing their moves based on expected values given the known distribution of 2-tiles and 4-tiles. "
                "I originally made a Python backend to this project as an assignment to the online 'micro-master in Artificial intelligence' at Columbia University. "
                "Since then I've fine-tuned the algorithms, added the expected-value considerations, designed a responsive front-end and put it all together using Flask."
            ),
        },
        "eightpuzzle": {
            "title": "8-puzzle solver",
            "subtitle": "Compare solution algorithms",
            "bg_color": "bg-green-100",
            "category": "Web Application",
            "project_id": "eightpuzzle",
            "github_url": "https://github.com/KristianMSchmidt/flask-8-puzzle",
            "external_url": "https://kristianmschmidt.pythonanywhere.com/puzzle",
            "stack": "Python, Flask, Html, Javascript, CSS, SCSS",
            "deployment": "PythonAnywhere (PaaS)",
            "description": (
                "On this web app, you can construct and play with classic 8-puzzles (and more complicated 15-puzzles). "
                "You can either try to solve the puzzles yourself or let an AI agent do the hard work. "
                "You can choose between 4 different solution algorithms (A*-search, Greedy Best-First Search, Depth-First Search and Breadth-First Search) and "
                "compare their performance: Info from the real-time solution process on the server, such as running time and the number of moves in the found "
                "solution, is rendered to the user, making the app a nice demonstration of the strengths and weaknesses of the different search algorithms. "
                "I originally made the python backend of this project as an assignment for Columbia University's "
                "Artificial Intelligence MicroMasters Program. "
                "More recently, I've designed a reponsive front-end with vanilla technologies and put it all together using the Flask web framework."
            ),
        },
        "sudoku": {
            "title": "Sudoku Solver",
            "subtitle": "Blazingly fast",
            "bg_color": "bg-purple-100",
            "category": "Web Application",
            "project_id": "sudoku",
            "github_url": "https://github.com/KristianMSchmidt/Sudoku-solver-Flask-web-app-",
            "external_url": "https://kristianmschmidt.pythonanywhere.com/sudoku",
            "stack": "Python, Flask, HTML, JavaScript, CSS, SCSS",
            "deployment": "PythonAnywhere (PaaS)",
            "description": (
                "This is a speed optimized automatic sudoku solver using Back Tracking Search (BTS) and an Arc Consistency Algorithm (AC-3). "
                "I originally made the python backend of this project as an assignment for Columbia University's "
                "Artificial Intelligence MicroMasters Program. "
                "More recently, I've designed a simply front-end with vanilla technologies and put it all together using the Flask web framework."
            ),
        },
    },
}
