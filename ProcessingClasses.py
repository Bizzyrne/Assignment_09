#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdid, cdtitle, cdartist = CDInfo
        
        ID = cdid
        title = cdtitle.strip()
        artist = cdartist.strip()
        
        try:
            ID = int(ID)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(ID, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # DONE add code as required
    
        cd_idx = int(cd_idx)
        
        for item in table:
            cd_id_x = int(item.cd_id)
            if cd_id_x == cd_idx:
                temp_obj = item
                break
            else:
                temp_obj = None
                
        if temp_obj == None:
            raise Exception("CD not in inventory!!")
        else:
            return temp_obj

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        # DONE add code as required
        try:
            trk_pos = int(track_info[0])
        except:
            print("Error:")
        trk_title = track_info[1]
        trk_len = track_info[2]
        
        try:
            cd.add_track(DC.Track(trk_pos, trk_title, trk_len))
            
        except:
            print("Track Position is not an integer.  Returning.")


