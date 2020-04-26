import os
import rospy
import rospkg
import subprocess
import getpass


from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QFileDialog, QLayoutItem, QCheckBox
from python_qt_binding.QtGui import QIcon
from os.path import expanduser


robot_dict = {}
alg_dict = {}
home = expanduser("~")

class MyPlugin(Plugin):
	#Do Not Touch, this is required code for python qt
    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        
        self.setObjectName('MyPlugin')

        
        from argparse import ArgumentParser
        parser = ArgumentParser()
        
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
    #There is where icons and logic for buttons are set    
	self._widget.load_algorithm_button.setIcon(QIcon.fromTheme('document-open'))
	self._widget.add_robot.pressed.connect(self._update_robot_list)
	self._widget.load_algorithm_button.pressed.connect(self._add_algorithm)
	self._widget.run_button.pressed.connect(self.run_funct)
	self._widget.push_button.pressed.connect(self.push_funct)
	
	#This loops through robots.txt to populate the robots section
	path =  home +'/deploy/robots.txt'
	file_object = open(path, 'r')
	counter = 0
	for lines in file_object:
		values = lines.split()
		if values[1] is not None:
			robot_dict[counter] = [values[0], QCheckBox(values[1])]
			self._widget.robot_check_layout.addWidget(robot_dict.get(counter)[1],int(counter/3),counter%3,1,1)
		counter +=1
	file_object.close()

	#This loops through algorithms.txt to populate the algorithms section
	path = home +'/deploy/algorithms.txt'
	file_object = open(path, 'r')
	counter = 0
	for lines in file_object:
		values = lines.split('/')
		if values[-1] is not None or "":
			alg_dict[counter] = [lines,QCheckBox(values[-1]),values[-1].rstrip()]
			self._widget.algorithm_radio_layout.addWidget(alg_dict.get(counter)[1],int(counter/3),counter%3,1,1)
		counter +=1
	file_object.close()	
	
	
	
	# Add widget to the user interface
	context.add_widget(self._widget)

    def run_funct(self):
	for alg_check in alg_dict:
		for check in robot_dict:
			if robot_dict[check][1].checkState() == 2:
				if alg_dict[alg_check][1].checkState() == 2:
					subprocess.call([home +'/deploy/start_robot.sh', robot_dict[check][0], alg_dict[alg_check][2]])

	
    def push_funct(self):
	for alg_check in alg_dict:
		for check in robot_dict:
			if robot_dict[check][1].checkState() == 2:
				if alg_dict[alg_check][1].checkState() == 2:
					subprocess.call([home +'/deploy/push_alg.sh', robot_dict[check][0], alg_dict[alg_check][0]])

    def _add_algorithm(self, file_name=None):
	if file_name is None:
            file_name = QFileDialog.getExistingDirectory(
                self._widget, self.tr('Upload Algorithm'), None, QFileDialog.ShowDirsOnly)
            if file_name is None or file_name == '':
                return
	
	path = home +'/deploy/algorithms.txt'
	if file_name:	
		file_object = open(path, 'a')
		file_object.write(file_name + '\n')
		file_object.close()
		print("Added Algorithm ")


    def _update_robot_list(self):
	path = home +'/deploy/robots.txt'
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
