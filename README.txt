Wedblog(final project by Divesh Angula) - Running at http://block647038-n5j.blueboxgrid.com

This is my attempt to recreate my wedding website, at least the parts that are important to me and .

Goal - Create a Wedding website where guests can register,login,RSVP,leave blog comments and view wedding information.
       Also provided extra stats when admin are logged like RSVP count or guest specific infomation. 

Following is the Description of Functionality of the web site.
1. Main page and Venue page are viewable to all.

2. a Registration link is available for users to be able to register to access the web site.

3. Once users are logged in(registered) following views  are available
    a. A link for RSVP and blog appear on the top control bar
    b. Users can click the RSVP link and Rsvp for the wedding.
       One Rsvp is submitted, users are rerouted to main page and a message based on 
       Rsvp status selected is flashed on top right.
    c. Users can view Blog page. where blogs for all users are shown. Users can add a blog entry.
    d. RSVP page cannot be access if user is not logged in.
 
4. Users with admin privileges have extra link stats accessible.
	a. this page is only accessible to users with admin privileges. Non-admin user cannot access this page.
	b. Stats page shows the RSVP stats count.
	c.This page also has a list of links to all users grouped by rsvp status.
    d. Each user link displays specific details about the user. They are
      i. RSVP status
      ii. All blog entries by the user and
      iii.An exta from to save additional information is   available on the right side.


What was not covered  - I wanted to do the following stuff but i could'nt get it done in time.
a. Have custom user registration - got half way,there, views and forms were good, but could finish a custome backend
b. Have multi level blog - where users could leave comments on blog entries. Got too complex and viewing a page with blog and corresponding comments was nasty so i had to drop it.

Instructions to run website locally.
1. create a virtaul env and install django verson 1.4.3 and django-registration
2. clone webstite - https://github.com/dangula/wedblog.git on you local virtual env
3. cd to finalsite and run python manage.py runserver.


Additional Information.
I have staged some data to play with the web site Running at http://block647038-n5j.blueboxgrid.com

 Users with admin privs(username and password is same)
 a. admin
 b. divesh.
 c. stephaine.

 Users with non-admin privs and their corresponding rsvp stats(username and password same again)
 a. jack(yes +2)
 b. jim(yes +1)
 c. adam(no)
 d. ashley(no)
 e. terry(maybe)
