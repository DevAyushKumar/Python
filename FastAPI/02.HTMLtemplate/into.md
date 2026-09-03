# HTML Frontend for Your API: Jinja2 Templates
================================================================================
1. OVERVIEW & MOTIVATION
================================================================================
- Why Jinja2 Templates?
  * Returning raw HTML strings in Python code is unmaintainable for real applications with headers, footers, navbars, and layouts.
  * Templates decouple the HTML presentation layer from backend business logic while allowing dynamic data injection.
  * Dual-Delivery Pattern: Maintains JSON endpoints (/api/posts) for programmatic consumers while rendering styled HTML pages (/) for human browser navigation using the exact same data source.
- Dependencies:
  * Jinja2 is pre-bundled when installing `fastapi[standard]`.
  * Manual installation (if minimal install was used): `pip install jinja2` or `uv add jinja2`.

================================================================================
2. DIRECTORY STRUCTURE CONVENTIONS
================================================================================
FastAPI follows standard web conventions for template and asset management:

fastapi_blog/
├── main.py
├── static/
│   ├── css/
│   │   └── main.css
│   ├── images/
│   └── js/
└── templates/
    ├── layout.html
    └── home.html

================================================================================
3. CORE JINJA2 SYNTAX PATTERNS
================================================================================
- Variable Interpolation:
  {{ variable_name }} or {{ post.title }}
- Loops & Control Structures:
  {% for post in posts %}
      ...
  {% endfor %}
- Conditionals:
  {% if title %}
      <title>{{ title }} - Blog</title>
  {% else %}
      <title>Default Blog Title</title>
  {% endif %}
- Template Inheritance (Blocks):
  Parent: {% block content %}{% endblock content %}
  Child:  {% extends "layout.html" %}
          {% block content %} ... {% endblock content %}
- Dynamic URL Resolution:
  * For Static Assets: {{ url_for('static', path='css/main.css') }}
  * For Named Routes:   {{ url_for('home') }} or {{ url_for('post') }}

================================================================================
4. TEMPLATE IMPLEMENTATIONS
================================================================================

--- templates/layout.html (Base Parent Template with Bootstrap 5) ---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if title %}
        <title>{{ title }} - FastAPI Blog</title>
    {% else %}
        <title>FastAPI Blog</title>
    {% endif %}
    <!-- Bootstrap CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS via static mount -->
    <link rel="stylesheet" href="{{ url_for('static', path='css/main.css') }}">
</head>
<body>
    <header class="p-3 bg-dark text-white mb-4">
        <div class="container">
            <div class="d-flex flex-wrap align-items-center justify-content-between">
                <a href="{{ url_for('home') }}" class="text-white text-decoration-none h4 mb-0">FastAPI Blog</a>
                <ul class="nav">
                    <li><a href="{{ url_for('home') }}" class="nav-link px-2 text-white">Home</a></li>
                    <li><a href="{{ url_for('get_posts') }}" class="nav-link px-2 text-white">API Posts</a></li>
                </ul>
            </div>
        </div>
    </header>

    <main class="container">
        {% block content %}{% endblock content %}
    </main>

    <!-- Bootstrap JS Bundle CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>


--- templates/home.html (Child Template Extending Base Layout) ---

{% extends "layout.html" %}

{% block content %}
    <h1 class="mb-4">Recent Posts</h1>
    {% for post in posts %}
        <article class="card mb-3 shadow-sm">
            <div class="card-body">
                <h2 class="card-title h4">{{ post.title }}</h2>
                <h6 class="card-subtitle mb-2 text-muted">By {{ post.author }} on {{ post.date_posted }}</h6>
                <p class="card-text">{{ post.content }}</p>
            </div>
        </article>
    {% endfor %}
{% endblock content %}

================================================================================
5. BACKEND CODE IMPLEMENTATION (main.py)
================================================================================

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static directory to serve CSS, JS, and image assets
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# In-memory dummy dataset
posts = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI Tutorial (Part 1)",
        "content": "Getting started with FastAPI and building REST APIs.",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Jinja2 Template Integration",
        "content": "Serving HTML templates with template inheritance in FastAPI.",
        "date_posted": "April 21, 2026",
    },
]

# ------------------------------------------------------------------------------
# JSON REST API ROUTE
# ------------------------------------------------------------------------------
@app.get("/api/posts")
def get_posts():
    """Returns raw JSON posts for API consumers"""
    return posts


# ------------------------------------------------------------------------------
# HTML FRONTEND ROUTES
# ------------------------------------------------------------------------------
# Notice: Explicit 'name' parameters prevent URL collision when stacking decorators
# on the same view function when resolving routes with url_for().

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="post")
def render_home_page(request: Request):
    """Renders the HTML home page with dynamic post context"""
    context = {
        "request": request,       # Mandatory for Jinja2 in FastAPI
        "posts": posts,
        "title": "Home"
    }
    return templates.TemplateResponse("home.html", context)

================================================================================
6. KEY TECHNICAL NUANCES & BEST PRACTICES
================================================================================
1. The Mandatory `request: Request` Parameter:
   - Jinja2Templates in FastAPI requires the active `Request` instance inside the template context to properly generate absolute/relative URLs using `url_for()`.

2. Static Files Mounting:
   - `app.mount("/static", StaticFiles(directory="static"), name="static")` exposes filesystem files located in `/static` to the URL route prefix `/static/`.

3. Explicit Route Naming (`name="home"`):
   - When stacking decorators on a single view function (e.g., `/` and `/posts`), FastAPI defaults to using the function name (`render_home_page`) as the route identity.
   - Setting explicit `name="home"` and `name="post"` ensures `url_for('home')` generates `/` rather than defaulting to the last stacked decorator route.

4. OpenAPI Cleanliness (`include_in_schema=False`):
   - Always apply `include_in_schema=False` to template-rendering web page endpoints so that Swagger UI (`/docs`) and ReDoc (`/redoc`) remain dedicated solely to the machine-readable REST API endpoints.