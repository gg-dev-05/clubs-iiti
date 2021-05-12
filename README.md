<p align="center"><a href="https://clubs-iiti.herokuapp.com/"><img src="https://user-images.githubusercontent.com/59741135/109805900-04823b80-7c4a-11eb-8335-d59325487ab4.png" alt="CLUBSIITI" width="200"></a></p>
<h4 align="center">A club management system build for  <a href="https://www.iiti.ac.in/" target="_blank">IITI</a> community.</h4>
<p align="center">
  <a href="#aim">AIM</a> •
  <a href="#local-installation">Local Installation</a> •
  <a href="#links">Links</a> •
  <a href="#testing">Tesing</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#team-members">Team Members</a>
</p>

<p align="center">
A project under the course <b>CS-258</b>, we created this application under the guidance of Puneet Gupta Sir and Anup Gupta Sir.
</p>


## AIM

”<b>IITI Club Management WEBSITE</b>” creates a space for Teachers, IITI students,nonIITI students and Office Staffs for making an effort to resume the activities of the
clubs which have stopped due to the pandemic for <br>example:-Dance, Music, etc...
After logging into the website by IIT-I Mail id, a student has been given a unique
id, by using which he/she can reach out to form-fill-up page.<br>
It will take his/her personal information,info about clubs which he/she have joined and info about the clubs for which he has applied.He will be added as a student of that particular club only after being approved by the club head.<br>Also the student can see the recent activities of any club and they can also see who all are already a part of the club.Student profile will contain all his personal information, past positions, recent positions etc...<br>
Office staff, admins and club Heads can control the website according to the club
which they have been assigned . But of course, with the permission of Director.
Directors’ main work is to assign permission to the admins,<br> club heads and office
staff when they want to create a new club or dissolve any existing club or merging
two clubs.He also has all the authorities that are with the admins and the staff.
He can also directly post<br> notice to the website, admins or club heads.

## Local Installation

-   Clone this repo using <code>git clone https://github.com/gg-dev-05/clubs-iiti.git</code>
-   After cloning create a <code>.env</code> file to store all the environment variables
-   Fill in the <code>.env</code> file with the content as follows

```
env = dev
CLEARDB_DATABASE_URL = RETRACTED (Put your mysql database url here)
client_id = RETRACTED (Put Your client id given by google developer console)
client_secret =  RETRACTED (Put Your client secret given by google developer console)
mail_id = RETRACTED (Enter the email using which all clubs related emails will be sent)
mail_password =  RETRACTED (Password for the above entered email-id)
secret_key =  RETRACTED (Any secret key of your choice)
```

<em>Here RETRACTED refers we must not share this variable, and thus should not be present in public repos</em>

-   After setting <code>.env</code> file install all the required python packages using
    <code>pip install -r requirements.txt</code>
-   Before running the server create all the required mysql tables and populate them by running <code><a href="https://github.com/gg-dev-05/clubs-iiti/blob/master/sql/clubs-iiti.ddl">clubs-iiti.ddl</a></code> and <code><a href="https://github.com/gg-dev-05/clubs-iiti/blob/master/sql/populate.sql">populate.sql</a></code> in your sql editor.
-   Start the server using <code>python <a href="https://github.com/gg-dev-05/clubs-iiti/blob/master/app.py">app.py</a></code>


## USAGE STEPS:-

-   New student has to fill a form to give his/her details in order to continue to explore the website with different clubs.<br>
-   Then He can choose to join club he is interested in by clicking on Join button.<br>
-   email will be sent to the student regarding details of the meeting. <br>
-   Meeting will be set by clubhead with the aspirants. <br>
-   If selected, he can continue


## Testing
In Order to run the automated testing in flask download chromewebdriver according to your version(for refernce see this tutorial <a href="https://youtu.be/Xjv1sY630Uc">click here</a>) and then  create a secret.py file and write the content as follows

```
email = RETRACTED (Enter the email for which you want to run the tests)
password =  RETRACTED (Password for the above entered email-id)
secret_key =  RETRACTED (Any secret key of your choice)
rasta=RETRACTED (path for chromewebdriver)
```


## Register Page

New Student can register by Filling out the details in this registration form <br>
<img src="https://i.imgur.com/KOrZKnW.png" width="500-px">

## Home

Home Page displays the different clubs and the current events of different clubs<br> with
a dashboard on the top with options menu of login,testinomials,apply etc.
as Shown in FIG <br>
<img src="https://i.imgur.com/cpKtjdb.png" width="500-px">
<br>
<img src="https://i.imgur.com/8ei7Vxj.png" width="500-px">

## Club Home Page

Home page of club containing description, events, members of the club
as shown in FIG <br>
<img src="https://i.imgur.com/Q6h2uEn.png" width="500-px">

## WORK FLOW

<img src="https://i.imgur.com/XtWWSBc.png" width="500-px">

## User Interface

<b>The User Interface</b> of the Website is crystal clean, sleek and simple with all the
utilities and functionalities to compliment the user with the best services. <br>
Diving into the color schema of the website , its a combination of sapphire blue and cream white
colors with a formal and sober look .
<br>The different clubs are being assembled in a
GRID fashion along with their Official Club Logo

## Links

We have hosted the website on heroku: <a href="https://clubs-iiti.herokuapp.com/">Visit Us!!</a>  
Demo Video : <a href="https://drive.google.com/file/d/1Q5iBTbU-AIOkCVzjc3rHZ2K9cDvHjiG9/view?usp=sharing">LINK</a>

## Tech Stack

<ul>	
	<ul>
		<b>FRONTEND</b>
		<ul>
			<li>HTML</li>
			<li>CSS (Bootstrap 4) </li>
			<li>JS(JQuery)</li>
		</ul>
	</ul>
	<ul>
		<b>BACKEND</b>
		<ul>
			<li>FLASK (Python)</li>
			<li>Flask-MySQL</li>
		</ul>
	</ul>
</ul>

## Team Members

<p align="center">
<a href="https://github.com/dmdivyansh">
  	<img src="https://github.com/dmdivyansh.png" width="50px">
</a>

<a href="https://github.com/eeshmalvi">
	<img src="https://github.com/eeshmalvi.png" width="50px">
</a>

<a href="https://github.com/gg-dev-05">
	<img src="https://github.com/gg-dev-05.png" width="50px">
</a>

<a href="https://github.com/somyamehta24">
	<img src="https://github.com/somyamehta24.png" width="50px">
</a>

<a href="https://github.com/Tanishq-30">
	<img src="https://github.com/Tanishq-30.png" width="50px">
</a>
</p>

<p align="center">
		<a href="https://github.com/dmdivyansh">Divyansh Maheshwari</a> •
		<a href="https://github.com/eeshmalvi">Eish Malvi</a> •
		<a href="https://github.com/gg-dev-05">Garvit Galgat</a> •
		<a href="https://github.com/somyamehta24">Somya Mehta</a> •
		<a href="https://github.com/Tanishq-30">Tanishq Jain</a>
</p>
