#### Admin

- As a user i want to be able to add products easily.
- As a user i want to be able to manage orders in a simple and easy manner.
- As a user i want to be able to upload to my portfolio easily.

#### Developer

- As a user i want to ensure the user can't break the flow of the site with correct defensive design choices.
- As a user i want to ensure an authenticated user can access all required information correctly.
- As a user i want to include options for the admin to quickly edit the site.

### Wireframes
- [Splash Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-desktop-splash.png)
- [Portfolio Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-desktop-portfolio.png)
- [Store Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-desktop-store.png)

#### Tablet
- [Splash Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-tablet-splash.png)
- [Portfolio Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-desktop-portfolio.png)
- [Store Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-tablet-store.png)

#### Mobile
- [Splash Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-mobile-splash.png)
- [Portfolio Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-mobile-portfolio.png)
- [Store Desktop](https://github.com/WisamTa/FragileArt/blob/main/wireframes/fa-mobile-store.png)

### Data Storage

#### User Table

| Title            | Key In Database | Form Validation | Data Type |
|------------------|-----------------|-----------------|-----------|
| Account id       | _id             | No Validation   | Primary Key  |
| First Name       | first_name      | max length 20 | CharField |
| Last Name        | last_name       | hashed min length 8 | CharField |
| E-mail Address   | email           | Must contain @ & .com etc | Email |
| Street Address   | default_street_address1 | max length 128 | CharField  |
| Street Address 2 | default_street_address2 | max length 128 | CharField  |
| City Or Town     | default_city_town     | max length 128 | CharField  |
| County/State     | default_county_state      | max length 64 | CharField  |
| Postal Code      | default_postcode_zi      | max length 12 | CharField  |
| Contact Number   | default_telephone_number | Number max length 20 | CharField  |
| Country          | country         | pycountry select  | Option    |

#### Products Table

As the brief for the project requires a portfolio and seperate store one table is created to ensure data isn't stored twice and can be
user by both components

| Title              | Key In Database | Form Validation | Data Type |
|--------------------|-----------------|-----------------|-----------|
| Product Id         | _id             | No Validation   | Primary Key  |
| Product Name       | name            | max length 254 | CharField |
| Product Category   | category        | max length 100 | CharField |
| Price              | price           | Max Digits 6 Decimal Places 2 | DecimalField  |
| Client             | client          | No validation | CharField |
| description        | description     | No validation | CharField |
| tools              | colour          | No validation | CharField |
| is sold            | is_sold         | Default True | BooleanField |
| sale_type          | sale_type       | max length 20| DecimalField |
| image              | image           | Null True Blank True | ImageField |

#### Orders Table

|     Title    | Key In Database |    Form Validation    |  Data Type  |
|:------------:|:---------------:|:---------------------:|:-----------:|
| Order Number | order_number    | No Validation         | Primary Key |
| User Profile | user_profile    | text                  | Foreign Key |
| First Name   | first_name      | max length 100 | CharField   |
| Last Name    | last name       | max length 100 | CharField   |
| email        | email           | max length 100 | CharField   |
| telephone Number | telephone_number | max length 20 | CharField |
| street address 1| street_address1 | max length 100 | CharField |
| street address 2 | street_address2 | max length 100 | CharField |
| City Town    | city_town       | max length 100 | CharField   |
| County/State | county_state    | max length 100 | CharField   |
| Postcode Zip | postcode_zip    | max length 8   | CharField   |
| Country      | country         | country select        | Option      |
| Order Date   | order_date      | datetime.date.today   | DateField   |
| Total Order   | total_order    | max digits 10   | DecimalField   |
| Delivery Charge | delivery_charge | max digits 5   | DecimalField   |
| Grand total  | grand_total     | max digits 10 | DecimalField    |

#### Clients Table

| Title         | Key in Database | Form Validation | Data Type  |
|---------------|-----------------|-----------------|------------|
| name          | name            | max length 128  | CharField  |
| Friendly name | friendly_name   | max length 254  | CharField  |
| business type | Business Type   | max length 50   | CharField  |
| Description   | description     | None            | TextField  |
| image         | image           | None            | ImageField |

## Technology Used

### Languages

- HTML
- CSS
- Javascript
- [Python](https://www.python.org/)

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Libraries

- [Jquery](https://jquery.com/)
- [Sweet Alert](https://sweetalert2.github.io/)
- [Stripe Payments](https://stripe.com/)
- [PopperJS](https://popper.js.org/)

### Tools

- [AWS](https://aws.amazon.com/s3/)
- [Heroku](https://www.heroku.com)
- [Git](https://git-scm.com/)
- [Postgres](https://www.postgresql.org/)

## Testing

No automated testing has been used on this project, i have opted to do all testing manually and through numerous user experiences.

- <strong>Implementation</strong> 🏭:
When i had set up the products fixtures and loaded into the database i could then view all saleable items in the store, i wanted to ensure all products loaded as expected and that item information was visable when selected.

- <strong>Test</strong> 🧪:
To test this, I went through each item and loaded the products information page, then looked at changing the url to ensure each item was loading correctly

- <strong>Result</strong> 🏆:
All products loaded as expected to the main store page, some items were missing their images but they were still selectable and loaded their page correctly. When amending the url all items again loaded as expected however if i tried to access an item id that didn't exist i was presented with a 404 page.

- <strong>Verdict</strong> ✅:
This test passed in it's basic form, amendments are required to the fixtures to ensure all the items images load correctly, also as the 404 page is the generic template provided with Django creating a custom page to handle these errors is desireable.

---

- <strong>Implementation</strong> 🏭:
As with the store the portfolio page is populated from all items even if they aren't saleable. i need to ensure these load correctly to their specific pages and the overlays work correctly.

- <strong>Test</strong> 🧪:
To test this, I went through each item and loaded the portfolio item information page, then looked at changing the url to ensure each item was loading correctly

- <strong>Result</strong> 🏆:
All portfolio items again populated the main page correctly, some with missing images and when clicked presented their specific pages with information displaying correctly.

- <strong>Verdict</strong> ✅:
This test was deemed to be a pass, some minor edits are needed to the fixtures to ensure when the items are loaded out of development branches they are displaying as expected.

---

- <strong>Implementation</strong> 🏭:
As a user can purchase items without signing in, i wanted to ensure that an order can be completed from start to finish.

- <strong>Test</strong> 🧪:
To test this i will select items at random and add them to the basket and proceed through checkout.

- <strong>Result</strong> 🏆:
Items were added to the basket correctly and the totals calculated as expected, going through the checkout process i was able to complete the order with stripes debug card ref and the order was confirmed and added to the db correctly.

- <strong>Verdict</strong> ✅:
This test completed as expected without bugs.

---

- <strong>Implementation</strong> 🏭:
With a logged in user, i want to make sure the user can view previous orders through the users account page.

- <strong>Test</strong> 🧪:
To test this i created a new user and proceeded to add items to the basket and complete the checkout process.

- <strong>Result</strong> 🏆:
As expected the checkout process completed and upon checking the users account page i could see the order details. upon completing multiple orders i was able to view these in a list as designed

- <strong>Verdict</strong> ✅:
This test completed as expected without bugs, it did flag a minor style change needed to the account page but information was present.

---

- <strong>Implementation</strong> 🏭:
To ensure the user can navigate the site as expected i need to test each view and link to ensure the user isn't 'lost' within the page.

- <strong>Test</strong> 🧪:
This test will be carried out by systematically navigating to each page from the previous and all links are clicked until all checked.

- <strong>Result</strong> 🏆:
Each page and link was checked and each provided a positive result, at no point was the user sent to an unexpected destination.

- <strong>Verdict</strong> ✅:
This test passed and no amendments were required.

---

- <strong>Implementation</strong> 🏭:
To test the responsiveness of the site, the page was loaded on local mobile devices to check design choices

- <strong>Test</strong> 🧪:
This test was carried out by loading the site and navigating to each page and adding and completing an order with more than one item

- <strong>Result</strong> 🏆:
Each page loaded and displayed correctly, an issue was found with the basket which caused the table to overflow the edge of the page.

- <strong>Verdict</strong> ✅:
This test was classed as a fail and upon rereading the code a redesign of the basket was required to ensure mobile users were presented with the correct information that could be easily read.