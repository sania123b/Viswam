# 📊 Dreamer — Telugu Dream Journal

## 👁️ Vision
A lightweight web platform where Telugu-speaking users can write down, rewrite, tag, and share their dreams — styled like poetic stories or plain logs, inspired by the spirit of social platforms.

## 🔍 Problem Statement
Telugu speakers often journal dreams informally or not at all. There is no creative, open-source, regional-language space for dream exploration and storytelling.

## 🛠 Tech Stack
- **Backend**: Flask 3.0.0
- **Frontend**: TailwindCSS + Jinja2 templates
- **Database**: SQLite (lightweight, file-based)
- **Hosting Ready**: Gunicorn + Procfile (Heroku-compatible)

## ✨ Key Features
| Feature             | Description                                                |
|---------------------|------------------------------------------------------------|
| Write Dreams        | In native Telugu script                                     |
| Rewriting Styles    | Choose between plain, poetic, or story-style retellings    |
| Tag System          | Add tags for searching dreams (like hashtags)              |
| Public Feed         | View all public dreams in reverse chronological order      |
| Tag-Based Search    | Search dreams by any matching tag                          |

## 🚀 Deployment
- Uses `gunicorn` for WSGI support
- Includes `Procfile`, `runtime.txt`, and `requirements.txt`

## 🔐 Security Considerations
- SQLite parameterized queries used to avoid SQL injection
- Basic XSS protection via Jinja2 escaping
- No authentication yet (can be added)

## 🔄 Future Improvements
- Add user login (Google OAuth)
- Add AI-powered Telugu dream interpretation or better poetic generation
- API endpoints for mobile apps
- Export dream as PDF or image card

## 👨‍💻 Team
- **Lead Developer**: [Your Name]
- **Language Contributor**: [Add others here]

## 📜 License
MIT — Free to use, modify, and distribute
