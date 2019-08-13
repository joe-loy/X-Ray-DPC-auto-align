import usb.core
import usb.util


MOTOR_TYPE = {
        "0":"No motor connected",
        "1":"Motor Unknown",
        "2":"'Tiny' Motor",
        "3":"'Standard' Motor"
        }


"""
MotorController
This class is used to control a rig containing five picomotors which can be used to adjust five different
degrees of freedom of movement for the gratings. This class uses the axis convention usually applied in optics
of making the z axis the direction in which the x-rays pass through the gratings. Thus, the X axis controls
side to side movement of the grating.
"""



class MotorController():
    
    # Establish serial connection with motors and setup controller
    def __init__(self):
        vid = 0x104d
        pid = 0x4000
        self.dev = usb.core.find(idProduct=pid, idVendor=vid)
        print(self.dev)

        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.dev.set_configuration()

        # get an endpoint instance
        cfg = self.dev.get_active_configuration()
        intf = cfg[(0,0)]

        self.ep_out = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)

        self.ep_in = usb.util.find_descriptor(
            intf,
            # match the first IN endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_IN)

        assert (self.ep_out and self.ep_in) is not None
        """
        
        """

        # Establish RS-485 Network Connection
        # Serial command SC2 scans RS-485 network of master controller and assigns
        # an address to controller 2
        scanNetwork = self.command('SC2')
        self.command('SC')


        # Test to confirm that both master and slave controllers are connected
        # Confirm connection to user
        resp = self.command('VE?')
        print("Connected to Motor Controller Model {}. Firmware {} {} {}\n".format(
                                                    *resp.split(' ')
                                                    ))
        numTranMotors = 2
        numRotMotors = 3
        # Translational Motors will be connected to master controller
        # Rotational Motors will be connected to slave controller
        # Slave controller commands must be prefixed with "2>"
        """
        for m in range(1,numTranMotors):
            resp = self.command("{}QM?".format(m))
            print("Motor #{motor_number}: {status}".format(
                                                    motor_number=m,
                                                    status=MOTOR_TYPE[resp[-1]]
                                                    ))
        for m in range(1,numRotMotors):
            resp = self.command("2>{}QM?".format(m))
            print("Motor #{motor_number}: {status}".format(
                                                    motor_number=m,
                                                    status=MOTOR_TYPE[resp[-1]]
                                                    ))
        """
        

        
         
    def send_command(self, usb_command, get_reply=False):
        """Send command to USB device endpoint
        
        Args:
            usb_command (str): Correctly formated command for USB driver
            get_reply (bool): query the IN endpoint after sending command, to 
                get controller's reply
        Returns:
            Character representation of returned hex values if a reply is 
                requested
        """
        self.ep_out.write(usb_command)
        if get_reply:
            return self.ep_in.read(100)
            
    # Used to convert a NewFocus command into a USB command
    def parse_command(self, newfocus_command):
        """Convert a NewFocus style command into a USB command
        Args:
            newfocus_command (str): of the form xxAAnn
                > The general format of a command is a two character mnemonic (AA). 
                Both upper and lower case are accepted. Depending on the command, 
                it could also have optional or required preceding (xx) and/or 
                following (nn) parameters.
                cite [2 - 6.1.2]
        """
        # Add a carriage return at the end to make the command valid
        newfocus_command += '\r'
        return newfocus_command
        
    # Used to return the reply of the motor from the serial command
    def parse_reply(self, reply):
        """Take controller's reply and make human readable
        Args:
            reply (list): list of bytes returns from controller in hex format
        Returns:
            reply (str): Cleaned string of controller reply
        """

        # convert hex to characters 
        reply = ''.join([chr(x) for x in reply])
        return reply.rstrip()

    # Sends a NewFocus command to a motor as a usb command 
    def command(self, newfocus_command):
        """Send NewFocus formated command
        Args:
            newfocus_command (str): Legal command listed in usermanual [2 - 6.2] 
        Returns:
            reply (str): Human readable reply from controller
        """
        usb_command = self.parse_command(newfocus_command)

        # if there is a '?' in the command, the user expects a response from
        # the driver
        if '?' in newfocus_command:
            get_reply = True
        else:
            get_reply = False

        reply = self.send_command(usb_command, get_reply)

        # if a reply is expected, parse it
        if get_reply:
            return self.parse_reply(reply)

    
    # Close serial connection with the MotorController when finished
    def closeMotorController():
        print(0)
        
        
    # Used to translationally move grating in X-axis relative to current position
    def moveX(self, direction, distance):
        if (direction == 0):
            distance = -distance
        motorCommand = '1PR' + str(distance)
        self.command(motorCommand)
            



    # Used to translationally move grating in Z-axis relative to current position
    def moveZ(self, direction, distance):
        if (direction == 0):
            distance = -distance
        motorCommand = '2PR' + str(distance)
        self.command(motorCommand)
    

        
    # Used to turn grating about X-axis relative to current orientation
    def turnX(self, direction, distance):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller
        # Send usb serial command to rotational motor in X-axis
        if (direction == 0):
            distance = -distance
        motorCommand = '2>1PR' + str(distance)
        self.command(motorCommand)
        

        
    # Used to turn grating about Y-axis relative to current orientation
    def turnY(self, direction, distance):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller
        # Send usb serial command to rotational motor in Y-axis
        if (direction == 0):
            distance = -distance
        motorCommand = '2>2PR' + str(distance)
        self.command(motorCommand)

        
    # Used to turn grating about Z-axis relative to current orientation
    def turnZ(self, direction, distance):
        # Using the direction and the desired angle of rotation, create proper
        # ascii command to send to controller
        # Send usb serial command to rotational motor in Z-axis
        if (direction == 0):
            distance = -distance
        motorCommand = '2>3PR' + str(distance)
        self.command(motorCommand)
      
    # Used to autoalign gratings based on picture of the fiducial image
    def autoAllign(self):
        print(0)
    
