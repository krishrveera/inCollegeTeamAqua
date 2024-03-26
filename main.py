from flask import Flask, render_template, request, redirect, url_for, session

app = Flask('app')
app.secret_key = 'secretKey'


# Main menu
def main():
  while True:
    print("Welcome to inCollege")
    print("Please select an option from the menu below")
    print("1. Login")
    print("2. Sign up")
    print("3. Connect with your friends")
    print("4. College Student Success Story")
    print("5. Exit")
    userChoice = input("Enter your choice: ")
    if userChoice == "1":
      return redirect(url_for('login'))
    elif userChoice == "2":
      return redirect(url_for('general->SignUp->login'))
    elif userChoice == "3":
      return redirect(url_for('connect'))
    elif userChoice == "4":
      return "Thank you for using inCollege. Goodbye"
    else:
      print("Invalid input, please try again")


# Global dictionary to hold username, passwords, first name, and last name
accounts = {}

# Global dictionary to hold job postings
job_postings = {}

# Global dictionary to hold profile info
profiles = {}

# functions for the homePage
friend_requests = {}
friends = {}
MAX_ACCOUNTS = 10


# Useful Links
@app.route('/')
def index():
  story = "College Student Success Story: Stacy, a recent college graduate, used InCollege to network with professionals in her field. She utilized the platform's job search feature and found a position at a company. Now, she's thriving in her career thanks to the connections she made on InCollege."
  return render_template('homePage.html', success_story=story)


@app.route('/general')  # the name of the page in the url
def general():  # name of the redirection that you are using in the html page
  return render_template('homePage->general.html')  # address of the html page


@app.route('/browseInCollege')
def browse():
  return "Under Construction"


@app.route('/businessSolutions')
def businessSolutions():
  return "Under Construction"


@app.route('/directories')
def directories():
  return "Under Construction"


#Incollege Important Links


@app.route('/copyrightNotice')
def copyrightNotice():
  return "Your personal information is protected and will never be shared with third parties without your consent. We employ industry-standard security measures to safeguard your data. Feel free to reach out to us if you have any concerns about your privacy or data usage at incollegesupport@gmail.com."


@app.route('/about2')
def about2():
  return "Under Construction"


@app.route('/accessibility')
def accessibility():
  return "Under Construction"


@app.route('/agreement')
def agreement():
  return "Under Construction"


@app.route('/important->privacyPolicy->guestControls', methods=['GET', 'POST'])
def privacyPolicy():
  preferences = {
      'Email': True,
      'SMS': True,
      'Advertising': True,
      'Language': 'English'
  }
  if request.method == 'POST':
    # Update preferences based on user input
    if 'email' in request.form:
      preferences['Email'] = False
    if 'sms' in request.form:
      preferences['SMS'] = False
    if 'advertising' in request.form:
      preferences['Advertising'] = False
    if 'language' in request.form:
      preferences['Language'] = request.form['language']

  return render_template('privacyPolicyNewAttempt.html',
                         preferences=preferences)


@app.route('/cookies')
def cookies():
  return "Under Construction"


@app.route('/copyrightPolicy')
def copyrightPolicy():
  return "Under Construction"


@app.route('/brand')
def brand():
  return "Under Construction"


# functions for the homePage->general page


@app.route('/sign_in_processing')
def sign_in_processing():
  return render_template('general->SignUp.html')


@app.route('/help_center')
def help():
  return "We’re here to help"


@app.route('/about')
def about():
  return "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"


@app.route('/press')
def press():
  return "In College Pressroom: Stay on top of the latest news, updates, and reports"


@app.route('/blog')
def blog():
  return "Under Construction"


@app.route('/careers')
def careers():
  return "Under Construction"


@app.route('/developers')
def developers():
  return "Under Construction"


@app.route('/general->SignUp->login', methods=['GET', 'POST'])
def login():
  error_message = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username in accounts and accounts[username]['password'] == password:
      session['username'] = username
      return redirect(url_for('post_menu', username=username))
    else:
      error_message = "Invalid username or password. Please try again."
  return render_template('general->SignUp->login.html',
                         error_message=error_message)


@app.route('/general->SignUp->login->post_menu/<username>',
           methods=['GET', 'POST'])


def post_menu(username):
  return render_template('general->SignUp->login->post_menu.html',
                         username=username)


@app.route('/job_search', methods=['GET', 'POST'])


def job_search():
  if request.method == 'POST':
    username = request.form.get('username')
    if username in accounts:
      if len(job_postings.get(username, [])) >= 10:
        return "You have reached the maximum number of job postings (10)."
      title = request.form['title']
      description = request.form['description']
      employer = request.form['employer']
      location = request.form['location']
      salary = request.form['salary']
      job_postings.setdefault(username, []).append({
          'title':
          title,
          'description':
          description,
          'employer':
          employer,
          'location':
          location,
          'salary':
          salary,
          'posted_by':
          accounts[username]['first_name'] + ' ' +
          accounts[username]['last_name']
      })
    return redirect(url_for('job_search'))

  else:
    return render_template('jobSearch.html', job_postings=job_postings)

@app.route('/delete_job', methods=['GET', 'POST'])
def delete_job():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        job_title = request.form.get('job_title')

        # remove job from job_postings
        if job_title and username in job_postings:
            job_postings[username] = [job for job in job_postings[username] if job['title'] != job_title]

    

        return redirect(url_for('post_menu', username=username))

    # show the job if its a get request
    jobs = job_postings.get(username, [])
    return render_template('delete_job.html', jobs=jobs)


@app.route('/find_contacts')
def find_contacts():
  return redirect(url_for('connect'))


