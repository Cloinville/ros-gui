import os
import rospy
import rospkg

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QFileDialog, QLayoutItem, QCheckBox
from python_qt_binding.QtGui import QIcon

class MyPlugin(Plugin):

    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_mypkg'), 'resource', 'MyPlugin.ui')
        loadUi(ui_file, self._widget)
        self._widget.setObjectName('MyPluginUi')
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        

        self._widget.load_algorithm_button.setIcon(QIcon.fromTheme('document-open'))
	self._widget.add_robot.pressed.connect(self._update_robot_list)
	self._widget.load_algorithm_button.pressed.connect(self._add_algorithm)
	
	path = '/home/colin/ros-gui/deploy/robots.txt'
	file_object = open(path, 'r')
	robot_dict = {}
	counter = 0
	for lines in file_object:
		values = lines.split()
		if values[1] is not None:
			robot_dict[counter] = QCheckBox(values[1])
			self._widget.robot_check_layout.addWidget(robot_dict.get(counter))
		counter +=1
	file_object.close()	
	#button1 =  QCheckBox("One")
	#self._widget.robot_check_layout.addWidget(button1)
	
	
	# Add widget to the user interface
	context.add_widget(self._widget)

    def run_funct(self):
	print("I run")

    def _add_algorithm(self, file_name=None):
	if file_name is None:
            file_name, _ = QFileDialog.getOpenFileName(
                self._widget, self.tr('Upload Algorithm'), None, None)
            if file_name is None or file_name == '':
                return
	
	path = '/home/colin/ros-gui/deploy/algorithms.txt'
	if file_name:	
		file_object = open(path, 'a')
		file_object.write(file_name)
		file_object.close()
		print("Added Algorithm ")


    def _update_robot_list(self):
	#path = '/opt/ros/kinetic/share/rqt_mypkg/resource/robots.txt'
	path = '/home/colin/ros-gui/deploy/robots.txt'
	ip = self._widget.ip_address.text()
	name = self._widget.robot_name.text()
	if ip and name:
		file_object = open(path, 'a')
		file_object.write(ip + " " + name + '\n')
		file_object.close()
		print("Added Robot " + name)
		
    
    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog
