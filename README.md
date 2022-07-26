<h1>BASIC CRUD FLASK APP FOR BLOG </h1>
<h2>Content</h2>
<ul>
  <li>Description</li>
  <li>Overview</li>
  <li>User Authentication</li>
  <li>Features</li>
 
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
  <span><img width="950" alt="login" src="https://user-images.githubusercontent.com/97950441/181099468-d5401a91-99de-46ee-918a-6dc6778231a2.png"></span>
  
  <h3>User Validation</h3>
<span><img width="958" alt="login error" src="https://user-images.githubusercontent.com/97950441/181098368-64a2c900-9d2f-4032-80fc-c5f6d3d1bf0c.png"></span>
    <h3>Request Reset Token</h3>
  <span>
   <img width="951" alt="reset password" src="https://user-images.githubusercontent.com/97950441/181102249-df86d706-86d3-47ec-bd38-3d50b5cc86ff.png">
  </span>
  <h3>Reset Token Message</h3>
  <p>The message was sent using flask mail you can as well use smtplib they use the same protocol</p>
<span><img width="606" alt="reset message" src="https://user-images.githubusercontent.com/97950441/181100650-5e673153-6003-4783-adc3-ea8c37d8e521.png"></span>
    <h3>Reset Password</h3>
<span><img width="950" alt="reset password form" src="https://user-images.githubusercontent.com/97950441/181100741-14316d7e-16e5-4559-a289-4a5599a2a78a.png">
      <h3>Reset Token Validation</h3>
<span><img width="943" alt="reset password validation" src="https://user-images.githubusercontent.com/97950441/181101167-229c0aae-e039-411d-ad8f-569836b78421.png">
</span>
 <div>
   <h3>User Account</h3>
<img width="946" alt="account  age" src="https://user-images.githubusercontent.com/97950441/181105753-67863e2c-2016-478f-9d88-4b7c4be715bf.png">
   
<h2>Post Features</h2>
   
   <h3>Create Post</h3>
   <img width="947" alt="create post" src="https://user-images.githubusercontent.com/97950441/181105800-9f275310-1384-4d1a-a6ac-f677bbf79d10.png">

  
   <h3>The video below shows the update and delete feature for authenticated user</h3>
   <h4> The logic behind this feature also checks and make sure only post authors can make changes to their post</h4>

   https://user-images.githubusercontent.com/97950441/181105289-7b8ef65e-16c6-43c7-ad4a-8669da79c717.mp4


   
