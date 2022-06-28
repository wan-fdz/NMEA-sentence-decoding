""" nmea-sentence-decoding.py

    Author: Vanessa Fernández
    Contact: vfernandezv6@gmail.com
    First created: 09/28/20
    Last updated: 10/04/20
"""

#Import standard libraries
from csv import reader
import numpy as np
import pandas as pd

def decode_gpgga(gps_line):
    """
    Print in console the $GPGGA NMEA sentence 

    :param gps_line: the actual row read from the dataset containing the $GPGGA information
    :return: None
    """
    print('\n')
    gps_message = np.array(gps_line)
    if(len(gps_message) == 15):

        print('\n')
        print('NMEA Sentence: {}'.format(gps_message[0]))
        print('UTC Time: {}'.format(gps_message[1]))
        print('Latitude: {}'.format(gps_message[2]))
        print('Latitude reference: {}'.format(gps_message[3]))
        print('Longitude: {}'.format(gps_message[4]))
        print('Longitude reference: {}'.format(gps_message[5]))
        print('GPS quality indicator: {}'.format(gps_message[6]))
        print('Number of satellites in use: {}'.format(gps_message[7]))
        print('Horizontal dilution of position: {}'.format(gps_message[8]))
        print('Antenna altitude below/above mean sea level: {}'.format(gps_message[9]))
        print('Meters (antenna heigh unit): {}'.format(gps_message[10]))
        print('Geoidal separation: {}'.format(gps_message[11]))
        print('Meters: {}'.format(gps_message[12]))
        print('Age in seconds since the last update: {}'.format(gps_message[13]))
        print('Checksum: {}'.format(gps_message[14]))
    
    return None

def decode_gpgsa(gps_line):
    """
    Print in console the $GPGSA NMEA sentence 

    :param gps_line: the actual row read from the dataset containing the $GPGSAinformation
    :return: None
    """

    print('\n')
    gps_message = np.array(gps_line)
    if(len(gps_message) == 18):
        print('\n')
        print('NMEA Sentence: {}'.format(gps_message[0]))
        print('Operation mode: {}'.format(gps_message[1]))
        print('Geometry mode: {}'.format(gps_message[2]))
        print('ID of 1st satellite in view used for position fix: {}'.format(gps_message[3]))
        print('ID of 2nd satellite in view used for position fix: {}'.format(gps_message[4]))
        print('ID of 3rd satellite in view used for position fix: {}'.format(gps_message[5]))
        print('ID of 4th satellite in view used for position fix: {}'.format(gps_message[6]))
        print('ID of 5th satellite in view used for position fix: {}'.format(gps_message[7]))
        print('ID of 6th satellite in view used for position fix: {}'.format(gps_message[8]))
        print('ID of 7th satellite in view used for position fix: {}'.format(gps_message[9]))
        print('ID of 8th satellite in view used for position fix: {}'.format(gps_message[10]))
        print('ID of 9th satellite in view used for position fix: {}'.format(gps_message[11]))
        print('ID of 10th satellite in view used for position fix: {}'.format(gps_message[12]))
        print('ID of 11th satellite in view used for position fix: {}'.format(gps_message[13]))
        print('ID of 12th satellite in view used for position fix: {}'.format(gps_message[14]))
        print('Position Dilution of Precision PDOP: {}'.format(gps_message[15]))
        print('Horizontal Dilution of Precision HDOP: {}'.format(gps_message[16]))
        print('Vertical Dilution of Precision: {}'.format(gps_message[17]))


    return None

