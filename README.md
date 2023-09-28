# Personal Blog Project

A personal blogging platform built using Flask, allowing for user registration, posting, commenting, and profile management.

## Features

- **User Authentication**: Register, log in, and manage user sessions.
- **Blog Management**: Create, update, and delete blog posts.
- **Commenting System**: Users can comment on posts and manage their comments.
- **Profile Management**: Users can update their profile details, including a bio and profile picture.
- **Search Functionality**: Dynamic search feature to find relevant posts.
- **Styling**: Integrated with Bootstrap for a responsive design.

## Technologies Used

- **Flask**: Micro web framework written in Python.
- **Flask-Login**: For handling user sessions after they log in.
- **Flask-SQLAlchemy**: ORM for database operations.
- **Flask-WTF**: For form handling and validations.
- **Flask-Migrate**: Database migration management.
- **Flask-Bootstrap**: Integration of Bootstrap in Flask.
- **SQLite**: Lightweight disk-based database.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Z8phyR/Personal-Blog.git
   cd Personal-Blog
   ```

2. **Set up a Virtual Environment**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install the Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python run.py
   ```

## Lessons Learned

Throughout this project, I deepened my understanding of web development using Flask. I practiced:

- ORM principles with SQLAlchemy, enhancing my understanding of databases.
- Form creation and validation with Flask-WTF.
- User session management with Flask-Login.
- Styling principles using Bootstrap.
- Creating a flexible and extendable project structure.
- Writing tests to ensure code reliability.

## Future Enhancements

- Implement a richer text editor for blog creation.
- Integrate with a frontend framework like React or Vue for a SPA feel.
- Deploy the blog to platforms like Heroku or AWS.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
