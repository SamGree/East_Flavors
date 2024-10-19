# Table of Contents


## Goals
   - Create an operational website for a restaurant.
   - Enable users to reserve a table for their preferred date and time through an easy-to-use form.
   - It should also provide users with the ability to easily book more tables (**but should not choose same hour with same date, but 1 hour apart ok**) or cancel their reservations.
   - Display the restaurant's menu to the user.
   - Enable users to register an account.
-------------------
-------------------


## Key Features

- Home page
   - The homepage greets users with a visually appealing image of a delicious meal, immediately capturing attention and setting the mood for the dining experience.

   - Logo left corner.
   - The top menu provides easy access to essential sections such as Home, Menu,Bookings, Login, and Register, ensuring smooth navigation.


   - Prominent buttons like *Explore Menu* and *Book a table* make it convenient for users to view the menu or make a reservation directly from the homepage.


   - A gallery of vibrant, high-quality food images offers users a glimpse of the restaurant's dishes, enticing them to explore more or place an order.


   - A personalized welcome message (**Welcome to East Flavors!**) makes the experience inviting and establishes a connection with the restaurant's brand.


   - The **About Us** section effectively communicates the restaurant’s 15-year journey, emphasizing a deep connection to Middle Eastern culinary traditions. It tells a story that appeals to both long-time fans and new visitors.
    The text welcomes everyone, from first-time visitors to regulars, making it clear that the experience is more than just about food—it’s about memorable dining moments.


   - The **Find Us** section provides essential contact details and opening hours, ensuring that customers can easily reach the restaurant or plan their visit.
   
   - Contact Information:

- Footer
   - Social media icons for email, Instagram, and Facebook are visible.

---------------------
---------------------
- Menu page 
   - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.

   - The top menu provides easy access to essential sections such as Home, Menu,Bookings, Login, and Register, ensuring smooth navigation.

 
   - Available Dishes:
The page highlights a selection of dishes with images and brief descriptions. This gives users a visual understanding of the food they can order.

---------------------
---------------------
- Register Page
   - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.

   - The top menu provides easy access to essential sections such as Home, Menu,Bookings, Login, and Register, ensuring smooth navigation.
   - User-Friendly Registration Form:

   - The form is simple, allowing users to sign up with minimal effort.
   - Fields include
      - Username:
      - Email Address:
      - Password:
      - Password Confirmation:

      - login.

   - Login Link for Existing Users:

      - If a user already has an account, they can easily switch to the Login page via the link: ***Already a member? Login.*** This reduces friction for returning users, offering a seamless experience. 
    
   - footer
     -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.

-----------------------
-----------------------
- Login Page
   - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.

   - The top menu provides easy access to essential sections such as Home, Menu,Bookings, Login, and Register, ensuring smooth navigation.

   - Simple Layout: Clean, minimalist design with a split layout—restaurant image on one side, login form on the other.

   - Login Form: Includes fields for username, password, and a prominent **Login** button for easy access.
   - New User Call to Action: Clear link to register for users without an account, improving user flow.
   
   - Footer
     -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.

------------------------
------------------------
- BOOKINGS page
   - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.

   - The top menu provides easy access to essential sections such as Home, Menu, Bookings, Logout, and user name left corner, ensuring smooth navigation.

   - Simple Booking Form: Users can easily select a date, time, and number of guests to book a table.

   - Availability Info: Clear indication that the restaurant operates between 11 AM and 11 PM.

   - Confirmation Button: A prominent “Book Now” button to finalize reservations quickly.

   - The restaurant image on the left reinforces the ambiance and brand.

- Your Bookings:
   - Booking Details Display: Shows user’s current booking with details like date, time, and number of guests.
   - Cancel Booking Option: Includes a clear and clickable "Cancel Booking" button for easy management of reservations.

     - Footer
     -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.
-----------------------
-----------------------

## Design Philosophy
- User-Centered Design:
  - The design emphasizes ease of navigation, ensuring users can quickly find what they need, such as menu options, table bookings, or location information. With clear sections like "Welcome to East Flavors" and "Find Your Best Food," users are guided seamlessly through the content.