def decode_gpgsv(gps_line):
    """
    Print in console the $GPGSV NMEA sentence 

    :param gps_line: the actual row read from the dataset containing the $GPGSV information
    :return: None
    """    
    print('\n')
    gps_message = np.array(gps_line)
    if(len(gps_message) == 20):

        print('\n')
        print('NMEA Sentence: {}'.format(gps_message[0]))
        print('Total number of messages of this type in this cycle: {}'.format(gps_message[1]))
        print('Message number: {}'.format(gps_message[2]))
        print('Total number of satellites in view: {}'.format(gps_message[3]))
        print('1st sat: Pseudo random noise PRN number: {}'.format(gps_message[4]))
        print('1st sat: Elevation in degrees [max 90 degrees]: {}'.format(gps_message[5]))
        print('1st sat: Azimuth, degrees from true north [000-359]: {}'.format(gps_message[6]))
        print('1st sat: SNR [00-99dB - null when not tracking]: {}'.format(gps_message[7]))
        print('2nd sat: Pseudo random noise PRN number: {}'.format(gps_message[8]))
        print('2nd sat: Elevation in degrees [max 90 degrees]: {}'.format(gps_message[9]))
        print('2nd sat: Azimuth, degrees from true north [000-359]: {}'.format(gps_message[10]))
        print('2nd sat: SNR [00-99dB - null when not tracking]: {}'.format(gps_message[11]))
        print('3rd sat: Pseudo random noise PRN number: {}'.format(gps_message[12]))
        print('3rd sat: Elevation in degrees [max 90 degrees]: {}'.format(gps_message[13]))
        print('3rd sat: Azimuth, degrees from true north [000-359]: {}'.format(gps_message[14]))
        print('3rd sat: SNR [00-99dB - null when not tracking]: {}'.format(gps_message[15]))
        print('4th sat: Pseudo random noise PRN number: {}'.format(gps_message[16]))
        print('4th sat: Elevation in degrees [max 90 degrees]: {}'.format(gps_message[17]))
        print('4th sat: Azimuth, degrees from true north [000-359]: {}'.format(gps_message[18]))
        print('4th sat: SNR [00-99dB - null when not tracking]: {}'.format(gps_message[19]))

    return None

def decode_gprmc(gps_line):
    """
    Print in console the $GPRMC NMEA sentence 

    :param gps_line: the actual row read from the dataset containing the $GPRMC information
    :return: None
    """
    print('\n')
    gps_message = np.array(gps_line)
    if(len(gps_message) == 13):
        print('\n')
        print('NMEA Sentence: {}'.format(gps_message[0]))
        print('Time stamp: {}'.format(gps_message[1]))
        print('Validity: {}'.format(gps_message[2]))
        print('Current latitude: {}'.format(gps_message[3]))
        print('Current latitude direction: {}'.format(gps_message[4]))
        print('Current longitude: {}'.format(gps_message[5]))
        print('Current longitude direction: {}'.format(gps_message[6]))
        print('Speed in knots: {}'.format(gps_message[7]))
        print('True course: {}'.format(gps_message[8]))
        print('Date stamp: {}'.format(gps_message[9]))
        print('Variation: {}'.format(gps_message[10]))
        print('East/West: {}'.format(gps_message[11]))
        print('Checksum: {}'.format(gps_message[12]))

    return None
  
def read_gps_data(gps_data_file):
    """
    Read raw GPS data from file.
    :param gps_data_file: path and filename of raw gps data file
    :return:
        df: dataframe with the raw gps data
    """

    # try to read the 'gps_data_file'
    try:
        file_id = open(gps_data_file)

    # if an exception is raised
    except OSError:
        print("ERROR: file " + gps_data_file + "couldn't be read")
        
        # close file object
        file_id.close()

        exit(-1)

    # otherwise
    else:
        # read gps data file as pandas-type data frame
        df = pd.read_csv('dataset.csv', header=None, sep='\n')
        df = df[0].str.split(',', expand=True)             

        # close file object
        file_id.close()

    # return line
    return df

def print_dataset(gps_data_file):
    """
    Read raw GPS data from file and print it in console.
    It also calls the following functions:
    decode_gpgga(gps_line), 
    decode_gpgsa(gps_line), 
    decode_gpgsv(gps_line), 
    decode_gprmc(gps_line).
    :param gps_data_file: path and filename of raw gps data file
    :return: None
    """
    # open file in read mode
    with open('dataset.csv', 'r') as read_obj:
    
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj, delimiter=',', skipinitialspace=True)
        
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            if "$GPGGA" in row:
                decode_gpgga(row)
            if "$GPGSA" in row:
                decode_gpgsa(row)
            if "$GPGSV" in row:
                decode_gpgsv(row)
            if "$GPRMC" in row:
                decode_gprmc(row)
    return None

