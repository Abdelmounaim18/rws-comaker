
# RWS Datalab Dashboard

The dashboard to monitor all the roads in NL.

## Requirements

_TLDR;_
_You can also run this project locally in case the docker deployment is not working properly (see last step)._

This project requires you to have docker pre-intsalled and running on the latest version.
To check if docker is installed run this command in your terminal

```bash
docker -v

---
$ Docker version 20.10.16, build aa7e414
```

If you dont have docker installed on your ubuntu system, head over to the [Docker Docs](https://docs.docker.com/desktop/linux/install/ubuntu/)  for the installation procedure.


Next! You also need to have Python3 installed on your system.
To check if Python is installed run this command in your terminal
```bash
python3 --version

---
$ Python 3.8.10
```

If you dont have Python3 installed on your ubuntu system, follow these steps below
```bash
  $ sudo apt update -y
  $ sudo apt full-upgrade -y
  $ sudo apt install python3 -y
```
## Installation



Step 1: \
Unzip and open directory

```bash
  $ sudo apt update -y
  $ sudo apt full-upgrade -y
  $ unzip RWS_Datalab_Dashboard.zip
  $ cd RWS_Datalab_Dashboard
```

Step 2: \
Install by running the python script  
The script will guide you throughout the installation!


```bash
  $ python3 installer.py
```

_When running the script for the first time, the installation type needs to be ```install```_

Step 3: \
For this project you'll need to have mariaDB installed on your system. The script allows you to pre-install mariaDB. If you already have mariaDB installed on your system, you can skip this step.

```bash
  Do you want to install mariaDB? You will need this in order to run this application (y/n): 
```
The default root password for mariadb is ```Rijkswaterstaat2022```. If you want to change this, you can do so by editing the variable ```db_root_pw``` on line 6 in the ```installer.py``` file. 
When doing so, make sure to also adjust the ```db_connection``` dict in the ```__init__.py``` file in the working directory.

> Make sure to re-run the script and using the install-type ```update``` for the changes to take effect!

Step 4: \
Specifiy on which port the container should run

```bash
  Please specify on which port RWS Dashboard should be accessible: x
  default=5000
```

Step 5: \
If no errors showed up, you should be greeted with this message 

```bash
  Successfully installed container 'rws-dashboard'
  Head over to -> http://[SERVER_IP]:[PORT]/docs <- to access the API!
```


## Updating


Updating is just as easy as the installation!

Step 1: \
Unzip and open directory

```bash
  $ sudo apt update -y
  $ sudo apt full-upgrade -y
  $ unzip RWS_Datalab_Dashboard.zip
  $ cd RWS_Datalab_Dashboard
```

Step 2: \
Update by running the python script again.


```bash
  $ python3 installer.py
```

_This time the installation type needs to be ```update```_

Step 3: \
You will get the option to re-install mariaDB in case of any issues.  If you don't want to re-install mariaDB, you can skip this step.

```bash
  Do you want to re-install mariaDB? (y/n): 
```

Step 4: \
Updating will remove the previous container and replace it with a newer version.
Now specify on which port the container should run:

```bash
  Please specify on which port RWS Dashboard should be accessible: x
  default=5000
```

Step 5: \
If no errors showed up, you should be greeted with this message

```bash
  Successfully updated container 'rws-dashboard'
  Head over to -> http://[SERVER_IP]:[PORT]/docs <- to access the API!
```




## View Dashboard

Step 1: \
With your Grafana instance open; head over to __Plugins__ and install [JSON API](https://grafana.com/grafana/plugins/marcusolsson-json-datasource/) 

Head over to the __Data Sources__ tab, add a new data source and select __JSON API__ as the type.
In the __URL__ field, enter the following: ```http://[SERVER_IP]:[PORT]/```. 
>![plugin_settings.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Ft7%2Fx9vwhr8j2gvd_vsgmrp424zc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_atCTSf%2FScherm%C2%ADafbeelding%202023-01-12%20om%2011.47.12.png)

Step 2: \
Open the __Dashboards tab > settings icon > JSON Model__ and import the dashboard from the ```./dashboard/grafana.json``` file. \
You should now be able to see the dashboard!
>![grafana_dashboard.png](..%2F..%2F..%2FDesktop%2FScherm%C2%ADafbeelding%202023-01-12%20om%2011.52.38.png)


