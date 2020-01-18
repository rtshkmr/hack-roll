
# Frame: 


Sat Jan 18 16:36:15 +08 2020

1. rails new hack_n_roll -d postgresql

2. rails db:create

3. models:

rails generate scaffold Module module_code:string;
rails generate scaffold Question question_body:text;
rails generate scaffold Answer answer_body:text;
rails generate scaffold Helper helper_score:integer;
rails generate scaffold Asker

4. rails db:migrate
 


5. gems to add to gemfile 

- responders gem to respond to json



6. Settle routes from routes.rb

7. 