from appJar import gui

app=gui()
app.setBg("blue")
app.setGeometry("500x500")
app.setFont(20)
app.addMeter("progress")
app.setMeterFill("progress", "green")
app.setMeter("progress", 50, "winning")
app.setMeterWidth("progress", 200)
app.setMeterHeight("progress", 200)
app.setMeterBg("progress", "black")
app.setMeterFg("progress", "orange")
app.setMeterFill("progress", "yellow")
#app.setBg("blue")
app.go()