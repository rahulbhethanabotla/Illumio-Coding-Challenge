import pandas as pd

class Firewall:
    def __init__(self, filepath):
        try:
            self.filepath = filepath
        except:
            print("There must have been wrong with the filepath you entered: " + filepath)

        try:
            # documentation for this method obtained from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
            self.df = pd.read_csv(self.filepath, header = None) # this will throw an error if any of the lines in the .csv file are malformed
        except:
            print("One of the lines in your input file is malformed. Please review and adjust this line.")




    def is_valid_ip_address(self, ip_address):
        octets = ip_address.strip().split(".")
        for octet in octets:
            if (int(octet) < 0 or int(octet) > 255):
                return False
        return True


    def accept_packet(self, direction, protocol, port, ip_address):
        if not isinstance(direction, str):
            raise TypeError
        if (direction != "inbound" or direction != "outbound"):
            raise ValueError

        if not isinstance(protocol, str):
            raise TypeError
        if (protocol != "udp" or protocol != "udp"):
            raise ValueError

        if not isinstance(port, int):
            raise TypeError
        if ("-" in port):
            range = port.strip().split("-")
            if (range[1] < 1 or range[1] > 655535 or range[0] < 1 or range[0] > 65535 or range[0] >= range[1]):
                raise ValueError
        else:
            if port < 1 or port > 65535:
                raise ValueError

        if not isinstance(ip_address, str):
            raise TypeError
        if ("-" in ip_address):
            range = port.strip().split("-")
            if (not is_valid_ip_address(range[0]) or not is_valid_ip_address(range[1])):
                raise ValueError
        else:
            if not is_valid_ip_address(ip_address):
                raise ValueError


        for row in df.itertuples(False, name = None): # the itertuples() method is the most efficient way of iterating through the rows of a dataframe
            direction_matches = row[0] = direction
            protocol_matches = row[1] = protocol

            port_satisfies_conditions = False
            if ("-" in row[2]):
                range = port.strip().split("-")
                port_satisfies_conditions = int(range[0]) <= port and port <= int(range[1])
            else:
                port_satisfies_conditions = int(row[2]) == port


            ip_address_satisfies = False
            if ("-" in row[3]):
                range = port.strip().split("-")
                ip_address_satisfies = range[0] <= port and port <= range[1]
            else:
                ip_address_satisfies = row[3] == ip_address


            if (direction_matches and protocol_matches and port_satisfies_conditions and ip_address_satisfies):
                return True
        return False

