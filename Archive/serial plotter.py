import serial
import matplotlib.pyplot as plt
from matplotlib import animation
import csv
import xlwt
from tempfile import TemporaryFile
from datetime import datetime

t = 0
i=0
x=list()
y=list()
y_2=list()
y_3=list()
y_4=list()
y_5=list()
y_6=list()
y_7=list()
time_list= list()
i=0
p = 0
def handle_close(evt):
    global x
    global y
    global y
    global y_2
    global y_3
    global y_4
    global y_5
    global y_6
    global y_7
    global time_list
    book = xlwt.Workbook()
    
    sheet1 = book.add_sheet('sheet1')
    sheet1.write(1,2,'Wind Speed')
    sheet1.write(1,3,'Rain')
    sheet1.write(1,4,'Temperature')
    sheet1.write(1,5,'Humidity')
    sheet1.write(1,6,'Temperature 2')
    sheet1.write(1,7,'Pressure')
    sheet1.write(1,8,'Soil Moisture')
    sheet1.write(1,9,'Date_Time')
    
    for i,e in enumerate(x):
        sheet1.write(i+2,1,e)
        
    for i,e in enumerate(y):
        sheet1.write(i+2,2,e)

    for i,e in enumerate(y_2):
        sheet1.write(i+2,3,e)
        
    for i,e in enumerate(y_3):
        sheet1.write(i+2,4,e)
    
    for i,e in enumerate(y_4):
        sheet1.write(i+2,5,e)
        
    for i,e in enumerate(y_5):
        sheet1.write(i+2,6,e)
        
    for i,e in enumerate(y_6):
        sheet1.write(i+2,7,e)
        
    for i,e in enumerate(time_list):
        sheet1.write(i+2,8,e)
    
    name = "Weather_data.xls"
    book.save(name)
    book.save(TemporaryFile())
    ser.close()
# Find photon serial port and type in below
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
ser = serial.Serial('COM25',9600)
ser.close()
ser.open()
fig = plt.figure(figsize=(10,6))
fig.canvas.mpl_connect('close_event',handle_close)
ax1 = fig.add_subplot(3,2,1)
ax1.set_ylabel('Wind Speed')
ax2 = fig.add_subplot(3,2,2)
ax2.set_ylabel('Rain')
ax3 = fig.add_subplot(3,2,3)
ax3.set_ylabel('Temperature')
ax4 = fig.add_subplot(3,2,4)
ax4.set_ylabel('Humidity')
ax5 = fig.add_subplot(3,2,5)
ax5.set_ylabel('Temperature 2')
ax6 = fig.add_subplot(3,2,6)
ax6.set_ylabel('Pressure')
plt.subplots_adjust(wspace = 0.6, hspace = 0.3)

def animate(i):
    global p
    if (p != 0):
        i = i + 1
    data = ser.readline()
    data_store = str(data).split(":")
    print(data_store)
    time_list.append(str(datetime.now()))
    x.append(i)
    y.append(float(data_store[1]))
    y_2.append(float(data_store[3]))
    y_3.append(float(data_store[5]))
    y_4.append(float(data_store[7]))
    y_5.append(float(data_store[9]))
    y_6.append(float(data_store[11]))
    ax1.clear
    ax1.plot(x,y)
    ax2.plot(x,y_2)
    ax3.plot(x,y_3)
    ax4.plot(x,y_4)
    ax5.plot(x,y_5)
    ax6.plot(x,y_6)
    p = p + 1
    
ani = animation.FuncAnimation(fig, animate, interval=20000)
plt.show()