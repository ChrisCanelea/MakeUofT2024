import sys
import requests
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime

BASE_URL = "http://192.168.4.1/"
route_num = -1
start_location = ""

location_list = []
substrings = ['0', '0', '0']
should_start = False

class MainWindow(QMainWindow):
    def __init__(self):
        global substrings
        global location_list

        super().__init__()
        self.setWindowTitle('Smart Home App')
        self.resize(800, 480)

        # Create a central widget and set layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QGridLayout(central_widget)

        # Create a stacked widget for managing screens
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget, 0, 0, 1, 3)

        # Create the home screen
        home_screen = QWidget()
        home_layout = QVBoxLayout(home_screen)

        # Add a big title label to the home screen
        title_label = QLabel('Welcome to Intelligent Residence')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 24pt; color: #333; padding: 20px;')
        home_layout.addWidget(title_label)

        home_button_layout = QHBoxLayout()
        button1 = QPushButton('Intelligent Transit')
        button2 = QPushButton('App 2')
        button3 = QPushButton('App 3')
        
        # Increase font size of buttons
        button1.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        button2.setStyleSheet('QPushButton { background-color: #008CBA; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        button3.setStyleSheet('QPushButton { background-color: #f44336; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        
        button1.setFixedSize(200, 200)
        button2.setFixedSize(200, 200)
        button3.setFixedSize(200, 200)
        home_button_layout.addWidget(button1)
        home_button_layout.addWidget(button2)
        home_button_layout.addWidget(button3)

        home_layout.addLayout(home_button_layout)
        home_screen.setLayout(home_layout)
        self.stacked_widget.addWidget(home_screen)

        # Create the screen for option 1
        option1_screen = QWidget()
        option1_layout = QVBoxLayout(option1_screen)

        back_button = QPushButton('↩')
        back_button.setStyleSheet('font-size: 24pt; padding: 10px; border: none; background-color: transparent;')
        back_button.setFixedSize(50, 50)
        back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))  # Switch to home screen

        # Info
        title = QLabel("Intelligent Transit")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 20pt; color: #333; padding: 10px;')
        
        self.body = QLabel("Next trains for number " + str(route_num) + " bus departing from " + start_location + ":")
        self.body.setAlignment(Qt.AlignCenter)
        self.body.setStyleSheet('font-size: 16pt; color: #333; padding: 0px;')
        self.body.setWordWrap(True)

        self.time0_label = QLabel(str(int(int(substrings[0]) / 60)) + ":" + str(int(substrings[0]) % 60))
        self.time0_label.setAlignment(Qt.AlignCenter)
        self.time0_label.setStyleSheet('font-size: 16pt; color: #333; padding: 0px;')
        self.time1_label = QLabel(str(int(int(substrings[1]) / 60)) + ":" + str(int(substrings[1]) % 60))
        self.time1_label.setAlignment(Qt.AlignCenter)
        self.time1_label.setStyleSheet('font-size: 14pt; color: #333; padding: 0px;')
        self.time2_label = QLabel(str(int(int(substrings[2]) / 60)) + ":" + str(int(substrings[2]) % 60))
        self.time2_label.setAlignment(Qt.AlignCenter)
        self.time2_label.setStyleSheet('font-size: 12pt; color: #333; padding: 0px;')

        select_button = QPushButton('Change Route')
        select_button.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        # select_button.setStyleSheet('font-size: 24pt; padding: 10px; border: none; background-color: transparent;')
        # select_button.setFixedSize(50, 50)
        # select_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        option1_layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)  # Align button to top-left
        option1_layout.addWidget(title)
        option1_layout.addWidget(self.body)
        option1_layout.addWidget(self.time0_label)
        option1_layout.addWidget(self.time1_label)
        option1_layout.addWidget(self.time2_label)
        option1_layout.addWidget(select_button)
        option1_screen.setLayout(option1_layout)
        self.stacked_widget.addWidget(option1_screen)

        # Create the screen for route selection
        route_screen = QWidget()
        route_layout = QVBoxLayout(route_screen)

        done_button = QPushButton('↩')
        done_button.setStyleSheet('font-size: 24pt; padding: 10px; border: none; background-color: transparent;')
        done_button.setFixedSize(50, 50)
        done_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        done_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))  # Switch back to option1 screen

        route_body = QLabel("Please enter your daily route number")
        route_body.setAlignment(Qt.AlignCenter)
        route_body.setStyleSheet('font-size: 18pt; color: #333; padding: 0px;')
        route_body.setWordWrap(True)

        self.textbox = QLineEdit(self)
        self.textbox.setAlignment(Qt.AlignCenter)
        self.textbox.setStyleSheet('font-size: 16pt; padding: 10px; border: 2px solid #333; border-radius: 5px;')
        # self.textbox.setFixedSize(100, 50)
        # self.textbox.move(50, 50)

        enter_button = QPushButton("Enter")
        enter_button.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        enter_button.clicked.connect(lambda: self.get_stops())  # Get stops based on route

        route_layout.addWidget(done_button)
        route_layout.addWidget(route_body)
        route_layout.addWidget(self.textbox)
        route_layout.addWidget(enter_button)
        route_screen.setLayout(route_layout)
        self.stacked_widget.addWidget(route_screen)

        # Create the screen for stop selection
        stop_screen = QWidget()
        stop_layout = QVBoxLayout(stop_screen)

        return_button = QPushButton('↩')
        return_button.setStyleSheet('font-size: 24pt; padding: 10px; border: none; background-color: transparent;')
        return_button.setFixedSize(50, 50)
        return_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        return_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))  # Switch back to route screen

        stop_body = QLabel("Please select your start location")
        stop_body.setAlignment(Qt.AlignCenter)
        stop_body.setStyleSheet('font-size: 18pt; color: #333; padding: 0px;')
        stop_body.setWordWrap(True)

        self.selection = QComboBox()
        self.selection.setStyleSheet('font-size: 16pt; padding: 10px; border: 2px solid #333; border-radius: 5px;')
        self.selection.addItems(location_list)

        next_button = QPushButton("Enter")
        next_button.setStyleSheet('QPushButton { background-color: #4CAF50; color: white; border: none; padding: 15px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 10px; cursor: pointer; border-radius: 10px; }')
        next_button.clicked.connect(lambda: self.select_page())  # Update start location and return to option1 screen

        stop_layout.addWidget(return_button)
        stop_layout.addWidget(stop_body)
        stop_layout.addWidget(self.selection)
        stop_layout.addWidget(next_button)
        stop_screen.setLayout(stop_layout)
        self.stacked_widget.addWidget(stop_screen)

        # Connect button1 to switch to option 1 screen
        button1.clicked.connect(lambda: self.select_page())

        # Connect select button to route select screen
        select_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))  # Switch to route select screen

        # Set the layout alignment for the stacked widget to top left
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        # Add label for displaying current time
        self.time_label = QLabel()
        self.time_label.setStyleSheet('font-size: 16pt; color: #333; border: none; background-color: transparent;')
        self.time_label.setAlignment(Qt.AlignRight | Qt.AlignTop)
        main_layout.addWidget(self.time_label, 0, 2)  # Add time label to the top-right corner
        self.update_time()  # Update time initially
        time_timer = QTimer(self)
        time_timer.timeout.connect(self.update_time)
        time_timer.start(1000)  # Update time every second

    def select_page(self):
        global start_location
        global should_start

        # print(str(route_num))
        
        if route_num == -1:
            self.stacked_widget.setCurrentIndex(2)
        else:
            start_location = self.selection.currentText()
            should_start = True
            self.body.setText("Next trains for number " + str(route_num) + " bus departing from " + start_location + ":")
            self.stacked_widget.setCurrentIndex(1)
    
    def update_time(self):
        global substrings
        global route_num
        global start_location
        global location_list
        global should_start

        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss')
        self.time_label.setText(display_text)

        if int(display_text[-2:]) % 5 == 0:
            # print(int(display_text[-2:]))
            if should_start == True:
                r1 = requests.get(BASE_URL + "$" + start_location)
                if r1.content != b'Received':
                    exit()
                # time.sleep(4)
                r2 = requests.get(BASE_URL + "result")
                substrings = r2.content.decode('utf-8').split("\r\n")
                # substrings = ['1054', '1894', '5922']

            print(substrings)
            self.time0_label.setText(str(int(int(substrings[0]) / 60)) + ":" + str(int(substrings[0]) % 60))
            self.time2_label.setText(str(int(int(substrings[2]) / 60)) + ":" + str(int(substrings[2]) % 60))
            self.time1_label.setText(str(int(int(substrings[1]) / 60)) + ":" + str(int(substrings[1]) % 60))

            # print("minutes: " + str(int(int(substrings[0]) / 60)))
            # print("seconds: " + str(int(substrings[0]) % 60))

    def get_stops(self):
        global location_list
        global route_num

        route_num = self.textbox.text()
        r1 = requests.get(BASE_URL + "&" + str(route_num))
        if r1.content != b'Received':
            exit()
        # time.sleep(5)
        # print(r.content.decode('utf-8'))
        r2 = requests.get(BASE_URL + "result")
        print(r2.content.decode('utf-8'))
        location_list = r2.content.decode('utf-8').split("\r\n")
        # location_list = ['opt1', 'opt2', 'opt3', '']
        location_list.remove("")
        self.selection.clear()
        self.selection.addItems(location_list)
        self.stacked_widget.setCurrentIndex(3)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
