import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow
from UI_MainWindow import Ui_mainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.main_win)

        # Define UI Elements
        self.lcd = self.ui.lcd_display
        self.time_setting = self.ui.time_edit_box
        self.status_bar = self.ui.statusbar

        # Set Timer Loop Status
        self.timer_status = False

        # Set GUI Init Value
        self.display_contents = "0:00"

        # Connect UI Button to Respective Functions
        self.ui.start_timer_btn.clicked.connect(self.start_timer)
        self.ui.reset_timer_btn.clicked.connect(self.reset_timer)

    def show(self):
        self.main_win.show()

    def timer(self, duration):
        seconds = 59
        duration -= 1
        seconds, duration = int(seconds), int(duration)

        while self.timer_status == True:

            QApplication.processEvents()

            if duration == 0 and seconds == 0:
                # Write to Display
                self.display_contents = "-:--"
                self.update_lcd()

                # Flash Status Bar Message
                self.status_bar.showMessage("Timer Ended")

                # End Function
                self.timer_status = False

            elif duration == 0 and seconds > 0:
                # Format Time
                if seconds <= 9:
                    self.display_contents = str(duration) + ":0" + str(seconds)
                else:
                    self.display_contents = str(duration) + ":" + str(seconds)

                # Write to Display
                self.update_lcd()

                # Countdown Logic
                seconds -= 1
                time.sleep(1)

            elif duration > 0 and seconds == 0:
                # Format Time
                if seconds <= 9:
                    self.display_contents = str(duration) + ":0" + str(seconds)
                else:
                    self.display_contents = str(duration) + ":" + str(seconds)

                # Write to Display
                self.update_lcd()

                # Time Logic
                duration -= 1
                seconds += 59
                time.sleep(1)

            elif duration > 0 and seconds > 0:
                # Format Time
                if seconds <= 9:
                    self.display_contents = str(duration) + ":0" + str(seconds)
                else:
                    self.display_contents = str(duration) + ":" + str(seconds)

                # Write to Display
                self.update_lcd()

                # Time Logic
                seconds -= 1
                time.sleep(1)

            else:
                # Flash Status Bar Message
                self.status_bar.showMessage("Error!")

                # End Function + Exit App
                self.timer_status = False
                time.sleep(1)
                sys.exit(1)

    def start_timer(self):
        # Flash Status Bar Message
        self.status_bar.showMessage("Timer Started")

        # Get Time Value From Input Box
        time_input = self.time_setting.time().minute()

        # Check if a time if provided
        if time_input <= 0:
            # Flash Status Bar Message
            self.status_bar.showMessage("Time <= 0 Minutes")

        # Start Timer
        self.timer_status = True

        # Call Timer Function
        self.timer(time_input)

    def reset_timer(self):
        # Set Timer Loop Status
        self.timer_status = False

        # Clear LCD Screen
        self.display_contents = "0:00"
        self.update_lcd()

        # Flash Status Bar Message
        self.status_bar.showMessage("Timer Reset")

    def update_lcd(self):
        self.lcd.display(self.display_contents)
        self.lcd.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
