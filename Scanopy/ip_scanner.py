class IpScanner:

    #Sets the callback function for sending output to gui console
    def set_console_callback(self, output_to_console):
        self.output_to_console = output_to_console

    def testCallback(self, gui):
        gui.sayHi()