- Visual Appeal and Authenticity:
  - The homepage uses high-quality images of food that capture the essence of Middle Eastern cuisine. This visual appeal is key to making users feel connected to the experience, as the design reflects the vibrancy and diversity of the dishes.
- Minimalistic Yet Informative:
  - The layout is simple yet informative, with clean sections and minimal text, allowing the food and visuals to speak for themselves. This minimalism ensures that users are not overwhelmed but can still access all necessary information, such as contact details, opening hours, and the booking system.      
- Color Palette.
  - Primary Colors:(#061918) Used for the header and footer. 
  - White (#FFFFFF): Applied for text and backgrounds to enhance readability and contrast against the darker elements.
  - Red (#FF0000): Used as an accent color for the navigation links to indicate the active page.
  - Body Background Colors: var(--color-grey-0).
  - Background color of the dish descriptions: var(--color-red-100) this soft and warm tone makes the text readable and adds a light.
  - Text Color black: used in the meals detailed descriptions and prices to maintain simplicity and clarity.
- Typography.
  - The typography for the East Flavors website is chosen to enhance readability, create a professional look, and align with the brand's modern and elegant feel. It is designed to ensure that the content is clear and accessible to all users while maintaining a cohesive visual identity.
- Design Process.
  - The design process for the East Flavors website was an iterative journey focused on creating a user-friendly, visually appealing, and functional restaurant website. As the sole designer, I managed all aspects of the design, from conceptualization to the final product, ensuring consistency and alignment with the restaurant’s brand.    
  - Research & Inspiration:
    - I began by researching modern restaurant websites, focusing on usability, aesthetics, and how food imagery can influence user engagement. Inspiration was drawn from both local and international restaurant brands to identify best practices in web design, user interface, and user experience.
  - Branding & Visual Identity:
    - Establishing a strong visual identity for East Flavors was a priority. I worked on creating a logo that reflects the restaurant’s Middle Eastern heritage with a modern twist. The color palette, fonts, and imagery were chosen to reflect warmth, authenticity, and a high-quality dining experience.
  - Responsive Design:
    - Recognizing that many users would access the website from mobile devices, I prioritized responsive design from the start. I ensured that all layouts would adapt seamlessly to different screen sizes, making the experience equally rich and engaging on mobile, tablet, and desktop. 
  - Wireframing & Layout Design:
    - Using wireframes, I sketched out the layout for each page, focusing on simplicity and ease of navigation. The homepage was designed to feature stunning food photography and an immediate call to action (menu exploration and booking a table).
  - Finalization & Launch:
    - The final design of East Flavors reflects a welcoming, vibrant, and user-friendly experience. Each element, from the color palette to typography and imagery, was thoughtfully crafted to engage users while showcasing the restaurant’s offerings and simplifying the online booking process.  
    ------------------
    ------------------
## Models  
  - Bookings Model

  

  - Menu Model

  -------------------
  -------------------
## Technologies Used  
    - Python Modules:

      asgiref==3.8.1
      cloudinary==1.36.0
      dj-database-url==0.5.0
      dj3-cloudinary-storage==0.0.6
      Django==4.2.16
      django-allauth==0.57.2
      django-summernote==0.8.20.0
      gunicorn==20.1.0
      oauthlib==3.2.2
      pillow==10.4.0
      psycopg2==2.9.9
      PyJWT==2.9.0
      python3-openid==3.2.0
      pytz==2024.2
      requests-oauthlib==2.0.0
      sqlparse==0.5.1
      urllib3==1.26.20
      whitenoise==6.5.0 


  - Django:
    - Main Python framework for project development. 
    - django-allauth is used for managing user accounts in the booking system.
    - Django's views handle database queries, while the Django Templating Engine renders the data onto the site pages, ensuring a dynamic and responsive user experience.
  - Deployment Platforms:  
    - Heroku: Cloud-based deployment platform.
    - ElephantSQL: Database hosting service.
   