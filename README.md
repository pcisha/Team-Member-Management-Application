# Team Member Management App

## Objective

1. The project is to implement a simple team-member management application that allows the user to view, edit, add, and
   delete team members.
2. The app consists of three pages for listing all the members, adding a new member and editing an exiting member. The
   functionality should also include deleting an existing member.
3. The three pages include: List page, Add page, Edit page
4. List page: This page shows a list of all team members. The subtitle should reflect the number of team
   members. If the team member is an admin, that is listed next to their name. Clicking a team member should show the
   Edit page. Clicking the plus button at the top should show the Add page.
5. Add page: The Add page appears when the user clicks the "+" on the List page. The user enters a team member's first &
   last name, their phone number, and email. Additionally, they can choose the team member's role (it defaults to '
   regular'). Hitting save adds the team member to the list and shows the List page.
6. Edit page: The Edit page appears when the user clicks a team member on the List page. This shows a form where the
   user can edit the details of the team member, including changing their role. Clicking save edits the team member
   information and shows the List page. Clicking Delete removes the team member and returns to the List page.
7. The web app should be implemented using Django. Consider using Django features such as model forms and generic
   class-based views to minimize the amount of code to write.
8. The front-end is ideally implemented as an SPA of your choice.

## Solution

#### Project Name: Team Member Management Application

#### Description:

1. This application creates a list of members. The application is an SPA (Single Page Application).
2. For each member, we require the first name, last name, email address, phone number and role.
3. There are two types of roles:`'Admin` and `Regular`. The role `Regular` is the default role assigned.
4. Functionality includes adding a new member, updating an existing member, deleting an exiting member and listing all
   members.
5. There are CRUD HTTP API endpoints to create, delete, edit member and view all members.
6. Error handling, logging (console and file), documentation, comments and test cases are included.
7. Also, for the frontend components, HTML pages (templates), CSS styling, and static images are included.

#### Approach

1. Created a new Django project `team_member_management` and a new app `members` within it.
2. There are CRUD HTTP API endpoints added in the views.py file for data manipulation. Note, the endpoints ar Http GET
   verb as the design of the app requires us to get the resources (member) first, and then modify it.
3. Created `TeamMember` class for managing first name, last name, email, phone, role and pk (id) of a member object, in
   the `models.py` file
4. Added HTML templates for the pages: listing members, add new member, delete a member, edit a member, in the `.html`
   files.
5. An additional HTML page is added for 404 Not Found Http Response handling when a member is not found for edition or
   deletion.
6. Created views for listing, adding, editing and deleting team members, in the `views.py`. These correspond to the URL
   endpoints of the app.
7. Error handling, logging, documentation are added to the views in the `views.py` file and also throughout the project
   for clarity and explanation.
8. URL endpoints and view endpoints are configured in the `urls.py` files respectively.
9. For static resources, `style.css` file is added for frontend design and image file `thumbnail.jpg` is added.
10. App configurations are done in the settings.py file and the `log.info` file contains some logs.
11. SQLite database contains the data. One migration of the database is done which contains the latest records in the
    db.sqlite3 file. Using the command `$python manage.py migrate`
12. `requirements-dev.txt` file is used for dependency management. Currently, Django version number is added as the only
    dependency.
13. Superuser `pcisha`'` without a password is created for the app.

#### URL Endpoints for CRUD Operations

1. All Members List: `GET http://127.0.0.1:8000/members/`
2. Add a new Team Member: `GET http://127.0.0.1:8000/members/add`
3. Edit an existing Team Member: `GET http://127.0.0.1:8000/members/{pk}/edit`
4. Delete an existing Team Member: `GET http://127.0.0.1:8000/members/{pk}/delete`
5. `GET http://127.0.0.1:8000/members/{pk}/edit/` returns 404 NOT FOUNd Http Response if a resource (member) does not
   exist.
6. `pk` is the unique identifier for each member object.

#### Tech Stack

1. Frontend: HTML 5, CSS 3, and JavaScript.
2. Backend: Python and Django.
3. Database: SQLite.
4. Deployment: Nginx.
5. Logging: Python's built-in logging library.
6. Testing and Debugging: Django Test Framework.
7. Version Control: Git, GitHub

#### Execution Commands

1. Create a `team_member_management` Django project with the app `members`.
2. Cd into the team_member_management folder.
3. Run Django environment: `$ python3 -m venv django-env`
4. Use this environment: `$ source django-env/bin/activate`
5. Install Django in this environment: `$ python -m pip install django`
6. Start the app: `$ python manage.py startapp members`
7. Install dependencies: `$ pip install -r requirements-dev.txt`
8. Apply database migration: `$ python manage.py migrate`
9. Create a superuser (optional): `$ python manage.py createsuperuser`
10. Run the development server locally: `$ python manage.py runserver`
11. To run tests cases: `$ python manage.py test`
12. `django-env/` folder is not included as it contains many files.

#### Frontend UI Experience

Attached as screenshots in the GitHub PR.

#### Time and Space Complexity

Models:

1. Time Complexity: O(1) for model operations.
2. Space Complexity: O(n) for storing 'n' team members in the database.

Views:

1. Time Complexity: O(n) for listing members, O(1) for CRUD operations.
2. Space Complexity: O(n) for storing members in memory during listing.

Rendering Pages: Space complexity for rendering pages is O(n), where 'n' is the number of team members being displayed
on a single page.

#### Consideration and Improvements

1. Overall, exception handling and error handling can be improved. Example: Database read-write operations, API endpoint
   HTTP statues (401, 503, 500, etc.). Custom error handling can be added. Form validation for data must be added.
2. Displaying errors to the Frontend User should be added.
3. Logs are currently written to console for debugging purposes. `settings.py file` can be modified to log to an
   info.log file.
4. CSRF tokens are added to the response. CSRF protection should be handled properly.
5. API endpoints can be updated to represent their true HTTP verbs of GET, PUT, POST, DELETE respectively.
6. API documentation can be added.
7. More happy path and unhappy path test cases can be added. More unit tests, database-level, API-level tests can be
   added.
8. Frontend UI experience can be added to leveraging JavaScript, HTML and CSS for a dynamic UI.
9. Delete confirmation page must be added.
10. Authentication and Authorization for the app permissions must be added.
11. Caching can be added for a members list.
12. At the production level, more security, monitoring, logging and alerting must be added. Some configuration in the
    current code reflects development environment.

## Summary:

This `README.md` file includes a clear description of the problem and the approach taken to solve,
time and space complexity analysis, and instructions on how to run the code.
This should provide a comprehensive overview for anyone reviewing the repository.

Author: Prachi Shah

Date: August 7, 2024.
