# SigmoidBoost
Python function for creating a sigmoid curve boost percentage
This function will generate a curve with a simple sloped section from 0 to a specified day and from a specified day to max. Without this sloped section the function is asymptotic and will take forever to ramp up/down.
We can manipulate several things within user parameters file to manipulate which slice of the sigmoid we take, which will change the vertical endpoints of the sigmoid curve affecting the steepness of the sloped sections.
We can also change the days of initial/final linear sloped sections to "squish"the sigmoid along the X axis. The more squished the sigmoid the more drawn out the linear section is and with a large sigmoid slice it will create a VERY aggressive slope upwards
Highly Recommend changing the variables around in a mirrored fashion until you get a grasp for what they affect(IE: IL & FL equal, LS & US are equal(with LS negative)
