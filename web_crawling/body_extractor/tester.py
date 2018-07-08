import format

# s = "\n \n hi i am sam. \n\n\n yo";
# print (s)
# print (format.remove_newlines(s))

# str = "Pune: An 18-year-old man was crushed in an accident near the Khandala tunnel on the Pune-Mumbai Expressway on Sunday evening. According to the police, Sayyed Sadaq Chandpasha Sayyed (18) of Karnataka worked as a cleaner on a truck headed for Mumbai from Pune. Shortly after crossing the tunnel, the truck\u2019s fan-belt snapped, forcing the driver to pull over. Sayed got out and was inspecting the truck from the front, when another truck, also headed for Mumbai, crashed into the stationary truck. Sayyed was found under the truck\u2019s front tyre.This was the third fatal accident this month on the expressway. On April 19, three people including a nine-year-old girl died after their car hit a tree on the expressway. Six others suffered injuries and were admitted to a local hospital.On April 16, the cleaner of a tempo was killed instantly while its driver sustained serious injuries when the vehicle rammed into a stationary truck on the expressway."

str = "A 22 year-old TV actress was killed and two injured in a car accident after the vehicle hit the centre median on the Chennai-Bengaluru National Highway 48 near Natrampallai during the early hours of Friday.The deceased has been identified as Rekha Sindhu, daughter of Paulraj and resident of Bengaluru. She was travelling along with her friend Rahini, while Jayakumar was behind the wheels of the car. Sindhu acted in an ad film (Ad film on Chennai Amirtha Institute), said the Natrampalli Police.They were heading towards Bengaluru from Chennai. The accident took place at about 1.30 am on Friday when the car was passing through Natrampalli.    According to police, Jayakumar fell asleep and the car hit the centre median and overturned. Sindhu who was sitting in the front seat died on the spot, while Jayakumar and Rahini sustained serious injuries and shifted to the government hospital in the vicinity. Later, they were referred to the hospital in Vellore.  The police shifted the body of Sindhu to the GH for post-mortem. A case has been registered in this regard.Read this story in: , , "

loc, art = format.reporting_location(str)

print (loc)
print (art)

