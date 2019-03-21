from appJar import  gui
# app = gui()
# app.addLabel("title", "Hello world")
# app.go()

# create gui and start it
win = gui("Project ASMA")

# code here
win.addLabel("label", "helloWorld")
win.addLabel("label1", "helloWorld")

#gui settings
win.setBg("teal")
win.setFont('13')
win.setLabelBg('label1', 'yellow')
win.setLabelFg('label', 'blue')
win.setSize("1024x600")
win.setResizable(False)


# buttons dont need unique title but need a function name in arg 2
def press(name):
    print(name, "button pressed")


def change_label(name):
    win.setLabel("label1", "Pressed")
# passes the name of the button into press fn


count = 10


def count_fn(name):
    global count
    count -= 1
    win.setLabel("label", "Pressed" + str(count) + " times")
    if count == 0:
        win.stop()
    if count % 2 == 1:
        win.setLabelBg("label", "orange")
    else:
        win.setLabelBg("label", "green")


win.addButton("Press thing this", press)
win.addButton("Change label of label", change_label)
win.addButton("count", count_fn)

win.go()


