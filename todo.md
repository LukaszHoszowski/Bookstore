# Signup

1. Model - User
2. Forms - CustomUserCreationForm
3. View:
   1. Create file at "accounts" views.py
   2. Class "CreatView"
4. Templates:
   1. Create signup.html -> templates/registration
5. Create urls at accounts app
   1. endpoint signup/, name="signup"
6. Connect account at main url's
7. settings - installed apps
8. base -> add sign up

# Crispy-forms

1. download bootstrap
2. pipenv install django-crispy-forms=="1.13.0"
3. settings -> Installed apps -> 3rd party
4. settings -> CRISPY_TEMPLATE_PACK = 'bootstrap4'
5. templates -> {% load crispy_forms_tags %}
6. {{ form.as_p }} replace with {{ form | crispy }}
7. pipenv install crispy-bootstrap5
8. settings -> CRISPY_TEMPLATE_PACK = 'bootstrap5'
9. CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"