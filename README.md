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
