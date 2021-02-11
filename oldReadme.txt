Relevant remaining software tasks in approximate priority (integrate into clickup on 1-28-20)
---------------------------------------------------------------------------------------------
General Track
	• Modify nodes to use single slot deque for communication
	Sensor Track
		• Test VPN laptop-pi connection
		• Finalize Arduino ultrasonic and video sensor code
		• Integration test sensor_relay.py, ui.py, sensor_driver.ino
	Motor Track
		• Finalize Arduino wheel motor code
		• Integration test collision_avoidance.py, controller_handler.py, and motor_driver.ino
	• Integration test manual full stack
Specialized Track
	Autonomous Track
		• Finalize navigation code for known section
		• Integration test known autonomous full stack
		• Finalize navigation code for unknown section
		• Integration test unknown autonomous full stack
	Arm Track
		• Finalize Arduino arm motor code
		• Integration test manual full stack
	Magnetometer/Accelerometer Track
		• Finalize Arduino magnetometer and accelerometer code
		• Integration test manual full stack
		• Overlay magnetometer compass on UI
		• Integration test manual full stack
	Networking Track
		• Loss of Signal test (see rulebook)
		• Use DCHP to obtain ports
		• Ensure setup complies with all network rules laid out in rulebook


Robot software layout
----------------------
• Arduino 1
	• sensor_driver.ino
		• Purpose: Run sensors and output their values to the pi
		• Output: sensor_relay.py through serial
• Arduino 2
	• motor_driver.ino
		• Purpose: Run motors and perform collision avoidance
		• Input: navigation.py through serial
• Laptop
	• launch_laptop.py
		• Purpose: launch and link all laptop programs
	• ui.py
		• Purpose: Display data incoming through pi
		• Input: sensor_relay.py through upd_client
	• controller_handler.py
		• Purpose: Read controller values and output the controls to the pi
		• Output: controller_relay.py through upd_client
• Pi
	• launch_pi.py
		• Purpose: launch and link all pi programs
	• sensor_relay.py
		• Purpose: Relay the sensor values from the arduino to all the relevant programs. If wifi drops,
			continues to send on queues.
		• Input: sensor_driver.ino through serial
		• Output: ui.py through upd_client
		• Output: naviation.py through queue
		• Output: collision_avoidance.py
	• navigation.py
		• Purpose: During known autonomous section, performs state machine dead reckoning. During unknown
			autonomous section, performs unknown.
		• Input: sensor_relay.py through queue
		• Output: collision_avoidance.py through queue
	• collision_avoidance.py
		• Purpose: Route incoming control values from navigation.py and controller_handler.py. By default, ignores navigation.py
			control values. If autonomous start signal is sent, follows navigation.py controls. If autonomous stop signal is sent,
			follows controller_handler.py controls. If connection is dropped and autonomous isn't set, turn on idle. If connection
			is dropped and autonomous signal is set, follow navigation.py controls.
		• Input: navigation.py through queue
		• Input: controller_handler.py through queue
		• Output: motor_driver.ino through serial
