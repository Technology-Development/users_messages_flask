# Users Messages: Many-to-Many

### Adding Tags!

Add another resource to your users and messages application! Create a resource for tags which has a many to many relationship with messages. Tags should be used to categorize the content of the message (e.g. "happy", "sports", "coding", etc).

1.  You should be able to create full CRUD on tags.
2.  When you create a message, you should be able to add existing tags to it.
3.  When you edit a message, you should be able to modify the tags associated to it.
4.  When you create a tag, you should be able to add existing messages to it.
5.  When you edit a tag, you should be able to modify the messages associated to it.

### Bonus: Database performance

If you add a bunch of data to the model solution, you should see that some pages require a lot of database querying in order to render. This means that the app probably won't scale very well as the database grows.

The underlying issue here is related to a family of problems known as _N + 1 query problems_. You can read a bit about these issues [here](https://www.rithmschool.com/courses/flask-fundamentals/database-performance). As a bonus, can you think of a way to improve the performance of the app by reducing the number of database queries required?

### Bonus: MOAR CRUD APPZ

If you finish your users / messages / tags app and want to build something else, try to create an app that allows you to perform CRUD on employees and departments for a company. A department can have many employees, and an employee can belong to many departments.

Your app should have the following features:

- Full CRUD on employees.
- Full CRUD on departments.
- The index or show page for employees should show the department name for each employee.
- The index or show page for departments should show all employees in the department.

Have fun!
