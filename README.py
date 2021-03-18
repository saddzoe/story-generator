# story-generator
# This is code for generating a random story given the following lines and information below

import random

when = ['A long time ago', 'Today', 'Last week', 'Just yesterday', 'A couple weeks ago', 'On May 4th, 3034', 'Many ions ago', 'On my birthday', 'Centuries ago', 'A long time ago in a galaxy far, far away....']
name = ['Darth Vader', 'Undertaker', 'John Cena', 'Ash Ketchum', 'Lelouch', 'Light', 'Goku', 'Eren', 'Armin', 'Mikasa', 'The Rock', 'Randy Orton', 'Soulja Boy', 'Lil B', 'Pooh Shiesty', 'Lil Smurk', 'Da Baby', 'Rick and Morty', 'Davido', 'Wizkid']
who = ['a dinosaur', 'a pig', 'a judge', 'a lawywer', 'a king', 'her boyfrined', 'his girlfriend', 'the queen', 'the prince']
residence = ['Hogwarts', 'Ghana', 'Nigeria', 'Brazil', 'South Africa', 'London', 'Canada', 'Pluto', 'Saturn', 'Houston', 'India']
went = ['to school', 'wedding', 'moon', 'space', 'movies', 'hospital', 'college', 'vet', 'army', 'play']
happened = ['saw shooting stars', 'saw The Weeknd', 'went shopping', 'saw Michael Jackson', 'listened to House of Ballons', 'fought the Big Show', 'found King Booker', 'worked out to Ariana Grande', 'went on a spaceship to see bettleguese', 'saw Anubus', 'meet Cleopatra', 'worked out with Barney', 'fought along side the X men', 'saw the Avengers and Thanos battle for the world', 'fought along side Harry, Hermoine, and Ron', 'teamed up with Voldermont']

print(random.choice(when) + ', ' + random.choice(who) + ' that visited ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
