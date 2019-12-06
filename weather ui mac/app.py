from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QComboBox, QMainWindow,QWidget, QLabel, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDate, QDateTime 
from scipy.signal import savgol_filter
import PyQt5
from weather_ui_2 import Ui_MainWindow

import os
import time
import sys
import gspread
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


res_x = 781
res_y = 521



class mywindow(QtWidgets.QMainWindow):
    
    def activate(self,index):
        #ts = time.time()
        
        res_x = (self.ui.pic_label.size()).width()
        res_y = (self.ui.pic_label.size()).height()
        if plt:
            plt.clf()
            
        if index == 0:
            temp_date_list = []
            temp_list = []
            for data in self.temp[1:]:
                temp_list.append(float(data))
            temp_date_list = self.date_list_creator(self.date,temp_date_list)
            temp_folder = list(zip(temp_date_list,temp_list))
            self.date_check(temp_folder)
            new_temp = []
            new_date = []
            for data in self.index_list:
                new_date.append(temp_date_list[data])
                new_temp.append(temp_list[data])
            plt.plot_date(new_date,new_temp,'-o', ms=2)
            self.set_axis("Temperature", "Time", "Temperature (F)")
            self.x_axis_format()
            #self.current_pic = plt
            plt.savefig('temp.png', dpi=self.sel_dpi)
            temp_map = QPixmap('temp.png')
            #fin_temp_pixmap = temp_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(temp_map)
            self.no_data_disp(new_temp)
            #self.current_image = temp_map
            #print("Duration: {} sec".format(time.time() - ts))
            #print(self.current_pic)
            
        if index == 1:
            
            wind_list = []
            for data in self.wind[1:]:
                wind_list.append(float(data))
            wind_date_list = []
            wind_date_list = self.date_list_creator(self.date,wind_date_list)
            temp_folder = list(zip(wind_date_list,wind_list))
            self.date_check(temp_folder)
            new_wind = []
            new_date = []
            for data in self.index_list:
                new_date.append(wind_date_list[data])
                new_wind.append(wind_list[data])
            plt.plot_date(new_date,new_wind, ms=2)
            self.set_axis("Wind Speed", "Time", "Wind Speed (MPH)")
            self.x_axis_format()
            #self.current_pic = plt
            plt.savefig('wind.png', dpi=self.sel_dpi)
            wind_map = QPixmap('wind.png')
            #fin_wind_pixmap = wind_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(wind_map)
            self.no_data_disp(new_wind)
            #self.current_image = temp_map
            
        if index == 2:
            
            sm_list = []
            for data in self.soil_moisture[1:]:
                sm_list.append(float(data))
            sm_date_list = []
            sm_date_list = self.date_list_creator(self.date,sm_date_list)
            temp_folder = list(zip(sm_date_list,sm_list))
            self.date_check(temp_folder)
            new_sm = []
            new_date = []
            for data in self.index_list:
                new_date.append(sm_date_list[data])
                new_sm.append(sm_list[data])
            plt.plot_date(new_date,new_sm,'-o', ms=2)
            self.set_axis("Soil Moisture", "Time", "Soil Moisture")
            self.x_axis_format()
            
            plt.savefig("sm.png", dpi=self.sel_dpi)
            sm_map = QPixmap("sm.png")
            #fin_sm_pixmap = sm_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(sm_map)
            self.no_data_disp(new_sm)
            
        if index == 3:
            st_list = []
            for data in self.soil_temp[1:]:
                st_list.append(float(data))
            soil_temp_list = []
            soil_temp_list = self.date_list_creator(self.date,soil_temp_list)
            temp_folder = list(zip(soil_temp_list,st_list))
            self.date_check(temp_folder)
            new_soil_temp = []
            new_date = []
            for data in self.index_list:
                new_date.append(soil_temp_list[data])
                new_soil_temp.append(st_list[data])
            plt.plot_date(new_date,new_soil_temp,'-o', ms=2)
            self.set_axis("Soil Temperature", "Time", "Soil Temperature (f)")
            self.x_axis_format()
            plt.savefig("soil_temp.png", dpi=self.sel_dpi)
            soil_temp_map = QPixmap("soil_temp.png")
            #fin_soil_temp_map = soil_temp_map.scaled(res_x,res_y)
            self.ui.pic_label.setPixmap(soil_temp_map)
            self.no_data_disp(new_soil_temp)
            
        if index == 4:
            
            h_list = []
            for data in self.humidity[1:]:
                h_list.append(float(data))
            humidity_list = []
            humidity_list = self.date_list_creator(self.date,humidity_list)
            temp_folder = list(zip(humidity_list,h_list))
            self.date_check(temp_folder)
            new_humid = []
            new_date = []
            for data in self.index_list:
                new_date.append(humidity_list[data])
                new_humid.append(h_list[data])
            plt.plot_date(new_date,new_humid,'-o', ms=2)
            self.set_axis("Humidity", "Time", "Humidity")
            self.x_axis_format()
            plt.savefig("humidity.png", dpi=self.sel_dpi)
            humidity_map = QPixmap("humidity.png")
            #fin_humidity_map = humidity_map.scaled(res_x,res_y)
            self.ui.pic_label.setPixmap(humidity_map)
            self.no_data_disp(new_humid)
            
        if index == 5:
            p_list = []
            for data in self.pressure[1:]:
                p_list.append(float(data))
            pr_date_list = []
            pr_date_list = self.date_list_creator(self.date,pr_date_list)
            temp_folder = list(zip(pr_date_list,p_list))
            self.date_check(temp_folder)
            new_pr = []
            new_date = []
            for data in self.index_list:
                new_date.append(pr_date_list[data])
                new_pr.append(p_list[data])
            plt.plot_date(new_date,new_pr,'-o', ms=2)
            self.set_axis("Pressure", "Time", "Pressure(pa)")
            self.x_axis_format()
            plt.savefig('pressure.png', dpi=self.sel_dpi)
            pr_map = QPixmap('pressure.png')
            #fin_pr_pixmap = pr_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(pr_map)
            self.no_data_disp(new_pr)
            
        if index == 6:
            v_list = []
            for data in self.voltage[1:]:
                v_list.append(float(data))
            volt_date_list = []
            volt_date_list = self.date_list_creator(self.date,volt_date_list)
            temp_folder = list(zip(volt_date_list,v_list))
            self.date_check(temp_folder)
            new_volt = []
            new_date = []
            for data in self.index_list:
                new_date.append(volt_date_list[data])
                new_volt.append(v_list[data])
            if len(new_volt) > 41:
                sg = savgol_filter(new_volt, 41, 2)
                plt.plot_date(new_date,sg,'-')
            else:
                plt.plot_date(new_date,new_volt,'-')
            self.set_axis("Voltage", "Time", "Voltage(v)")
            self.x_axis_format()
            plt.savefig('voltage.png', dpi=self.sel_dpi)
            volt_map = QPixmap('voltage.png')
            #fin_volt_pixmap = volt_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(volt_map)
            self.no_data_disp(new_volt)
            
        if index == 7:
            d_list = []
            for data in self.wind_dir[1:]:
                d_list.append(float(data))
            dir_date_list = []
            dir_date_list = self.date_list_creator(self.date,dir_date_list)
            temp_folder = list(zip(dir_date_list,d_list))
            self.date_check(temp_folder)
            new_dir = []
            new_date = []
            for data in self.index_list:
                new_date.append(dir_date_list[data])
                new_dir.append(d_list[data])
            #plt.plot_date(new_date,new_volt,'-')
            #self.set_axis("Voltage", "Time", "Voltage(v)")
            #self.x_axis_format()
            num_time = []
            t = 0
            for time in new_date:
                t += 1
                num_time.append(t)
            check_dir = []
            fin_dir = []
            p = 0
            for data in new_dir: 
                temp_dir = self.direction_finder(data)
                if temp_dir!= "inval":
                    fin_dir.append(temp_dir)
                    check_dir.append(p)
                p += 1
            time_dir = []
            for x in check_dir:
                time_dir.append(new_date[x])
            plt.plot_date(time_dir,fin_dir)
            #plt.polar(fin_dir,num_time, 'ro')
            plt.savefig('dir.png', dpi=self.sel_dpi)
            dir_map = QPixmap('dir.png')
            #fin_dir_pixmap = dir_map.scaled(res_x, res_y)
            self.ui.pic_label.setPixmap(dir_map)
            self.no_data_disp(new_dir)
            
    def direction_finder(self,direction):
        switcher = { 
        0: "N", 
        1: "NE", 
        2: "E",
        3: "SE",
        4: "S",
        5: "SW",
        6: "W",
        7: "NW",
        }  
        return switcher.get(direction, "inval") 
            
    def x_axis_format(self):
        if self.time_bool: 
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        if not self.time_bool:
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H'))
            plt.xticks(rotation=45)
            plt.gcf().subplots_adjust(bottom=0.25)
        self.current_pic = plt
            #plt.tight_layout()
                
    def date_check(self, list_1):
        self.index_list = []
        i = 0
        if self.time_bool:
            for data in list_1:
                self.index_list.append(i)
                i += 1
        if not self.time_bool:
            for data in list_1:
                tem_date = matplotlib.dates.num2date(data[0])
                if self.start_date <= tem_date <= self.end_date:
                    self.index_list.append(i)
                i += 1

    def set_axis(self,title_text, x_text, y_text):
            plt.title('{}'.format(title_text))
            plt.xlabel('{}'.format(x_text))
            plt.ylabel('{}'.format(y_text))
            
    def no_data_disp(self,data):
        if not data:
            self.ui.pic_label.setPixmap(self.no_info)
    
    def date_list_creator(self,date_raw,date_list):
        for day in date_raw[1:]:
            time = datetime.datetime.strptime(day,'%Y-%m-%d %H:%M:%S')
            date_list.append(matplotlib.dates.date2num(time))
        return date_list
                
    def print_cal(self):
        self.date_hold = self.ui.calendarWidget.selectedDate()
    
    def __init__(self):
        super(mywindow,self).__init__()
        self.time_bool = 0
        self.current_pic = 0
        self.sel_dpi = 200
        #self.ui = uic.loadUi("app_data\\weather_ui_2.ui")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.show()
        pixmap = QPixmap('MAC-Decal-MASTER.png')
        self.no_info = QPixmap('no data.png')
        self.waiting = QPixmap('loading.png')
        self.company_icon = QPixmap('MAC-Round-Logo.png')
        self.ui.MAC_LOGO.setPixmap(self.company_icon)
        self.ui.pic_label.setPixmap(pixmap)
        self.ui.sel_combo.activated.connect(self.change_param)#(self.activate)
        self.ui.dev_combo.activated.connect(self.dev_select)
        self.ui.Save_Image.triggered.connect(self.save_button)
        self.ui.action200_dpi.triggered.connect(self.action200)
        self.ui.action300_dpi.triggered.connect(self.action300)
        self.ui.action400_dpi.triggered.connect(self.action400)
        self.ui.action600_dpi.triggered.connect(self.action600)
        self.ui.refreshbutton.clicked.connect(self.refresh_data)#(self.refresh_data)
        self.date_hold = datetime.datetime.now()
        self.start_date = self.ui.date_start.date()
        self.end_date = self.ui.date_end.date()
        #self.download_data()
        #print(self.ui.date_start.date().toPyDate())
        self.ui.date_start.dateChanged.connect(self.calc_date_range)
        self.ui.date_end.dateChanged.connect(self.calc_date_range)
        self.index_stored = 0
        self.change_bool = 1
        self.ui.date_start.setDate(QDate.currentDate())
        self.ui.date_end.setDate(QDate.currentDate())
        self.ui.current_dpi.setText("current res: {}".format(self.sel_dpi))
        self.device_selected = self.ui.dev_combo.currentText()
        self.dev_listing = open("unit.txt")
        for x in self.dev_listing:
            self.ui.dev_combo.addItem(x.split()[0])
        #self.dev_listing = open("app_data\\unit.txt",'a')
        #self.dev_listing.write("33\n")
        #self.dev_listing.close()
        self.ui.actionAdd_Device.triggered.connect(self.add_device)
        
    def add_device(self):
        text, okPressed = QInputDialog.getText(self, "New device","Device number:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.dev_listing = open("unit.txt",'a')
            self.dev_listing.write("{}\n".format(text))
            self.dev_listing.close()

    
    def change_param(self, index):
        self.index_stored = index
        
    def action200(self):
        self.sel_dpi = 200
        self.res_change()
        
    def action300(self):
        self.sel_dpi = 300
        self.res_change()
        
    def action400(self):
        self.sel_dpi = 400
        self.res_change()
        
    def action600(self):
        self.sel_dpi = 600
        self.res_change()
        
    def res_change(self):
        if self.current_pic:
            plt = self.current_pic
            plt.savefig("res_change.png", dpi=self.sel_dpi)
            changed_map = QPixmap('res_change.png')
            self.ui.pic_label.setPixmap(changed_map)
            self.ui.current_dpi.setText("Current resolution: {}".format(self.sel_dpi))
        else:
            self.sel_data_warning("resolution")
    
    def save_button(self):
        if self.current_pic:
            saved_file = self.saveFileDialog()
            plt = self.current_pic
            plt.savefig(saved_file, dpi=300)
        else:
            self.sel_data_warning("save as")
            
    
    def sel_data_warning(self,message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Please load a chart before selecting {}".format(message))
        msgBox.setWindowTitle("Caution")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
    
    def calc_date_range(self):
        self.start_date = self.ui.date_start.dateTime()
        self.end_date = self.ui.date_end.dateTime()
        self.date_hold = self.start_date
        
    def dev_select(self):
        self.device_selected = self.ui.dev_combo.currentText()
        self.change_bool = 1
                   
    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            self.time_bool = 1
            self.ui.calendarWidget.setEnabled(False)
            
        else:
            self.time_bool = 0
            self.ui.calendarWidget.setEnabled(True)

        
    def refresh_data(self):
        if self.change_bool == 1:
            self.flag_data = 0
            try:
                self.sheet = client.open('Weather Station {}'.format(self.device_selected)).sheet1
            except:
                self.flag_data = 1
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Invalid device! Please select a different device")
                msgBox.setWindowTitle("Caution")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
            if self.flag_data == 0:
                
                self.date = self.sheet.col_values(1)
                self.wind = self.sheet.col_values(2)
                self.voltage = self.sheet.col_values(3)
                self.temp = self.sheet.col_values(4)
                self.soil_moisture = self.sheet.col_values(5)
                self.humidity = self.sheet.col_values(6)
                self.pressure = self.sheet.col_values(7)
                self.soil_temp = self.sheet.col_values(8)
                self.wind_dir = self.sheet.col_values(9)
                self.activate(self.ui.sel_combo.currentIndex())
                self.change_bool = 1
                self.activate(self.index_stored)
#            except:
#                msgBox = QMessageBox()
#                msgBox.setIcon(QMessageBox.Warning)
#                msgBox.setText("Invalid device! Please select a different device")
#                msgBox.setWindowTitle("Caution")
#                msgBox.setStandardButtons(QMessageBox.Ok)
#                returnValue = msgBox.exec()
        else:
            #self.activate(self.ui.sel_combo.currentIndex())
            self.activate(self.index_stored)
        
    def download_data(self):
        self.sheet = client.open('Weather Station {}'.format(self.device_selected)).sheet1
        self.date = self.sheet.col_values(1)
        self.wind = self.sheet.col_values(2)
        self.voltage = self.sheet.col_values(3)
        self.temp = self.sheet.col_values(4)
        self.soil_moisture = self.sheet.col_values(5)
        self.humidity = self.sheet.col_values(6)
        self.pressure = self.sheet.col_values(7)
        self.soil_temp = self.sheet.col_values(8)
        self.wind_dir = self.sheet.col_values(9)
        
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save as","","Image Files (*.png)", options=options)
        if fileName:
            return(fileName)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#app = QApplication(sys.argv)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
self.dev_listing.close()
