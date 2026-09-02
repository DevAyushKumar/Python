Python FastAPI Tutorial (Part 1) - Getting Started: Web App + REST API
================================================================================
1. OVERVIEW & PROJECT ROADMAP
================================================================================
- Goal: Build a full-featured, production-ready web application and REST API from scratch using FastAPI.
- Key Technologies Covered in Series:
  * Backend API: FastAPI (modern, fast, built-in async support, automatic documentation).
  * Data Validation: Pydantic models.
  * Database: SQLite (development) transitioning to PostgreSQL via SQLAlchemy ORM.
  * Authentication: Password hashing with bcrypt, JWT (JSON Web Tokens).
  * Architecture: Clean router organization (`APIRouter`), CRUD operations, background tasks (email sending), file uploads.
  * Frontend: Dual-delivery architecture serving both JSON API endpoints and Jinja2 HTML templates.

================================================================================
2. ENVIRONMENT SETUP & INSTALLATION
================================================================================
FastAPI recommends installing with the standard extras, which bundles:
  * `fastapi`: The core web framework.
  * `uvicorn`: High-performance ASGI web server.
  * `fastapi-cli`: Command-line tool for running and debugging FastAPI apps.

--- Project Initialization ---

# Option A: Using UV (Fast modern Python package manager)
uv init fastapi_blog
cd fastapi_blog
uv add "fastapi[standard]"

# Option B: Using standard pip
mkdir fastapi_blog
cd fastapi_blog
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install "fastapi[standard]"

================================================================================
3. RUNNING THE APPLICATION
================================================================================
Run the development server with live auto-reload enabled:

# Using the FastAPI CLI:
fastapi dev main.py

# Using Uvicorn directly:
uvicorn main:app --reload

- Default Server Port: http://127.0.0.1:8000
- Built-in Interactive API Documentation:
  * Swagger UI: http://127.0.0.1:8000/docs
  * ReDoc UI:   http://127.0.0.1:8000/redoc

================================================================================
4. COMPLETE SOURCE CODE (main.py)
================================================================================

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Dummy in-memory dataset
posts = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI Tutorial",
        "content": "Getting started with FastAPI and building REST APIs.",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python Async Programming",
        "content": "Understanding ASGI and async/await in modern Python.",
        "date_posted": "April 21, 2026",
    },
]

# ------------------------------------------------------------------------------
# 1. JSON REST API ENDPOINTS
# ------------------------------------------------------------------------------
# Automatically documented in /docs and /redoc

@app.get("/api/posts")
def get_posts():
    """Returns list of posts as pure JSON"""
    return posts


# ------------------------------------------------------------------------------
# 2. FRONTEND HTML ROUTES (WITH MULTI-URL STACKING & SCHEMA FILTERING)
# ------------------------------------------------------------------------------
# Multiple routes mapped to a single view function by stacking decorators.
# 'include_in_schema=False' hides web browser HTML routes from the OpenAPI/Swagger docs.

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def render_posts_html():
    """Renders basic HTML for web browser consumption"""
    html_content = "<h1>Blog Posts</h1>"
    for post in posts:
        html_content += f"""
        <div>
            <h2>{post['title']}</h2>
            <p>By {post['author']} on {post['date_posted']}</p>
            <p>{post['content']}</p>
        </div>
        <hr>
        """
    return html_content

================================================================================
5. CORE TAKEAWAYS & BEST PRACTICES
================================================================================
1. Automatic JSON Serialization:
   - Python dictionaries and lists returned from route functions are automatically serialized into valid JSON with `application/json` Content-Type headers.

2. Response Class Customization:
   - Use `response_class=HTMLResponse` to return raw HTML or template responses with `text/html; charset=utf-8`.

3. Decorator Stacking for Route Aliasing:
   - Stack multiple `@app.get()` decorators on top of the same view function to serve identical content across different URLs (e.g., `/` and `/posts`).

4. Separation of Web UI vs. API Documentation (`include_in_schema=False`):
   - Interactive docs (`/docs`) are intended for programmatic API consumers.
   - Setting `include_in_schema=False` keeps user-facing HTML pages out of OpenAPI documentation to keep the API schema clean.