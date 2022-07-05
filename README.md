# Kart-O-City
<!-- Output copied to clipboard! -->

<!-- You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 27 -->


![alt_text](images/image1.png "image_tooltip")


<h2>FCS User Guide Group No. : 8</h2>


**Kart-O-City **: 

A secure and aesthetic web e-commerce application that allows customers to purchase apparel, mobiles, toys and other electronics through verified and encrypted transaction channels, while also allowing sellers to put up their items for sale.

 

<h4>**Technologies Used :** </h4>


Django DB, AWS S3, Django, HTML, CSS, JS, Apache, RazorPay

 

<h4>**How to Access the site :** visit **https://192.168.2.241**</h4>


 

<h3>
            **Home Page or Landing Page:**</h3>




* Consists of Website Logo
* Home page button which is used to redirect back to this landing page when needed,
* categories drop down menu which displays different categories of products available,
* Search bar(It only accepts alphanumeric string and space of length less than 50) and search button to search for products by name,
* Cart button(which has live, dynamic counter of items in cart as you shop)
* And Signup and Login buttons(by default they lead to signup and login for a buyer)
* And contains pictorial links to various items arranged according to their popularity for you to buy.
* The Home Page also displays all the items for sale


![alt_text](images/image2.png "image_tooltip")



                **Signup - Buyer/Customer**

**	**



* Opens up a form on the site to take information required for sign up
* Takes First Name, Last Name, Phone Number, Email ID and password which will be used for the new account(password field is anonymised)
* After signing up, you need to login again


![alt_text](images/image3.png "image_tooltip")


After filling the details and clicking on Create an Account, a page opens prompting us for the 6-digit OTP sent on our registered email(You will receive the OTP on your email and will expire after 2 mins). Also a virtual keyboard appears on the screen when you click on the OTP field which the user can use to ensure more secure browsing.


![alt_text](images/image4.png "image_tooltip")


Once signed up it returns you to the home page


            **Sign In - Customer**


![alt_text](images/image5.png "image_tooltip")


Consists of an email and password field used to login, also has a captcha(4 Capital Alphabets) field for extra security. After completing all these fields one should press ‘Send OTP’ to proceed in the login process (You will receive the OTP on your email and will expire after 2 mins). Also a virtual keyboard appears on the screen when you click on the OTP field which the user can use to ensure more secure browsing.

<h5>Password : </h5>



![alt_text](images/image6.png "image_tooltip")



![alt_text](images/image7.png "image_tooltip")


After entering the OTP successfully, one is redirected back to the landing page however they can see a circular image of themselves on the top right corner indicating they have been logged in.


![alt_text](images/image8.png "image_tooltip")



                **Profile Page**


![alt_text](images/image9.png "image_tooltip")


**The profile page allows the user to check their order and bill payment history, allows them to change their password **


![alt_text](images/image10.png "image_tooltip")



![alt_text](images/image11.png "image_tooltip")



            **Making Purchases as a Customer**

Go to the home page/search for your item by name/search for the item within categories


![alt_text](images/image12.png "image_tooltip")


It shows options to share the link of the item on facebook, whatsapp and even telegram. It also shows three images of the item in a dynamic carousel fashion.

Click on Add to Cart button for all such items which you wish to buy

Once you’ve finished adding to cart, click on the Cart button on the top right


![alt_text](images/image13.png "image_tooltip")


Click on Checkout after verifying the items, prices and quantity(quantity can be increased from the page dedicated to the item)

After clicking on Checkout, a prompt asks you for the delivery address, successfully adding which will take you to the next page where you need to add the OTP you would have received at your email address.


![alt_text](images/image14.png "image_tooltip")


Upon successfully adding the OTP, you would be asked to Proceed to Razorpay for payment.


![alt_text](images/image15.png "image_tooltip")


On the next page, the Razorpay in-site window opens


![alt_text](images/image16.png "image_tooltip")


Choose the convenient payment method and follow the instructions on screen


![alt_text](images/image17.png "image_tooltip")


Click on the Pay button and complete the payment


![alt_text](images/image18.png "image_tooltip")


Upon successful payment the cart will be emptied and a successful order message will appear.


                **Signup Seller**


![alt_text](images/image19.png "image_tooltip")


Similar steps as signing up as a customer, click on Create an Account to proceed to the OTP step.

Upon successful login, you’ll be redirected to the home page where now you can login as a seller


                **Login- Seller**


![alt_text](images/image20.png "image_tooltip")


Login by using registered email, password, and also input the captcha

Once you’ve logged in successfully you need to upload a Pan Card and GST document(in pdf format)(names of the two must be distinct from both the files), as part of a requirement for the entire seller process.

Here, the profile button will also act as a Logout button in order to log out the seller from the website .


![alt_text](images/image21.png "image_tooltip")


Choose the required files locally and proceed by clicking upload.

On successful completion this message will be displayed
![alt_text](images/image22.png "image_tooltip")


Then the Admin of the website will approve whether the seller can use the website or not.

(For admin access, you need to apply for specific permission by mailing to **[kartocity.pvt.ltd@gmail.com](https://mail.google.com/mail/u/0/#sent?compose=new)**)

Once approved, the seller will receive a confirmation email that they have successfully been verified as a seller.

Next, when the seller logs in to the website, they will get a screen where they need to add product details of the product they wish to sell over the website.


![alt_text](images/image23.png "image_tooltip")


Then it needs to wait for approval from the admin as well.

After getting approved from Admin we can view the product on the landing page with other products.


![alt_text](images/image24.png "image_tooltip")



                **Forgot Password**

If you have forgotten your password, go to the login page of either the seller or the customer, and enter your email address


![alt_text](images/image25.png "image_tooltip")


If the seller is registered, they will receive an OTP on their email address which will lead them to the next page to reset their password


![alt_text](images/image26.png "image_tooltip")


On successful reset you get a “Password Updated” Message.


                **Simple admin login :**


![alt_text](images/image27.png "image_tooltip")


**For admin access enter /admin in the url bar after the ip or paste the given url in the search bar : **https://192.168.2.241/admin

**Username : **admin

**Password : **FCS2021@koc

**Current Views available in admin account : c**ategories of the products, all the products , and customer details.

**Limitations (Due to limited ram and space):**



1. Documents uploaded need to have distinct names, the latest document with the same name will overwrite the previous document.
2. Otp might give an alert of wrong otp during the first login.
3. During Seller login you might see an error message with name Forbidden in that case kindly go back to the login page switch to Seller login and retry with your used credentials it will work.
4. During the seller login if the otp fails the login page defaults to Customer Login so the tester or the user is requested to switch to the seller login from the button given below on the login page.
