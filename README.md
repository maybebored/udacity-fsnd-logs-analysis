# Udacity Full Stack Nanodegree Project 3 - Logs Analysis
Submission for [Udacity's Full Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)'s Logs Analysis Project. The project tests SQL skills learnt in Section 3 of the nanodegree. 

## Project Purpose
The program written in *logs_analysis.py* will query a *News* database to answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Get Started

Follow these steps to run the project. You must use a terminal (command line interface):

### Set up the virtual machine
1. **Install VirtualBox**
    
    You can [download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system.

2. **Install Vagrant**
    
    Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com.](https://www.vagrantup.com/downloads.html) Install the version for your operating system.

3. **Download the VM Configuration**
    
    Fork and clone the  [Fullstack Nanodegree VM Repo](https://github.com/udacity/fullstack-nanodegree-vm). Open up your terminal and then `cd` into the directory. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory. 
    
    [*How to Fork a Repository*](https://help.github.com/articles/fork-a-repo/)

4. **Start the virtual machine**
    
    From inside the **vagrant** directory run the following command:
    ```bash
    vagrant up
    ```
    After that is completed run the following command to login to the virtual machine:
    ```bash
    vagrant ssh
    ```
### Prepare database and run queries    
5. **Download the data**
    
    Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called *newsdata.sql*. Put this file into the vagrant directory, which is shared with your virtual machine.
    To load the data, go into the vagrant directory and enter the command:
    
    ```bash
    psql -d news -f newsdata.sql
    ```
6. **Download the code**
    
    Clone this repository to the vagrant directory. Go into the directory and then run:
    ```python
    python logs_analysis.py
    ```

    This should print the results on the terminal.