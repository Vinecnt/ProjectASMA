from appJar import gui

app=gui("Grid Demo", "400x400")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)


app.addLabel("Menu", "Menu", 0, 0, 1, 1)
app.addLabel("Graphs", "Graphs", 0, 1, 3, 1)
app.addLabel("Motivation", "Motivation", 1, 0, 2, 1)
app.addLabel("Other", "Other", 1, 3, 1, 1)

app.setLabelBg("Menu", "red")
app.setLabelBg("Graphs", "blue")
app.setLabelBg("Motivation", "green")
app.setLabelBg("Other", "yellow")



app.go()
