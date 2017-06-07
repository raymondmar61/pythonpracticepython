#Practice Python 036 Birthday Plots

#use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.
#If you are looking for a plotting library in Python, you have two main options: matplotlib and bokeh. Today I want to discuss bokeh, because I think it will become more popular in years to come. Many Python developers (and especially data scientists and researchers) will tell you that the most commonly used plotting library in Python is matplotlib.  There is no one “best” plotting library you should use whichever one feels and looks better for you. But for the rest of this post, I’ll talk about how to use bokeh to make a basic plot.

# need to import at least 3 things to make your bokeh plots work
from bokeh.plotting import figure, show, output_file
# we specify an HTML file where the output will go
#must be connected to the internet
output_file("plot.html")
# load our x and y data
x = [10, 20, 30]
y = [4, 5, 6]
# create a figure
p = figure()
# create a histogram
p.vbar(x=x, top=y, width=0.5)
# render (show) the plot
show(p)
#when you run a piece of bokeh code, it outputs the result into an HTML file that you can then save and display in a web browser on it’s own. After you run this segment on top, it will automatically open a web browser and show you a plot.

#in the exercise, we are dealing with months, which is called a “categorical” variable (i.e. it belongs to a category, and is not continuous). To make sure bokeh draws the axis correctly, you need to specify a special call to figure() to pass an x_range, like so:
from bokeh.plotting import figure, show, output_file
output_file("plot2.html")
x_categories = ["a", "b", "c", "d", "e"]
x = ["a", "d", "e"]
y = [4, 5, 6]
p2 = figure(x_range=x_categories)
p2.vbar(x=x, top=y, width=0.5)
show(p2)
#There are also extra commands and arguments you can pass to bokeh to display an title for the plot, for each of the axis, for the color of the bars, and so on.
#If you want to dive deep into that documentation, check out these resources (on the pdf file).

from bokeh.plotting import figure, show, output_file
from collections import Counter
output_file("plotbirthdays.html")
# x_categories3 = ["January","February","March","April","May","June","July","August","September","October","November","December"]
x_categories3 = ["April","August","December","February","January","July","June","March","May","November","October","September"] #months sorted alphabetically
import json
import datetime
with open("birthdays.json","r") as r:
	info = json.load(r)
monthscount = []
for birthday in info:
	b = info[birthday]
	datee = datetime.datetime.strptime(b, "%m/%d/%Y")	
	monthscount.append(datee.strftime("%B"))
	monthscount.sort()
m = Counter(monthscount)
print(m) #counter dictionary
print(dict(m)) #convert counter dictionary to regular dictionary
xlist = [] #list for the months for x-axis
ylist = [] #list for the months count for y-axis
for eachm in sorted(m):	#sort dictionary separting key and value to two lists
	xlist.append(eachm) #append months to xlist
	ylist.append(m[eachm]) #append months count to ylist
print(xlist)
print(ylist)
# x = [xlist]
# y = [ylist]
x = ['August', 'February', 'January', 'July', 'March', 'October']
y = [1, 1, 1, 2, 1, 1]
# for some reason, bokeh doesn't want to plot the xlist and ylist lists directly from the for loop.  bokeh does want to plot the xlist and ylist explicitly.  If I comment out xlist and ylist explicitly and uncomment out [xlist] and [ylist], then bokeh doesn't plot.
p3 = figure(x_range=x_categories3)
p3.vbar(x=x, top=y, width=0.5)
show(p3)