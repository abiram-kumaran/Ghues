# Ghues - Flask Blog Application

A modern, feature-rich blogging platform built with Flask and SQLAlchemy. Create posts, comment on others' posts, and engage with the community.

## Features

✨ **Core Features:**
- User authentication (register/login/logout)
- Create, read, and delete posts
- Comment on posts
- Like/unlike posts in real-time
- User-specific post viewing
- Secure password hashing with bcrypt
- Session management with Flask-Login

🎨 **UI/UX:**
- Responsive Bootstrap design
- Clean, intuitive interface
- Real-time feedback with flash messages
- Hover effects and smooth animations

## Technology Stack

- **Backend:** Flask 3.0.3
- **Database:** SQLite with SQLAlchemy ORM
- **Authentication:** Flask-Login & bcrypt
- **Frontend:** Bootstrap 5, Jinja2 templates
- **Forms:** Flask-WTF with WTForms validation

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/abiram-kumaran/Ghues.git
   cd Ghues
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python3 app.py
   ```

5. **Access the app**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## Default Test Credentials

**Authorized GA Numbers & Emails** (for registration):

| GA Number | Email |
|-----------|-------|
| 18GA112 | flamesraft@gmail.com |
| 21GA106 | abhidhyasri5@gmail.com |
| 23GA129 | abiram.kumaran@gmail.com |
| 20GA106 | amareshgamer2203@gmail.com |
| 11GA118 | chaarya.rangasamy@gmail.com |

(Full list available in `website/auth.py`)

**To Test:**
1. Go to `/register`
2. Enter an authorized GA number and corresponding email
3. Set a password (minimum 6 characters)
4. Create an account and login

## Project Structure

```
Ghues/
├── app.py                    # Main Flask application entry point
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── .gitignore              # Git ignore rules
└── website/
    ├── __init__.py         # Flask app factory & database setup
    ├── models.py           # SQLAlchemy database models
    ├── auth.py             # Authentication routes (login/register/logout)
    ├── views.py            # Main application routes (posts, comments, likes)
    ├── database.db         # SQLite database (auto-created)
    ├── static/
    │   └── index.js        # Frontend JavaScript for like functionality
    └── templates/
        ├── base.html       # Base template with navigation
        ├── login.html      # Login page
        ├── signup.html     # Registration page
        ├── home.html       # Home feed
        ├── create_post.html# Create new post page
        ├── posts.html      # User's posts view
        └── posts_div.html  # Post cards component
```

## Database Models

### User
- `id` - Primary key
- `email` - Unique email address
- `username` - Unique username
- `GA` - Unique GA number
- `password` - Hashed password
- `date_created` - Account creation timestamp
- Relations: Posts, Comments, Likes

### Post
- `id` - Primary key
- `text` - Post content
- `author` - Foreign key to User
- `date_created` - Post creation timestamp
- Relations: Comments, Likes

### Comment
- `id` - Primary key
- `text` - Comment content (max 200 chars)
- `author` - Foreign key to User
- `post_id` - Foreign key to Post
- `date_created` - Comment creation timestamp

### Like
- `id` - Primary key
- `author` - Foreign key to User
- `post_id` - Foreign key to Post
- `date_created` - Like timestamp

## API Endpoints

### Authentication
- `GET/POST /login` - User login page and logic
- `GET/POST /register` - User registration page and logic
- `GET /logout` - User logout (requires authentication)

### Posts
- `GET /` or `/home` - View all posts (requires authentication)
- `GET/POST /create-post` - Create new post (requires authentication)
- `GET /delete-post/<id>` - Delete a post (requires authentication)
- `GET /posts/<username>` - View posts by specific user (requires authentication)

### Comments
- `POST /create-comment/<post_id>` - Add comment to post (requires authentication)
- `GET /delete-comment/<comment_id>` - Delete a comment (requires authentication)

### Likes
- `POST /like-post/<post_id>` - Like/unlike a post (requires authentication)

## Bug Fixes Applied

This version includes fixes for the following issues:

1. **Fixed delete_post logic** - Corrected permission check to compare `current_user.id` with `post.author` instead of `post.id`
2. **Fixed create_comment query** - Added `.first()` to properly retrieve post object from database
3. **Fixed database configuration** - Updated SQLite path handling with proper Flask instance folder management
4. **Fixed permission checks** - Corrected username comparisons and access control logic

## Security Features

- Passwords hashed using bcrypt (pbkdf2:sha256)
- CSRF protection on all forms with Flask-WTF
- Session management with secure cookies
- SQL injection prevention with SQLAlchemy ORM
- Login required decorators on protected routes

## Known Limitations

- GA number and email validation is hardcoded (list in auth.py)
- No email verification
- Single-page post creation (no drafts)
- No post editing functionality
- No notifications system

## Future Enhancements

- [ ] Post editing functionality
- [ ] User profiles with bio
- [ ] Email verification
- [ ] Direct messaging
- [ ] Post categories/tags
- [ ] Search functionality
- [ ] Admin dashboard
- [ ] Deployment to production server

## Development Notes

- Debug mode is enabled by default in `app.py`
- For production, use a proper WSGI server (Gunicorn, uWSGI)
- Database is SQLite by default for simplicity
- For production, consider PostgreSQL or MySQL

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please create an issue on the GitHub repository.

---

**Created by:** Abiram Kumaran  
**Last Updated:** November 2026
