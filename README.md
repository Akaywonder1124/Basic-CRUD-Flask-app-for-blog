<h1>BASIC CRUD FLASK APP FOR BLOG </h1>
<h2>Content</h2>
<ul>
  <li>Description</li>
  <li>Overview</li>
  <li>User Authentication</li>
  <li>Features</li>
  <li>Conclusion</li>
</ul>
<h2>Description</h2>
<p>
CRUD Meaning: CRUD is an acronym that comes from the world of computer programming and refers
 to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete. 
 In This App, a user will be able to Create a post, Modify the post, Read and also Delete it This gives users full control over their blog post
</p>

<h2>Overview</h2>
<h3>The Video below shows an overview of what an anonymous user will be able to see</h3>

https://user-images.githubusercontent.com/97950441/181084681-fde09f9f-a703-4933-bbbe-62dd6dfda04c.mp4

<h2>User Authentication</h2>
<p>User authentication verifies the identity of a user attempting to gain access to  the CRUD system by authorizing a human-to-machine transfer of credentials in order to confirm a user's authenticity.</p>
<h3>Extensions Used For User Authentication<h3>
  
  <h4>Flask-wtform</h4>
  <p>
  WTForms are really useful it does a lot of heavy lifting when it comes to data validation on top of the CSRF protection .
  Another useful thing is the use combined with Jinja2 where there is need to write less code to render the form
  </p>
  <h4>Flask-Login</h4>
    <p>
  Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, 
  and remembering your users' sessions over extended periods of time. 
  It will: Store the active user's ID in the session, and let you log them in and out easily.
  </p>
  <h4>Flask Sqlalchemy </h4>
    <p>
    I chose Sqlalchemy as my ORM(Object relational Mapper)
    SQLAlchemy is great because it provides a good connection / pooling infrastructure; a good Pythonic query
    building infrastructure; and then a good ORM infrastructure that is capable of complex queries and 
    mappings (as well as some pretty stone-simple ones).
  </p>
   
  <h4>Bcrypt</h4>
    <p>
  BCrypt is based on the Blowfish block cipher cryptomatic algorithm and takes the form of an adaptive hash function
  Using a Key Factor, BCrypt is able to adjust the cost of hashing. With Key Factor changes, the hash output can be influenced. 
  In this way, BCrypt remains extremely resistant to hacks, especially a type of password cracking called rainbow table.
  </p>
<br>
<h3>User Registration</h3>
<div>
<span><img width="960" alt="register" src="https://user-images.githubusercontent.com/97950441/181091688-2255b3c3-cb59-4b47-a8a0-b01e8f24855c.png"></span>
  <h3>Registration Validation</h3>
<span><img width="958" alt="registration errors" src="https://user-images.githubusercontent.com/97950441/181091770-0adecf68-a25d-474c-a260-d032034631db.png">
</span>
 <div>
   <h3>User Login</h3>
   <div>
<span>
  <span><img width="950" alt="login" src="https://user-images.githubusercontent.com/97950441/181099468-d5401a91-99de-46ee-918a-6dc6778231a2.png"></span
  <h3>User Validation</h3>
<span><img width="958" alt="login error" src="https://user-images.githubusercontent.com/97950441/181098368-64a2c900-9d2f-4032-80fc-c5f6d3d1bf0c.png"></span>
 <div>


