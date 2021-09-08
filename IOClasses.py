#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        # DONE modify method to accept a list of file names.
        
        cd_file_name = file_name[0]
        track_file_name = file_name[1]
        
        try:
            with open(cd_file_name, 'w') as CDfile:
                for disc in lst_Inventory:
                    CDfile.write(disc.get_record())
            with open(track_file_name, 'w') as Trackfile:
                for disc in lst_Inventory:
                    trk_lst = disc.tracks
                    album_ID = disc.cd_id
                    for track in trk_lst:
                        Trackfile.write('{}, {}'.format(album_ID, track.get_record()))
            
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.

        """
        print("Loading Inventory.....\n")
        lst_Inventory = []
        
        cd_file_name = file_name[0]
        track_file_name = file_name[1]
        
        # DONE modify method to accept a list of file names
        # DONE add code to load track data
        
        try:
            with open(cd_file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cd_ident = int(data[0])
                    row = DC.CD(cd_ident, data[1], data[2])
                    lst_Inventory.append(row)
        
 
            fileobj = open(track_file_name, 'r')
            
            for line in fileobj:
                data = line.strip().split(',')
                trk_cd_ID = int(data[0])
                trk_ID = int(data[1])
                trk_title = data[2]
                trk_length = data[3]
                    
                for item in lst_Inventory:
                    cd_identity = item.cd_id
                    if trk_cd_ID == cd_identity:
                        item.add_track(DC.Track(trk_ID, trk_title, trk_length))        
            fileobj.close()
            
        except Exception:
            print('Error.  File may not exist.  No data loaded.\n')
            
        
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        while True:        
            cdId = input('Enter ID: ').strip()
            
            try:
                test = int(cdId)
                break
            except:
                print("Must enter an integer\n")
                continue
        
        
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """
        while True:
            trkId = input('Enter Position on CD / Album: ').strip()
            
            try:
                test = int(trkId)
                break
            except:
                print("Must enter an integer")
                continue
            
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

