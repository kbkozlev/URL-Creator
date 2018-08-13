#created by Kaloian Kozlev on 10.08.2018

import replit
import time


def welcome():
    choice = 0
    while choice <= 4:
        print(
            "\nWelcome to URL Generator \n------------------------ \n\n1.Direct      2.Indirect\n3.Console              \n\n4.Exit "
        )

        try:
            choice = int(input("\nSelect URL generator: "))
            if choice == 1:
                cid = str(input("\nPlease enter the CID: "))
                rid = int(input("Please enter the RID: "))
                pid = int(input("Please enter the PID: "))
                print("\nhttps://bda.bookatable.com/?cid=" + cid + "&rid=" +
                      str(rid) + "&pid=" + str(pid) + "&lang=en-GB")

            elif choice == 2:
                rid = int(input("\nPlease enter the RID: "))
                pid = int(input("Please enter the PID: "))
                print(
                    "\nhttps://bda.bookatable.com/?cid=INTL-LBDIRECTORY_INDIRECT:10508&rid="
                    + str(rid) + "&pid=" + str(pid) + "&lang=en-GB")
            elif choice == 3:
                rid = int(input("\nPlease enter the RID: "))
                pid = int(input("Please enter the PID: "))
                print(
                    "\nhttps://bda.bookatable.com/?cid=CONSOLEEMAILCAMPAIGNS:18663&rid="
                    + str(rid) + "&pid=" + str(pid) + "&lang=en-GB")
            elif choice == 4:
                replit.clear()
                print("\n\nProgram terminated")
                return
            else:
                print("\nWrong selection, please choose options 1-4")
                time.sleep(2)
                replit.clear()
                welcome()

            end = input("\nWould you like to continue Y/N ")
            if end == "y":
                replit.clear()
            if end == "n":
                replit.clear()
                print("\n\nProgram terminated")
                return
            elif end == "":
                replit.clear()
                print("\n\nProgram terminated")
                return

        except ValueError:
            print("\nPlease enter a number!")
            time.sleep(1)
            replit.clear()


welcome()
