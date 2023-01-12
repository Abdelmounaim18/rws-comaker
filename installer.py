import os
import socket
from sys import platform
from art import *

db_root_pw = "Rijkswaterstaat2022"

if platform == "linux" or platform == "linux2":
    os.system("sudo apt install python3-pip")
    os.system("sudo pip install art")
    os.system("clear")
    Art = text2art("rws dashboard - Installer")
    print(Art)
    print("-+-+- This script will transform your Flask Application into a docker container -+-+-\n\n")
    # print("Proceed with installation (y/n)")
    type_text = input("Specify installation type (install/ update): ")

    if type_text == "install":
        input_text = input("Proceed with installation (y/n): ")
        if input_text == "y" or input_text == "yes":
            print("\n\n")
            os.system("docker -v")
            os.system("sudo docker build -t rws-dashboard:latest .")

            install_mariadb = input("\nDo you want to install mariaDB? You will need this in order to run this application (y/n): ")
            if install_mariadb == "y" or install_mariadb == "yes":
                os.system(f"sudo docker run --name mariadb-rws -e MYSQL_ROOT_PASSWORD={db_root_pw} -p 3306:3306 -d mariadb:latest")
                print("\nSuccessfully installed container 'mariaDB'")
            else:
                print("Skipping installation of mariaDB")
            while True:
                try:
                    input_num = int(input("\nPlease specify on which port rws dashboard should be accessible: (eg.: 5000) "))
                    if input_num is None:
                        input_num = 5000
                    if os.system(f"sudo lsof -i:{input_num}") == 256:
                        os.system(f"sudo docker run --name=rws-dashboard -it -d -p {input_num}:5000 rws-dashboard:latest")
                        print("\nSuccessfully installed container 'rws-dashboard'")
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect(("1.1.1.1", 80))
                        local_ip = s.getsockname()[0]

                        print(f"Head over to -> http://{local_ip}:{input_num}/docs <- to access the API!")
                        break
                    else:
                        print("\nPort is already in use, please try a different one")
                except ValueError:
                    print("\nEnter a port number between 1 and 65535...")
                    continue
        else:
            print("Install aborted")

    elif type_text == "update":
        input_text = input("Proceed with update (y/n): ")
        if input_text == "y" or input_text == "yes":
            print("\n\n")
            os.system("docker -v")
            os.system("sudo docker build -t rws-dashboard:latest .")
            os.system("sudo docker stop rws-dashboard")
            print("\n### removing previous version... ###")
            os.system("sudo docker rm rws-dashboard")

            install_mariadb = input("\nDo you want to re-install mariaDB? (y/n): ")
            if install_mariadb == "y" or install_mariadb == "yes":
                print("\n### removing previous version... ###")
                os.system("sudo docker stop mariadb-rws")
                os.system("sudo docker rm mariadb-rws")
                os.system(f"sudo docker run --name mariadb-rws -e MYSQL_ROOT_PASSWORD={db_root_pw} -p 3306:3306 -d mariadb:latest")
                print("\nSuccessfully re-installed container 'mariaDB'")
            else:
                print("Skipping installation of mariaDB")
            while True:
                try:
                    input_num = int(input("\nPlease specify on which port rws dashboard should be accessible: (eg.: 5000) "))
                    if input_num is None:
                        input_num = 5000
                    if os.system(f"sudo lsof -i:{input_num}") == 256:
                        os.system(
                            f"sudo docker run --name=rws-dashboard -it -d -p {input_num}:5000 rws-dashboard:latest")
                        print("\nSuccessfully updated container 'rws-dashboard'")
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect(("1.1.1.1", 80))
                        local_ip = s.getsockname()[0]

                        print(f"Head over to -> http://{local_ip}:{input_num}/docs <- to access the API!")
                        break
                    else:
                        print("\nPort is already in use, please try a different one")
                except ValueError:
                    print("\nEnter a port number between 1 and 65535...")
                    continue
        else:
            print("Update aborted")
    else:
        print("\nInvalid option, aborting...\n")

else:
    print("You can only run this script on linux (recommended: Ubuntu) based Operation Systems!")

