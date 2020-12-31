# Graphically Graphic

Graphically graphic is a hub for all the nedds of a graphic designer looking to acquire freelance work and house all requests from clients. The site groups together the needs to communicate with customers looking for work to be completed with the needs to showcase impressive previous works in order to let viewers know they are in the right place. Equally as a user looking to get work done, the ssite allows you to see feedback on previous jobs completed, get a quote for the work you're requesting and sign in to see your requests active whilst monitoring their proggress as updated by the admin. 

 
## UX

The website is built as a platform for people to request graphic design work from an expert, by specifying their requirements, their preference of print medium, and output format. It is straight forward for users to request their preferences and also to discuss the options with the creator to get what they need out of a request.

    * As a potential client, I want to be able to log in so that my interactions with the site can be saved for future reference

    * As a potential client, I want to be able to make a request to the designer to complete work for me

    * As a potential client, I want to be able to know how much a job will cost so that I can judge if I am willing to pay

    * As a potential client, I want to be able to see the progress made on my requests so that I can be reassured of it's completion

    * As an admin, I want to be the only one able to see requests made to me by potential clients so that I may accept or decline them.

    * As an admin, I want to be able to easily contact potential clients so that I may discuss their requests with them.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

- Login system, is a function of logging into a session as a user or as an admin with different site 

- Payment system - allows users to put down a deposit for the work they would like to be completed, once a fee has been agreed and allows users to pay for completed work.

- Form to submit requests, with calculated quote and time frame 

- As Admin, view current requests in priority order (With status = Accepted, Declined, awaiting deposit, deposit recieved, in progress, completed, awaiting payment, paid)

- Chat with client concerning work requested - linked to work request

- As client - see requests past, current.
 
### Existing Features

- Login system, as admin or as user - allows both users and admins to log in to the site and see requests you've created and your quote and as admin allows you to see all requests made to you and update their progress

- Payment system - allows users to put down a deposit for the work they would like to be completed, once a fee has been agreed and allows users to pay for completed work.

- Request views allow both users and admins to view request they've made or received and communicate and update statuses as they progress


### Features Left to Implement

- Gallery to hold all existing and future work created by the graphic designer

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Materialize Framework](https://materializecss.com/)
    - I used **Materialize** to provide responsiveness and structure to my website.

- [Heroku](https://www.heroku.com/)
	- I used Heroku to deploy and host my live-site

- [Django](https://django.com/)
    - I used **Django** to serve as the main framework for my website.

- [MySql](https://dev.mysql.com/)
    - I used **MySQL** to store data relating to my site my website.


## Testing


    * As a potential client, I want to be able to log in so that my interactions with the site can be saved for future reference
        Open website, reach login page.
        click navbar dropdown and select sign up
        created new user filling in sign up form
        returned to log in page via navbar
        filled in details
        confirmed username was in navbar showing as logged in with new dropdown options

    * As a potential client, I want to be able to make a request to the designer to complete work for me
        Open website, reach login page.
        Once logging in, see "submit request" option in navigation dropdown
        Filled in form
        Got redirected to request view

    * As a potential client, I want to be able to know how much a job will cost so that I can judge if I am willing to pay
        Open website, reach login page.
        Once logging in, see "submit request" option in navigation dropdown
        Filled in form
        Basket on right hand side shows me the price before submitting

    * As a potential client, I want to be able to see the progress made on my requests so that I can be reassured of it's completion
        Logging into the site and navigating to "My Requests" from navigation dropdown as a non superuser,
        I am able to see all of my requests, and if they have changed status, the status will show on the requests/mine page.

    * As an admin, I want to be the only one able to see requests made to me by potential clients so that I may accept or decline them.
        Login as an admin and navigate to the requests/all page. I should be able to see requests from all users/
        Login as a non admin, and navigate to the requests/all page/ I should be redirected away from the requests/all page, since I am not allowed to see them.

    * As an admin, I want to be able to easily contact potential clients so that I may discuss their requests with them.
        Once logged in as an admin or a normal user, I can navigate to a request and add comments for the other party to see. There is a comment form,
        which once submitted will show the most recent comments at the top

## Deployment

I had to follow details in https://devcenter.heroku.com/articles/django-app-configuration, to ensure that the migrations and database details were set up correctly.

Once the database details were coorrectly configured, I was able to access my site at https://louis-ms4.herokuapp.com/