def create_csv(raw_data):
    """
    Read raw GPS data from file and search for the different NMEA messages,
    dividing $GPGGA, $GPGSA, $GPGSV and $GPRMC into 4 different CSV files.
    :param raw_data: raw data to convert into a dataframe
    :return: None
    """
    
    df_c = pd.DataFrame(raw_data)
    
    #Make the CSV file for the $GPGGA message
    df_gpgga = df_c[df_c.loc[:,0] == "$GPGGA"]
    df_gpgga = df_gpgga.dropna(axis=1,how='all')
    df_gpgga=pd.DataFrame(df_gpgga.values, columns = ["NMEA Sentence", "UTC Time", "Latitude", "Latitude reference",
                                                "Longitude", "Longitude reference", "GPS quality indicator",
                                                "Number of satellites in use", "Horizontal dilution of position",
                                                "Antenna altitude below/above mean sea level", 
                                                "Meters (antenna heigh unit)",
                                                "Geoidal separation", "Meters", "Age in seconds since the last update",
                                                "Checksum"])
    df_gpgga.to_csv('gpgga_dataset.csv', index = False)

    #Make the CSV file for the $GPGSA message
    df_gpgsa = df_c[df_c.loc[:,0] == "$GPGSA"]
    df_gpgsa = df_gpgsa.dropna(axis=1,how='all')
    df_gpgsa=pd.DataFrame(df_gpgsa.values, columns = ["NMEA Sentence", "Operation mode", "Geometry mode", 
        "ID of 1st satellite in view used for position fix",
        "ID of 2nd satellite in view used for position fix", "ID of 3rd satellite in view used for position fix",
        "ID of 4th satellite in view used for position fix", "ID of 5th satellite in view used for position fix",
        "ID of 6th satellite in view used for position fix", "ID of 7th satellite in view used for position fix",
        "ID of 8th satellite in view used for position fix", "ID of 9th satellite in view used for position fix", 
        "ID of 10th satellite in view used for position fix", "ID of 11th satellite in view used for position fix",
        "ID of 12th satellite in view used for position fix", "Position Dilution of Precision PDOP", 
        "Horizontal Dilution of Precision HDOP", "Vertical Dilution of Precision"])
    df_gpgsa.to_csv('gpgsa_dataset.csv', index = False)

    #Make the CSV file for the $GPGSV message
    df_gpgsv = df_c[df_c.loc[:,0] == "$GPGSV"]
    df_gpgsv = df_gpgsv.dropna(axis=1,how='all')
    df_gpgsv=pd.DataFrame(df_gpgsv.values, columns = ["NMEA Sentence", 
        "Total number of messages of this type in this cycle", 
        "Message number", "Total number of satellites in view",
        "1st sat: Pseudo random noise PRN number", "1st sat: Elevation in degrees [max 90 degrees]",
        "1st sat: Azimuth, degrees from true north [000-359]", "1st sat: SNR [00-99dB - null when not tracking]",
        "2nd sat: Pseudo random noise PRN number", "2nd sat: Elevation in degrees [max 90 degrees]",
        "2nd sat: Azimuth, degrees from true north [000-359]", "2nd sat: SNR [00-99dB - null when not tracking]", 
        "3rd sat: Pseudo random noise PRN number", "3rd sat: Elevation in degrees [max 90 degrees]",
        "3rd sat: Azimuth, degrees from true north [000-359]", "3rd sat: SNR [00-99dB - null when not tracking]", 
        "4th sat: Pseudo random noise PRN number", "4th sat: Elevation in degrees [max 90 degrees]",
        "4th sat: Azimuth, degrees from true north [000-359]", "4th sat: SNR [00-99dB - null when not tracking]"])
    df_gpgsv.to_csv('gpgsv_dataset.csv', index = False)

    #Make the CSV file for the $GPRMC message
    df_gprmc = df_c[df_c.loc[:,0] == "$GPRMC"]
    df_gprmc = df_gprmc.dropna(axis=1,how='all')
    df_gprmc=pd.DataFrame(df_gprmc.values, columns = ["NMEA Sentence", "Time stamp", "Validity", "Current latitude",
        "Current latitude direction", "Current longitude", "Current longitude direction",
        "Speed in knots", "True course", "Date stamp", "Variation", "East/West", "Checksum"])
    df_gprmc.to_csv('gprmc_dataset.csv', index = False)

    return None
    
def main():
    """
    This function calls the following functions in order to read the GPS data, make the 4 CSV files and print in console:
        read_gps_data(gps_data_file), 
        create_csv(raw_data),
        print_dataset(gps_data_file).
    :param:
        No parameters
    :return:
        Nothing to return
    """
    gps_df = "dataset.csv"
    d_set= read_gps_data(gps_data_file=gps_df)
    create_csv(raw_data=d_set)
    print_dataset(gps_data_file=gps_df)

    return None
    
main()

