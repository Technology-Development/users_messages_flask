# Users Messages: One-to-Many

### Part I - User

It's time to build a new application! This application should have full CRUD on the `users`. Each user should have a unique `id`, `first_name`, and `last_name`. The application will be horribly insecure: every will be able to edit or delete every other user. That's okay for now!

### Part II - Message

Now that you have one resource, it's time to add another! Each `user` should be able to write many `messages`. Each message should have a unique `id` and `content`.

Your application should have full CRUD on the users and messages. Remember that one user can send many messages.

### Bonuses

- Add styling to your application. Use Bootstrap or Bootswatch to help scaffold your design.
- Handle 404 errors elegantly.
- Add another column to users for an `image_url`. This way users can have their images show up in the application.