@app.route('/general->SignUp->login->post_menu->skills/<username>',
           methods=['GET', 'POST'])
def skills(username):
  if request.method == 'POST':
    skill = request.form.get('skill')
    if skill:
      return f"You have selected {skill}. Under construction"
    else:
      error_message = "Please select a skill."
      return render_template('learningNewSkills.html',
                             username=username,
                             error_message=error_message)
  return render_template('learningNewSkills.html', username=username)


@app.route('/logout')
    
def logout():
  return "logout"


@app.route('/general->SignUp->SignUp', methods=['GET', 'POST'])


def signup():
  error_message = None
  success_message = None

  if len(accounts) >= 10:
    return "Sorry, the maximum number of accounts has been reached."

  if request.method == 'POST':
    username = request.form['username']
    if username in accounts:
      error_message = "This username is already taken. Please try again."
    else:
      password = request.form['password']
      password_check = check_password(password)
      if password_check is not True:
        error_message = password_check
      else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        accounts[username] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }
        success_message = "Account created successfully!"

  return render_template('general->SignUp->SignUp.html',
                         error_message=error_message,
                         success_message=success_message)


def check_password(password):
  # Check if password is at least 8 characters long
  if not 8 <= len(password) <= 12:
    return "Password must be between 8 and 12 characters long. Please try again"

  # Check if password has at least one uppercase letter, one digit, and a special character
  if not any(char.isupper() for char in password):
    return "Password must contain at least one uppercase letter. Please try again"

  if not any(char.isdigit() for char in password):
    return "Password must contain at least one digit. Please try again"

  if not any(char in "!@#$%^&*()_+-=[]{}|;:,./<>?\\" for char in password):
    return "Password must contain at least one special character. Please try again"

  return True


@app.route('/general->SignUp->Connect', methods=['GET', 'POST'])
def connect():
  connection_result = None
  if request.method == 'POST':
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if any(account['first_name'] == first_name
           and account['last_name'] == last_name
           for account in accounts.values()):
      connection_result = "They are a part of the InCollege system. You can sign up or log in to join."
    else:
      return "They are not yet a part of the InCollege system."
  return render_template('general->SignUp->Connect.html',
                         connection_result=connection_result)


@app.route('/success_story')
def success_story():
  return "College Student Success Story: Stacy, a recent college graduate, used InCollege to network with professionals in her field. She utilized the platform's job search feature and found a position at a company. Now, she's thriving in her career thanks to the connections she made on InCollege."


@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():

  username = session.get('username')
  if not username:
    return redirect(url_for('login'))

  if request.method == 'POST':
    # handle form submission for post request
    title = request.form.get('title', '')
    major = request.form.get('major', '')
    university = request.form.get('university', '')
    info = request.form.get('info', '')
    experience = request.form.get('experience', '').split('\n')
    education = request.form.get('education', '').split('\n')

    # save the profile information
    profiles[username] = {
        'title': title,
        'major': major,
        'university': university,
        'info': info,
        'experience': experience,
        'education': education
    }

    # Redirect to the profile page for the submitted username
    return redirect(url_for('profile_view', username=username))

  # if it's a get request, render the form to update the profiles
  # get the existing profile information if it exist
  profile = profiles.get(username, {})
  return render_template('update_profile.html', profile=profile)


@app.route('/search_profile/', methods=['GET', 'POST'])
def search_profile():
  if request.method == 'POST':
    username = request.form.get('username')
    if username in profiles:
      return redirect(url_for('profile_view', username=username))
    else:
      return "Profile not found. Please try again."
  # handle get request
  return render_template('search_profile.html')


@app.route('/profile/<username>')
def profile_view(username):
  # get profile information based on the username
  profile = profiles.get(username)

  # handle case where profile is not found
  if profile is None:
    return "Profile not found"

  return render_template('profile_view.html', profile=profile)

@app.route('/search_students', methods=['GET', 'POST'])
def search_students():
    if request.method == 'POST':
        last_name = request.form['last_name']
        university = request.form['university']
        major = request.form['major']

        results = []
        for username, profile in accounts.items():
            if (last_name == '' or profile['last_name'] == last_name) and \
               (university == '' or profile['university'] == university) and \
               (major == '' or profile['major'] == major):
                results.append(username)

        return render_template('search_results.html', results=results)

    return render_template('search_students.html')


@app.route('/friend_requests')
def show_friend_requests():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    pending_requests = friend_requests.get(username, [])
    return render_template('friend_requests.html', requests=pending_requests)

@app.route('/send_friend_request/<recipient>', methods=['POST'])
def send_friend_request(recipient):
    sender = session.get('username')
    if not sender:
        return redirect(url_for('login'))

    if recipient not in accounts:
        return "Recipient not found."

    if recipient in friend_requests.get(sender, []):
        return "Friend request already sent."

    friend_requests.setdefault(recipient, []).append(sender)
    return "Friend request sent successfully."


@app.route('/accept_friend_request/<sender>')
def accept_friend_request(sender):
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if sender in friend_requests.get(username, []):
        # Accept friend request
        friends.setdefault(username, []).append(sender)
        friends.setdefault(sender, []).append(username)

        # Remove friend request
        friend_requests[username].remove(sender)

        return "Friend request accepted successfully."
    else:
        return "No pending friend request from this user."


@app.route('/my_network')
def show_network():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    user_network = friends.get(username, [])
    return render_template('my_network.html', network=user_network)


@app.route('/disconnect/<friend>')
def disconnect(friend):
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if friend in friends.get(username, []):
        friends[username].remove(friend)
        friends[friend].remove(username)
        return f"You are no longer connected with {friend}."
    else:
        return f"{friend} is not in your network."

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)
