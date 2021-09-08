#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        
        while True:
            cd_idx = input('Select the CD / Album index: ')
            try:
                Test = int(cd_idx)
                break
            except:
                print("Must be an integer")
            
            continue
            
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODO add code to handle tracks on an individual CD
        
        while True:
            print('\n')
            IO.ScreenIO.print_CD_menu()
            subchoice = IO.ScreenIO.menu_CD_choice()
            
            if subchoice == 'x':
                break
            if subchoice == 'a':
                trkID, trkTitle, trkLength = IO.ScreenIO.get_track_info()
                tempTrack = None
                tempTrack = DC.Track(trkID, trkTitle, trkLength)
                cd.add_track(tempTrack)
            elif subchoice == 'd':
                print(cd.get_record())
                print(cd.get_tracks())
            elif subchoice == 'r':
                while True:
                    trk_rem = ""
                    trk_rem = input('Select the Track to Remove: ')
                    try:
                        TRK = int(trk_rem)
                        break
                    except:
                        print("Must be an integer")
                        continue
                
                cd.rmv_track(TRK)
            else:
                print('General IN WHILE STATEMENT Error')
                continue
            
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')