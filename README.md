# East flavors

![chicken on the grill](/readme.images/front.png)

- Direct link to the website:
  [East flavors](https://east-flavors-6a20eeb5fe30.herokuapp.com/)
- Link to the github: [Github link](https://github.com/SamGree/East_Flavors)

# Table of Contents

- [Design Philosophy](#design-philosophy)
- [Design Wireframe](#design-wireframe)
- [Key Features](#key-features)
- [Admin page](#admin-page)
- [Models](#models)
- [Technologies Used](#technologies-used)
- [Manual testing](#manual-testing)'
- [Validator testing](#validator-testing)
- [Bugs](#bugs)
- [Credits](#credits)

## Goals

- Create an operational website for a restaurant.
- Enable users to reserve a table for their preferred date and time through an easy-to-use form.
- It should also provide users with the ability to easily book more tables (**but should not choose same hour with same date, but 1 hour apart**)
- Add, edit or cancel their reservations.
- Display the restaurant's menu to the user.
- Enable users to register an account.
- East Flavors restaurant is co-owned by two partners who oversee daily operations. They manage a staff organized into two teams, ensuring the restaurant is open every day.

---

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
  - The design process for the East Flavors website was an iterative journey focused on creating a user friendly, visually appealing, and functional restaurant website. I managed all aspects of the design, from conceptualization to the final product, ensuring consistency and alignment with the restaurant’s brand.
  - Research & Inspiration:
    - I began by researching modern restaurant websites, focusing on usability, aesthetics, and how food imagery can influence user engagement.
  - Branding & Visual Identity:
    - Establishing a strong visual identity for East Flavors was a priority. I worked on creating a logo that reflects the restaurant’s Middle Eastern heritage with a modern twist. The color palette, fonts, and imagery were chosen to reflect warmth, authenticity, and a high-quality dining experience.
  - Responsive Design:
    - Recognizing that many users would access the website from mobile devices, I prioritized responsive design from the start. I ensured that all layouts would adapt seamlessly to different screen sizes, making the experience equally rich and engaging on mobile, tablet, and desktop.
  - Wireframing & Layout Design:
    - Using wireframes, I sketched out the layout for each page, focusing on simplicity and ease of navigation. The homepage was designed to feature stunning food photography and an immediate call to action (menu exploration and booking a table).
  - Finalization & Launch:
    - The final design of East Flavors reflects a welcoming, vibrant, and user-friendly experience. Each element, from the color palette to typography and imagery, was thoughtfully crafted to engage users while showcasing the restaurant’s offerings and simplifying the online booking process.

---

## Design Wireframe.

- Mobile wireframe:
- Same wireframe applies to the tablet.

![home page](/readme.images/mobile.home.page.png)![home page](/readme.images/mobile.home.navbar.png)![home page](/readme.images/menu.mobile.png)![home page](/readme.images/login.mobile.png)![home page](/readme.images/register.mobile.png)![home page](/readme.images/booktable.mobile.png)![home page](/readme.images/mobile.mybooking1.png)

---

- Desktop and laptop wireframe:
  ![wireframe for laptop](/readme.images/wire.laptop.home.png)
  ![wireframe for laptop](/readme.images/wire.laptop.menu.png)
  ![wireframe for laptop](/readme.images/wire.laptop.register.png)![wireframe for laptop](/readme.images/wire.laptop.login.png)![wireframe for laptop](/readme.images/wire.laptop.book.table.png)![wireframe for laptop](/readme.images/lap.booking1.png)

---

## Key Features

- Home page

  - The homepage greets users with a visually appealing image of a delicious meal, immediately capturing attention and setting the mood for the dining experience.
    ![chicken on the grill](/readme.images/front2.png)

  ***

  - Logo left corner.
    ![logo img](/readme.images/logo.png)

  ***

  - The top menu provides easy access to essential sections such as Home, Menu,Bookings, Login, and Register, ensuring smooth navigation. I made it easy for the user to know which page they are currently on by highlighting the corresponding item in the navbar with a red color.
    ![navbar](/readme.images/nav1.png)

  ***

  - A personalized welcome message (**Welcome to East Flavors!**) makes the experience inviting and establishes a connection with the restaurant's brand.
    ![welcome message](/readme.images/welcome.png)

  ***

  - Prominent buttons like _Explore Menu_ and _Book a table_ make it convenient for users to view the menu or make a reservation directly from the homepage.
    ![img buttons](/readme.images/explore.menu.png)

  ***

  - A gallery of vibrant, high-quality food images offers users a glimpse of the restaurant's dishes, enticing them to explore more or place an order.
    ![img of people and food](/readme.images/foodgallary.png)

  ***

  - The **About Us** section effectively communicates the restaurant’s 15-year journey, emphasizing a deep connection to Middle Eastern culinary traditions. It tells a story that appeals to both long-time fans and new visitors.
    The text welcomes everyone, from first-time visitors to regulars, making it clear that the experience is more than just about food—it’s about memorable dining moments.
    ![text](/readme.images/abouttext.png)

  ***

  - The **Find Us** section provides essential contact details and opening hours, ensuring that customers can easily reach the restaurant or plan their visit.
    ![restaurant address](/readme.images/findus.png)

  ***

- Footer
  - Social media icons for email, Instagram, and Facebook are visible.
    ![Social media icons](/readme.images/footer.png)

---

- Menu page
  - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.
    ![logo img](/readme.images/logo.png)
  ***
  - The top menu provides easy access to essential sections such as Home, Login, and Register, ensuring smooth navigation.
    ![menu nav bar](/readme.images/nav.menu1.png)
  ***
  - Available Dishes:
    The page highlights a selection of dishes with images and brief descriptions. This gives users a visual understanding of the food they can order.
    ![images of Dishes](/readme.images/menu.gallery.png)
  ***
- Footer
  - Social media icons for email, Instagram, and Facebook are visible.
    ![Social media icons](/readme.images/footer.png)

---

- Register Page

  - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.
    ![logo img](/readme.images/logo.png)

  ***

  - The top menu provides easy access to essential sections such as Home, Menu and Login, ensuring smooth navigation.
    ![navbar register](/readme.images/register.nav1.png)

  ***

  - User-Friendly Registration Form:

  - The form is simple, allowing users to sign up with minimal effort.
  - Fields include

    - Username:
    - Email Address:
    - Password:
    - Password Confirmation:

    - login.

  - Login Link for Existing Users:

    - If a user already has an account, they can easily switch to the Login page via the link: **_Already a member? Login._** This reduces friction for returning users, offering a seamless experience.
      ![form register](/readme.images/register.form.png)

    ***

  - footer
    -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.
    ![Social media icons](/readme.images/footer.png)

---

- Login Page

  - Logo left corner. Clicking the logo in the top left corner will take you back to the homepage.
    ![logo img](/readme.images/logo.png)

  ***

  - The top menu provides easy access to essential sections such as Home, Menu,Bookings and Register, ensuring smooth navigation.
    ![navbar img](/readme.images/login.nav1.png)

  ***

  - Simple Layout: Clean, minimalist design with a split layout—restaurant image on one side, login form on the other.

  - Login Form: Includes fields for username, password, and a prominent **Login** button for easy access.
  - New User Call to Action: Clear link to register for users without an account, improving user flow.
    ![login form and dinning img](/readme.images/login.form.png)

  ***

  - Footer
    -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.
    ![Social media icons](/readme.images/footer.png)

---

- BOOKINGS page

  - Logo left corner. Clicking the logo in the top left corner
    will take you back to the homepage.
    ![logo img](/readme.images/logo.png)
    ***
  - The top menu provides easy access to essential sections such as Home, Menu, Bookings, Logout, and user name come up in the right top corner, ensuring smooth navigation.
    ![navbar and user name](/readme.images/inlog.navbar.png)

  ***

  -
  - Simple Booking Form: Users can easily select a date, time, and number of guests to book a table.

  - Availability Info: Clear indication that the restaurant operates between 11 AM and 11 PM.

  - Confirmation Button: A prominent “Book Now” button to finalize reservations quickly.
    ![navbar and user name](/readme.images/booking.page.new.png)

  ***

- My Bookings:
  - Booking Details Display: Shows user’s current booking with details like date, time, and number of guests.
  - Cancel Booking Option: Includes a clear and clickable "Add Booking", "Edit booking" and "Cancel booking". - Click on add booking it will take you to book a table form.
  - Click on edit booking it will take you to booking page with current booking you wish to update it.
  - Click on cancel booking will delete reservation.
    ![my booking page](/readme.images/my.booking.new.png)
  ***
  - Footer
    -Clickable Links: Social media icons for email, Instagram, and Facebook are visible.
    ![Social media icons](/readme.images/footer.png)

---

### User notification

- First time user register.
  ![welcome](/readme.images/welcome.newuser.png)
  ***
- User logout.
  ![logout](/readme.images/logout.message.png)
  ***
- User logged in.
  ![login](/readme.images/login.welcome.back.png)
  ***
- User booking successful.
  ![booking](/readme.images/booking.successfull.png)
  ***
- User update booking.
  ![booking](/readme.images/booking.update.png)
  ***
- User booking alert
  ![one.m.ahead](/readme.images/one.m.ahead.png)
  ***
- User selected date in the past.
  ![date](/readme.images/date.invalid.png)
  ***
- User selected time in the past.
  ![time](/readme.images/time.invalid.png)
  ***
- User canceled booking.
  ![canceled](/readme.images/booking.cancel.png)

---

## Admin page

- This is the Django admin dashboard, a built-in feature that allows superusers to manage and interact with models and data from the web interface.
  - Site administration panel:
    - This panel gives access to different sections of your Django application.
  - Sections and Models:
    - ACCOUNTS:
      - Email addresses: Manage email addresses associated with user accounts.
    - AUTHENTICATION AND AUTHORIZATION:
      - Groups: Manage user groups and permissions.
      - Users: Add, view, edit, or delete users in the application.
    - BOOKING:
      - Bookings: Manage bookings made on the website.
      - Tables: Handle table-related information (likely referring to tables in a restaurant setting).
    - DJANGO SUMMERNOTE:
      - Attachments: Manage file attachments using the Django summernote package.
    - MENU:
      - Manage restaurant menu items and can easily add it here.
    - SITES: Manage configurations related to the **sites** framework, often used for multi-site setups.
    - Recent Actions Panel:
      - On the right side, it displays a list of recent actions performed by the logged-in admin user, such as adding, changing, or deleting objects.(in this case, menu items).
    - Header:
      - The header includes links for the admin to view the site, change the password, and log out.
        ![admin page](/readme.images/admin.page.png)
    ***
    - This is the **Add menu** form in the Django admin interface. It allows the admin to add a new menu item with the following fields:
      - **Name:** The name of the menu item.
      - **Description:** A text area to describe the menu item.
      - **Price:** The cost of the item.
      - **Image:** An option to upload an image for the menu item.
      - At the bottom, there are buttons to save the entry, save and add another item, or save and continue editing the current item.
        ![admin page](/readme.images/add.menu.png)
    ***
    - This is the Django admin interface's "Select booking to change" page. It shows a list of bookings currently stored in the system.
      ![booking admin page](/readme.images/booking.admin.png)
    ***
    - Admin interface for **Table** management:
      This admin panel allows the site owner to manage the restaurant's table capacities easily. Through this interface, the owner can create and configure tables by specifying their seating capacity.
      ![admin page for add table](/readme.images/admin.add.table.png)
    ***
    - Current tables overview in admin panel:
      This section of the admin panel displays the current list of tables available in the restaurant, ordered by their seating capacity. Each table shows its capacity, allowing the site owner to easily manage and modify the table arrangement. The list contains tables with capacities ranging from 1 to 10 seats, giving flexibility to accommodate different group sizes.
      ![admin current table](/readme.images/admincurrent.1.png)

---

---

## Models

- Booking Model.
- Represents a reservation made by a user for a table.
  - user: Many-to-One → A user can have multiple bookings, but each booking belongs to one user.
  - table: Many-to-One → A table can have multiple bookings, but each booking is for one table.
  - date & time: Stores reservation date and time.
  - guests: Number of guests (1-10), with validation and predefined choices.
  - If a user or table is deleted, related bookings are removed.

---

- Bookings Model
  ![list of field, type and description](/readme.images/model.booking1.png)

---

- Menu Model
  ![list of field, type and description](/readme.images/menu.model.png)

---

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

- Deployment Platforms:
  - All code from Gitpod was pushed to GitHub using the following steps:
    1. git add .
    2. git commit -m "Commit message"
    3. git push
  - Heroku: Cloud-based deployment platform.
    1. Go to Heroku page and login.
    2. Create new app.
    3. App name (east-flavors) and choose Europe for region(If you are in europe).
    4. Create app. Click GitHub, connect to Github.
    5. Go to the settings tab.
       1. Config vars.
       2. Add environment variables.
    6. Go to the deploy tab, and Select github.
    7. Confirm what I want to connect to github.
    8. Now we can search for github repository name. and Scroll down to Manual Deploy and select deploy branch.
- Packages Used:
  - Development Tools:
    - Gitpod: IDE used for coding and file transfer between editor and repository.
    - GitHub: Version control and repository hosting.
    - Balsamiq: Wireframe models for site design.
    - Global css: Styling the text throughout the site.
- Django Documentation:
  - Code Institute: Course help to create the project.
  - Reference for achieving CRUD functionality and associated views.
  - Django-allauth Documentation: Guide for implementing authentication features correctly.

---

## Manual testing

- Manual test for home page.
  ![manual text list](/readme.images/manual.test.first.png)

---

- Manual test for menu page.
  ![manual text list](/readme.images/manual.test.menu1.png)

---

- Manual test for login page.
  ![manual text list](/readme.images/manual.test.login.png)

---

- Manual test for register page
  ![manual text list](/readme.images/manual.test.register.png)

---

- Manual test for booking.

| Test item                           | Test Carried Out                                    | Result                                                 | Pass/Fail |
| ----------------------------------- | --------------------------------------------------- | ------------------------------------------------------ | --------- |
| Select a current or future date     | Choose a valid date                                 | Date is accepted                                       | PASS      |
| Select a past date                  | Choose a date in the past                           | "Date Invalid" notification appears                    | PASS      |
| Select a time within allowed range  | Choose a time between 11:00 AM - 10:00 PM           | Time is accepted                                       | PASS      |
| Select a time outside allowed range | Choose a time before 11:00 AM and 10:00 PM or after | "Time Invalid" notification appears                    | PASS      |
| Select a past time for today        | Choose a past time for the current day              | "Time Invalid" notification appears                    | PASS      |
| Leave date field empty              | Try submitting without selecting a date             | Error message appears                                  | PASS      |
| Leave time field empty              | Try submitting without selecting a time             | Error message appears                                  | PASS      |
| Submit with valid inputs            | Choose a valid date, time, and guest number         | "Booking is successful"message appears                 | PASS      |
| Cancel booking                      | Click on cancel booking                             | "Cancel booking successful"message appears             | PASS      |
| Edit booking                        | Click on the existing booking you wish to edit      | Details for chosen booking appears in the booking page | PASS      |

---

- Automatic Testing
  - Testing Menu app. - Testing is essential to ensure that our application’s features and components work as expected. This suite of tests focuses on verifying the functionality of the Menu model and related views in the application. These tests ensure that: - The data models behave correctly when creating and accessing menu items. - The views render the appropriate templates, load content correctly, and display expected data to users.
    ![auto test](/readme.images/menu.crud.png).

---

- Testing Booking App.
  ![booking app test](/readme.images/booking.crud.png)
  - Test Cases.
    - test_user1_cannot_update_user2_booking.
      - Logs in as User1 and attempts to update User2’s booking.
      - The update should fail, and the booking should remain unchanged.
    - test_user1_cannot_cancel_user2_booking.
      - Logs in as User1 and attempts to cancel User2’s booking.
      - The request should return a 404 error, as User1 has no permission to cancel it.
    - test_user1_cannot_book_for_user2.
      - Logs in as User1 and creates a booking.
      - The booking should be assigned to User1 (not User2), ensuring users can only book for themselves.

---

## Validator testing.

- All pages are went through the URI test and passed
  ![html test](/readme.images/html.valid.png)

---

- Css validate. All CSS files went through a validater test, result; no error found.
  ![css validate](/readme.images/css.valid.png)

---

- Jshint.
- link for js code test: [jshint](https://jshint.com/)
  - Bookings js.
    - Metrics.
    - There are 2 functions in this file.
      Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 11 statements in it, while the median is 5.5.
    - The most complex function has a cyclomatic complexity value of 3 while the median is 2.
  - main js.
    - Metrics.
    - There are 3 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 2 statements in it, while the median is 1.
    - The most complex function has a cyclomatic complexity value of 2 while the median is 1.
    ***
  - Pep8
    - Link for: [test python code](https://pep8ci.herokuapp.com/)
    - All Python code has been thoroughly tested, and the results show **no errors were found.**
  - Lighthouse
    - Lighthouse .This test is been done on my laptop.  
      ![light house](/readme.images/light.house.png)

---

---

## Bugs.

- Duplicate ID Errors:
  - Issue: I received multiple errors for duplicate id attributes in HTML elements (e.g., menu-image, text, title, etc.).
  - Cause: IDs in HTML must be unique within a page. Having duplicate IDs can cause conflicts, especially with JavaScript and styling.
  - Fix: Updated elements to use unique IDs or used class attributes instead of id.
- Image Accessibility Issues:
  - Issue: Some images were missing alt attributes, leading to warnings about accessibility.
  - Fix: Added descriptive alt attributes to all images to ensure better accessibility.
- CSS Validator Errors:
  - Issue: CSS validation produced errors due to incorrect usage of certain properties, like justify-content: baseline.
  - Fix: Updated CSS to use the correct properties (e.g., justify-content: center).
- Test Failures Due to Incorrect String Representation:
  - Issue: One of my tests failed because the ** str** method in my Menu model was returning the wrong string ("Menu object (1)" instead of "Spaghetti").
  - Cause: The ** str** method was incorrectly defined outside the class.
  - Fix: Moved the ** str** method inside the Menu class so it correctly returns the name of the menu item.
- User Could Book a Table in the Past:
  - Issue: Initially, users were able to book tables for times in the past, which was not allowed and created incorrect data in the booking system.
  - Fix: A solution was implemented to prevent users from booking tables in the past by handling timezones and validating booking times:
    - Installed the pytz library for timezone handling.
    - utils.py: Updated to check if the booking time is in the future based on the user's timezone.
    - views.py: Modified to receive the user's timezone from the frontend and validate the booking time.
    - main.js: Added JavaScript to capture the user's timezone.
- unsolved bugs:
  - none.

---

---

## Credits

- I want to thank my mentor, **Luke Buchanan**, for his invaluable support and guidance during this project, and Tutor Assistance.
- Images for the entire project.
  - <https://www.munchery.com/blog/old-meets-new-the-roots-and-current-trends-of-middle-eastern-cooking/>
  - <https://amazingfoodanddrink.com/middle-eastern-foods/>
  - <https://en.wikipedia.org/wiki/Dolma>
  - <https://unsplash.com/s/photos/forest>
  - The address and phone number used in this project are provided with permission from Kurdistan Restaurang <http://kurdistanrestaurang.se/> and are used solely for demonstration purposes.
  - I did look at this site, the layout of the header and footer, which have a slightly similar look and feel.
    <https://east-street-bc0671035c95.herokuapp.com/>.
- Notice
  - At the start of the project, I interpreted the Portfolio 4 Assessment Guide's instruction to 'Avoid double bookings' as preventing users from booking two tables at the same time and date. (That was my understanding). Therefore, the booking system will not allow users to book two tables at the same time and same day unless they are one hour apart. However, upon reviewing the guide again before submitting the project, I realized that 'Avoid double bookings' actually refers to preventing double bookings of the same table, not a user.
