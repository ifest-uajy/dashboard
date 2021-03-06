# Dashboard Informatics Festival

Sistem berbasis web yang memungkinkan beberapa pengguna untuk melakukan aktifitas seperti mendaftar dalam perlombaan. Serta memiliki fungsi untuk mengumpulkan submisi tugas dari setiap perlombaan dan memverifikasi pembayaran.

## Tech Stack
1. Django
2. Django Rest Framwork
3. Vue
4. MySQL

## Features
1. Authentication
    - Registrasi
    - Login
    - Forgot password
    - Change password
    - Profile
2. Competitions
    - Create a team
    - Join a team
    - ~~Team profile~~
    - Team members
    - Payment (including in file upload)
    - File upload
3. ~~Talks (not implemented, coz using 3rd services)~~
    - ~~Join a seminar/workshop~~
    - ~~Payment~~
    - ~~Ticket/attendance confirmation~~
4. Staff Dashboard
    - Verify payment
    - Verify file upload (for those need verified files)
    - Download user uploaded files
    - ~~Download rekap data peserta~~
    - ~~Edit data~~
5. Mailing system
    - Welcome onboard
    - Forgot password
    - Team forming greetings
    - ~~Team forming invitations~~
    - Payment needed
    - Payment confirmed
    - Task rejected
    - ~~File upload needed~~
    - ~~Ticket/attendance confirmation issued~~

## Development

Development steps below using `pipenv` and `npm`. If you want to use others development environment please consider to do it yourself.

1. Using pipenv and npm `pipenv install` and `npm install`
2. Open shell `pipenv shell`
3. Migrate database `py manage.py makemigrations` and `py manage.py migrate`
4. Create superuser `py manage.py createsuperuser`
5. Collect statics for assets `py manage.py collectstatics`
6. Serve backend server `py manage.py runserver`
7. Serve frontend server `npm run serve`
8. Open `localhost:8080`

### Dev info
1. Frontend server: `localhost:8080`
2. Backend api server: `localhost:8000/api/`

## Build
1. Using development instruction
2. Make build bundle for frontend `npm run build`
3. Collect statics for assets `py manage.py collectstatics` again
4. Ships using proxy server like: Apache or nginx

## Copyright

This is a source code repository for a registration system that uses in a event. You could take a look to this work but cannot do anything with this code. This code was have no license, so you could read more in [here](https://choosealicense.com/no-permission/) what could you do and don't.

## Author
- Vriyas Hartama (liehart) - Full Stack Developer

## Notes
This web app is build to fullfill the need of event registration system of [Informatics Festival](https://ifest-uajy.com/) by [Himaforka UAJY](https://himaforka-uajy.org).
