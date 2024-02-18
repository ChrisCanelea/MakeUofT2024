import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime

class MainWindow(QMainWindow):
    def __init__(self):
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
        button2 = QPushButton('Option 2')
        button3 = QPushButton('Option 3')
        
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
        option1_label = QLabel('Option 1 Screen')
        back_button = QPushButton('↩')
        back_button.setStyleSheet('font-size: 24pt; padding: 10px; border: none; background-color: transparent;')
        back_button.setFixedSize(50, 50)
        back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))  # Switch to home screen
        
        option1_layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)  # Align button to top-left
        option1_layout.addWidget(option1_label)
        option1_screen.setLayout(option1_layout)
        self.stacked_widget.addWidget(option1_screen)

        # Connect button1 to switch to option 1 screen
        button1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

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
    
    def update_time(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss')
        self.time_label.setText(display_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
