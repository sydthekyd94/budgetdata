#Budget Tracker
#Simple program that takes user input, does calculations, puts it in a file.

#Created on: 8/18/20
#Last Modified on: 8/19/20
#Created by: sydthekyd94

#To use in your code, write:
#import _mod_Budget
#Otherwise, just click on this file to run it!
#Happy Budgeting! 

while True:
        print("""
Options:
Enter 'view' to view existing data
Enter 'data' to add new data to existing
Enter 'overwrite' to delete any old data and start over
Enter 'quit' to end the program""")
        user_input = input(": ")
        if user_input == 'view' or user_input == 'data':
                try: #Open past input to gather information:
                        file = open("_doc_my_budget_data.txt","r")
                        file_lines = file.readlines()
                        current_mon = int((file_lines[0].split("|"))[1])
                        current_yr = int((file_lines[1].split("|"))[1])
                        current_tot = float((file_lines[2].split("|"))[1])
                        last_mon = int((file_lines[3].split("|"))[1])
                        last_yr = int((file_lines[4].split("|"))[1])
                        last_tot = float((file_lines[5].split("|"))[1])
                        tot_save_mon = float((file_lines[6].split("|"))[1])
                        tot_lost_mon = float((file_lines[7].split("|"))[1])
                        tot_save = float((file_lines[8].split("|"))[1])
                        tot_lost = float((file_lines[9].split("|"))[1])
                        cum_avg_save = float((file_lines[10].split("|"))[1])
                        cum_avg_lost = float((file_lines[11].split("|"))[1])
                        count = float((file_lines[12].split("|"))[1])
                        first_tot = float((file_lines[13].split("|"))[1])
                        first_mon = int((file_lines[14].split("|"))[1])
                        first_yr = int((file_lines[15].split("|"))[1])
                except FileNotFoundError: #File DNE, new file needed
                        try: #creating new file
                                file = open("_doc_my_budget_data.txt","w")
                                data = 0 
                                file.write(str("Current Month|{0}\n".format(data)))
                                file.write(str("Current Year|{0}\n".format(data)))
                                file.write("Current Total|{0}\n".format(data))
                                file.write("Last Month|{0}\n".format(data))
                                file.write("Last Year|{0}\n".format(data))
                                file.write("Last Total|{0}\n".format(data))
                                file.write("Total Saved Past Month|{0}\n".format(data))
                                file.write("Total Lost Past Month|{0}\n".format(data))
                                file.write("Total Saved Over All|{0}\n".format(data))
                                file.write("Total Lost Over All|{0}\n".format(data))
                                file.write("Cumulative Avg Saved/Month|{0}\n".format(data))
                                file.write("Cumulative Avg Lost/Month|{0}\n".format(data))
                                file.write("Number of data entries|{0}\n".format(data))
                                file.write("First Total|{0}\n".format(data))
                                file.write(str("First Month|{0}\n".format(data)))
                                file.write(str("First Year|{0}\n".format(data)))
                        finally: #close file
                                file.close()
                        try: #read file
                                file = open("_doc_my_budget_data.txt","r")
                                file_lines = file.readlines()
                                current_mon = int((file_lines[0].split("|"))[1])
                                current_yr = int((file_lines[1].split("|"))[1])
                                current_tot = float((file_lines[2].split("|"))[1])
                                last_mon = int((file_lines[3].split("|"))[1])
                                last_yr = int((file_lines[4].split("|"))[1])
                                last_tot = float((file_lines[5].split("|"))[1])
                                tot_save_mon = float((file_lines[6].split("|"))[1])
                                tot_lost_mon = float((file_lines[7].split("|"))[1])
                                tot_save = float((file_lines[8].split("|"))[1])
                                tot_lost = float((file_lines[9].split("|"))[1])
                                cum_avg_save = float((file_lines[10].split("|"))[1])
                                cum_avg_lost = float((file_lines[11].split("|"))[1])
                                count = float((file_lines[12].split("|"))[1])
                                first_tot = float((file_lines[13].split("|"))[1])
                                first_mon = int((file_lines[14].split("|"))[1])
                                first_yr = int((file_lines[15].split("|"))[1])
                        finally: #close file
                                file.close()
                except: #Some other error happened
                        print("Some error occurred when trying to open the variables data file")
                finally: #close file
                        file.close()

                try: #Open historical doc
                        history = open("_doc_my_budget_history.txt","r")
                except FileNotFoundError: #File DNE, new file needed
                        try: #Writing the historical data file
                                history = open("_doc_my_budget_history.txt","w")
                                history.write("Current Month|Current Year|Current Total|Total Saved Past Month|Total Lost Past Month|Total Saved Over All|Total Lost Over All|Cumulative Avg Saved Per Month|Cumulative Avg Lost Per Month\n")
                        finally: #Close file
                                history.close()
                except: #Some other error happened
                        print("Some error occurred when trying to open the historical data file")
                finally: #close file
                        file.close()

                print("Data file successfully processed")

                if user_input == 'view': #View option lets the user see the data that is currently in the file
                        print("\nPlease see below for the summary data for the time range: {0}/{1} - {2}/{3}".format(first_mon, first_yr, current_mon, current_yr))
                        print("The current total is: {0}".format(current_tot))
                        if tot_save_mon != 0:
                                print("The Total Saved in the past recorded month is: {0}".format(tot_save_mon))
                        if tot_lost_mon != 0:
                                print("The Total Lost in the past recorded month is: {0}".format(tot_lost_mon))
                        if tot_save != 0:
                                print("The Total Saved over all is: {0}".format(tot_save))
                        if tot_lost != 0:
                                print("The Total Lost over all is: {0}".format(tot_lost))
                        if cum_avg_save != 0:
                                print("The Cumulative Avg Saved per month is: {0}".format(cum_avg_save))
                        if cum_avg_lost != 0:
                                print("The Cumulative Avg Lost per month is: {0}".format(cum_avg_lost))
                        
                elif user_input == 'data': #Data option lets the user enter in new data
                        print("Please enter data as the last 1st of the month")
                        new_current_mon = input("Current month ##: ")
                        new_current_yr = input("Current year ##: ")
                        check_tot = input("Checking Acct Total as of {0}/01/{1} including cents: ".format(new_current_mon, new_current_yr))
                        save_tot = input("Savings Total as of {0}/01/{1} including cents: ".format(new_current_mon, new_current_yr)) 
                        new_current_tot = round((float(check_tot) + float(save_tot)),2)
                        last_mon = current_mon 
                        last_yr = current_yr 
                        last_tot = current_tot 
                        current_mon = new_current_mon 
                        current_yr = new_current_yr 
                        current_tot = new_current_tot 
                        count += 1 
                        
                        if count == 1: #First time entering data
                                first_tot = current_tot
                                first_mon = current_mon
                                first_yr = current_yr
                                try:
                                        file = open("_doc_my_budget_data.txt","w") 
                                        file.write(str("Current Month|{0}\n".format(current_mon))) #got
                                        file.write(str("Current Year|{0}\n".format(current_yr))) #got
                                        file.write("Current Total|{0}\n".format(current_tot)) #got
                                        file.write("Last Month|{0}\n".format(last_mon)) #is 0
                                        file.write("Last Year|{0}\n".format(last_yr)) #is 0
                                        file.write("Last Total|{0}\n".format(last_tot)) #is 0
                                        file.write("Total Saved Past Month|{0}\n".format(tot_save_mon)) #is 0
                                        file.write("Total Lost Past Month|{0}\n".format(tot_lost_mon)) #is 0
                                        file.write("Total Saved Over All|{0}\n".format(tot_save)) #is 0
                                        file.write("Total Lost Over All|{0}\n".format(tot_lost)) #is 0
                                        file.write("Cumulative Avg Saved/Month|{0}\n".format(cum_avg_save)) #is 0
                                        file.write("Cumulative Avg Lost/Month|{0}\n".format(cum_avg_lost)) #is 0
                                        file.write("Number of data entries|{0}\n".format(count)) #got
                                        file.write("First Total|{0}\n".format(first_tot)) #got
                                        file.write(str("First Month|{0}\n".format(first_mon))) #got
                                        file.write(str("First Year|{0}\n".format(first_yr))) #got
                                        print("Your new data has been added and new calculations have been done")
                                        print("If you want to view the new calculations, please select 'view'")
                                finally:
                                        file.close()
                                try:
                                        history = open("_doc_my_budget_history.txt","a")
                                        history.write("{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}\n".format(current_mon,current_yr,current_tot,tot_save_mon,tot_lost_mon,tot_save,tot_lost,cum_avg_save,cum_avg_lost))
                                        print('History Data Saved Successfully')
                                finally: #Close file
                                        history.close()
                                
                        else: #not the first time entering data
                                diff = round((float(current_tot) - float(last_tot)),2)
                                if diff > 0: #current_tot > last_tot
                                        tot_save_mon = diff
                                        tot_lost_mon = 0.00
                                elif diff < 0: #current_tot < last_tot
                                        tot_save_mon = 0.00
                                        tot_lost_mon = abs(diff)
                                elif diff == 0: #current_tot == last_tot
                                        tot_save_mon = 0.00
                                        tot_lost_mon = 0.00

                                full_diff = round((float(current_tot) - float(first_tot)),2)
                                if full_diff > 0: #current_tot > first_tot
                                        tot_save = full_diff
                                        tot_lost = 0.00
                                elif full_diff < 0: #current_tot < first_tot
                                        tot_save = 0.00
                                        tot_lost = abs(full_diff)
                                elif full_diff == 0: #current_tot == first_tot
                                        tot_save = 0.00
                                        tot_lost = 0.00

                                cum_avg_save = round((float(tot_save) / float(count)),2)
                                cum_avg_lost = round((float(tot_lost) / float(count)),2)
                                
                                try:
                                        file = open("_doc_my_budget_data.txt","w") 
                                        file.write(str("Current Month|{0}\n".format(current_mon))) #got
                                        file.write(str("Current Year|{0}\n".format(current_yr))) #got
                                        file.write("Current Total|{0}\n".format(current_tot)) #got
                                        file.write("Last Month|{0}\n".format(last_mon)) #got
                                        file.write("Last Year|{0}\n".format(last_yr)) #got
                                        file.write("Last Total|{0}\n".format(last_tot)) #got
                                        file.write("Total Saved Past Month|{0}\n".format(tot_save_mon)) #calculated
                                        file.write("Total Lost Past Month|{0}\n".format(tot_lost_mon)) #calculated
                                        file.write("Total Saved Over All|{0}\n".format(tot_save)) #calculated
                                        file.write("Total Lost Over All|{0}\n".format(tot_lost)) #calculated
                                        file.write("Cumulative Avg Saved/Month|{0}\n".format(cum_avg_save)) #calculated
                                        file.write("Cumulative Avg Lost/Month|{0}\n".format(cum_avg_lost)) #calculated
                                        file.write("Number of data entries|{0}\n".format(count)) #got
                                        file.write("First Total|{0}\n".format(first_tot)) #got
                                        file.write(str("First Month|{0}\n".format(first_mon))) #got
                                        file.write(str("First Year|{0}\n".format(first_yr))) #got
                                        print("Your new data has been added and new calculations have been done")
                                        print("If you want to view the new calculations, please select 'view'") 
                                finally:
                                        #Close file
                                        file.close()
                                try:
                                        history = open("_doc_my_budget_history.txt","a")
                                        history.write("{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}\n".format(current_mon,current_yr,current_tot,tot_save_mon,tot_lost_mon,tot_save,tot_lost,cum_avg_save,cum_avg_lost))
                                        print('History Data Saved Successfully')
                                finally: #Close file
                                        history.close()

                                   
        elif user_input == 'overwrite':
                print("Are you sure? Overwriting will delete all existing data. Input Y to continue or N to go back")
                overwrite_ans = input(": ")
                overwrite_ans = overwrite_ans.upper()
                if overwrite_ans == 'Y':
                        try: #Rewriting the variables file
                                file = open("_doc_my_budget_data.txt","w")
                                data = 0
                                file.write(str("Current Month|{0}\n".format(data)))
                                file.write(str("Current Year|{0}\n".format(data)))
                                file.write("Current Total|{0}\n".format(data))
                                file.write("Last Month|{0}\n".format(data))
                                file.write("Last Year|{0}\n".format(data))
                                file.write("Last Total|{0}\n".format(data))
                                file.write("Total Saved Past Month|{0}\n".format(data))
                                file.write("Total Lost Past Month|{0}\n".format(data))
                                file.write("Total Saved Over All|{0}\n".format(data))
                                file.write("Total Lost Over All|{0}\n".format(data))
                                file.write("Cumulative Avg Saved/Month|{0}\n".format(data))
                                file.write("Cumulative Avg Lost/Month|{0}\n".format(data))
                                file.write("Number of data entries|{0}\n".format(data))
                                file.write("First Total|{0}\n".format(data))
                                file.write(str("First Month|{0}\n".format(data)))
                                file.write(str("First Year|{0}\n".format(data)))
                        finally: #Close file
                                file.close()
                        
                        try: #Rewriting the historical data file
                                history = open("_doc_my_budget_history.txt","w")
                                history.write("Current Month|Current Year|Current Total|Total Saved Past Month|Total Lost Past Month|Total Saved Over All|Total Lost Over All|Cumulative Avg Saved Per Month|Cumulative Avg Lost Per Month\n")
                        finally: #Close file
                                history.close()
                        print("Any existing data has been removed and a new file was created.")
                elif overwrite_ans == 'N':
                        continue
                else:
                        print("Unknown input - taking you back to main menu")
                        
        elif user_input == 'quit':
                print("Are you sure you want to exit? Input Y to continue or N to go back")
                quit_ans = input(": ")
                quit_ans = quit_ans.upper()
                if quit_ans == 'Y':
                        break
                elif quit_ans == 'N':
                        continue
                else:
                        print("Unknown input - taking you back to main menu")
        
        else:
                print("Unknown input")




