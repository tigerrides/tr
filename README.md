# tigerride™
## what is tigerride?
Tigerride is a student-run application created to streamline the process of students sharing transportation services to and from the Princeton University campus. Sharing such services allows users to save money, travel more safely, as well as take a step towards a greener environment. Users fill out a simple form to find other users to share rides with, and have the flexibility of requesting to join and leave rides at any time.

#### You can visit our site [here](https://tigerride.herokuapp.com).
## user guide
Note: All users of tigerride must be Princeton students or faculty members with a valid netID and password because our website utilizes a Central Authentication Service system to make the app safe and reliable for all users.
### logging in
1. Navigate to http://tigerride.herokuapp.com/.
2. Click the “login” button at the bottom, which takes the user to the Princeton University Central Authentication Service authentication page.
3. Fill out input fields for NetID and Password, click “LOGIN” and proceed with preferred method of DUO security authentication.
### creating a profile
1. The first-time user must create a profile in order to create or view rides.
2. Users are presented with two options: creating a new profile from scratch, or importing their information from Tigerbook.
    - Starting from scratch:
      - Fill out fields for preferred first name and last name.
      - Input phone number.
      - Upload a profile photo.
    - Using Tigerbook information:
      - Clicking the button automatically imports the user’s name, netID, and photo.
3. Users can update their profile information anytime by navigating to their profile page by selecting the “profile” option on the menu bar and clicking the “edit” button.
### finding rideshare buddies
1. Once the user is logs in, they are redirected to a welcome page with presented with two buttons. Click on “plan a trip.”
2. Under “origin,” select desired origin from the dropdown menu. Options are EWR, PHL, JFK airports and Princeton University.
3. Under “destination,” Select desired destination from the dropdown menu. Options are EWR, PHL, JFK airports and Princeton University.
4. Under “date,” input the day, month, and year of departure. Clicking the small arrow on the right opens up a calendar for easy selection.
5.  Under “time frame,” there are two fields. In the first field, enter the earliest possible time of departure. In the second field (after “~”), enter the latest possible time of departure
    - Tip: Entering a flexible time frame is more likely to return more options.
6. Under “notes,” enter any information that may be useful for potential ride sharers to know. Some things to consider:
    - desired rideshare option (ex. Standard Lyft, Lyft XL, Lyft Lux, Uber X)
    - flight number (be cautious!)
    - terminal details
    - amount of luggage
    - preferred seating arrangement (ex. next to the driver, in the back)
    - desired number of rideshare partners
    - your airline is known to be frequently delayed
7. Click “submit.”
8. If user is the first to submit a ride in their desired time frame, they are redirected to a page that displays the following message: “Your ride has been created and we will notify you via your Princeton email when other students join your group!”
    - User will receive e-mail notifications of trip details and group members when others join their group. 
9. If another user has joined the ride immediately after the current user has submitted his/her ride, the following message will be displayed: “A rider beat you to it and has already joined your ride!” The user can then see this ride group by clicking on “my rides,” which navigates to his/her ride history.
10. Otherwise, user is redirected to page displaying all open rides that match their search. User can join a ride. This notifies all members in the group via their Princeton e-mail of the trip details. 
11. If the user does not join someone else’s group, tigerride automatically creates a ride with their own preferences for others to join in the future.
### viewing your ride history
1. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar), click “see all rides.”
2. Under “current rides,” you can view all your current open rides. Under “past rides,” you can see all your completed rides. 
### re-searching for rideshare buddies
1. Note: Re-searching for ride share buddies is only possible if you have not yet joined a group.
2. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar), click “see all rides.”
3. Under “current rides,” locate the ride you would like to find rideshare buddies for and click “see more.” You will be taken to a page that shows all the details of the ride with the option to “continue search.” 
4. If there are no current rides that match their ride details, the student will be redirected to a page that displays the following message: “Your ride has been created and we will notify you via your Princeton email when other students join your group!”
    - User will receive e-mail notifications when others request to join their ride. 
5. Otherwise, user is redirected to page displaying all open rides that match their search. User can join a ride. This notifies all members in the group via their Princeton e-mail of the trip details. 
### deleting a ride
1. Note: Deleting a ride is only possible if you have not joined a group and are the initial creator of the ride, and completely removes the ride from the tigerride database.
2. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar), click “see all rides.”
3. Under “current rides,” locate the ride you wish to delete and click “see more.” You will be taken to a page that shows all the details of the ride with the option to click “delete ride.” 
4. You will be taken to a confirmation page that asks “are you sure you want to delete this ride?” Click “delete!” Note: this action cannot be reversed.
5. The ride is deleted from your ride history as well as the database.
### completing a ride
1. Note: Completing a ride is only possible if you have joined a group.
2. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar), click “see all rides.”
3. Under “current rides,” locate the ride you wish to complete and click “see more.” You will be taken to a page that shows all the details of the ride with the option to click “complete ride.”
4. You will be taken to a confirmation page that asks “are you sure you want to complete this ride?” Click “complete!” Note: this action cannot be reversed.
5. The ride is now moved down to the “past rides” section and other users can no longer request to join your ride.
### leaving a ride
1. Note: Leaving a ride is only possible if you have joined a group.
2. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar), click “see all rides.”
3. Under “current rides,” locate the ride you wish to leave and click “see more.” You will be taken to a page that shows all the details of the ride with the option to click “leave ride.”
4. You will be taken to a confirmation page that asks “are you sure you want to leave this ride?” Click “leave!” Note: this action cannot be reversed.
5. You are no longer a part of this group, but your individual ride will still be visible under “current rides” in your ride history.
### rating a rider
1. Note: You can only rate a rider if you have completed a ride with him/her.
2. From the home page (the first page user sees after logging in, can be accessed by clicking “home” in menu bar or the “tigerride” logo), click “see all rides.”
3. Click on any rider’s name in your past rides. This will take you to their user profile, where you will see an option to click “rate.”
4. You will be taken to a page that will allow you to rate them on a scale of 1 to 5 (1 being the worst and 5 being the best).
5. Upon success, you will be taken to a page that allows you to navigate to your ride history once again by clicking the button “see my rides.”
### user profiles
1. You can view a user profile at any point where their name and a button to their profile shows up. If they do not have a user profile, you will be taken to a page with a link to their TigerBook page.
2. Each user profile will always display the first name, last name, rating, netid, and number of trips taken. However, when you are currently in a ride-share group with other users, their profiles will also display their phone numbers for ease of contacting them. You are also able to view the phone numbers of each user you have a past ride with. 
3. As explained earlier, you are also able to rate a user in their profile (but this feature is only available if you have completed a ride with him/her).
### addressing questions, concerns, and suggestions
1. Click the “contact” button on the menu bar.
2. Email any of the four developers listed on the page with your question, concern, or suggestion.
### logging out
1. Click the “logout” button on the top right corner of any page.
## contact us
Email us at princetontigerrides@gmail.com with any questions, comments, or concerns!

