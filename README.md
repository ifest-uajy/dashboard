# regsys-backend

Registration system for an annual-event.

## The Grand Plan

This will achieve a working state in production. A API to work with registration system of an event.

1. API to handle user registration
2. API to handle sending email to user
3. API to handle user team forming (we'll use token based issued special link to invitee more user to join one created team)
4. Api to handle talk registration

## Tech Stack Plan

1. Django
2. Django Rest Framework
3. React

## Have done

1. Authentication System
   Custom authenticationn system has done within registration function, login function, confirm email function, reset function. Need to work later, refresh JWT token function.

## Detailed Plan

### Authentication and Authorization

User will register through website and returned a JWT token to perform actions in the website.

### Mail Server

After finishing registration, user will recieve onboarding email in purpose to confirm their email. User then will get promotional email that contain what events or talks that open to join.

1. Onboarding email
2. Team forming confirmation
3. Payment reminder
4. Payment success recipt
5. Cancellation email
6. Ticket email
7. Finalist email

### Payment

There will be other dashboard like website to perform update the value of payment confirmation. This action could be done online with staff permission.

## Copyright

This is a source code repository for a registration system that uses in a event. You could take a look to this work but cannot do anything with this code. This code was have no license, so you could read more in [here](https://choosealicense.com/no-permission/) what could you do and don't.
