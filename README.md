# Census Management System

### 1. Introduction

* This Census Management system aims to digitalize the process of Census Data Entry, summarization and individual data lookup. 
* The existing system is nothing but a manual system in which the admin has to fill the citizen’s data in a written form and then manually entering in the computers later. 
* It is a tedious work to merge the data of all citizens obtained by various  administrators without any redundancy or information loss.
* This project helps to reduce errors and mishandling of data while minimizing mannual data entry and time.

### 2. Proposed System

The proposed System has three main utilities : 
* Data Summarization (ADMIN View) : Admins canview the summary of all collected data in detailed manner.
* Data Insertion (ADMIN View) : Admins can only enter data in the database while taking help from existing AADHAR data.
* Data Viewing (Citizen View) : Citizens can view their data by entering their registration number and AADHAR Number.

### 3. ER Diagram of the Database/System :
<p align =center>
<img width="800" alt="ER Diagram" src="https://user-images.githubusercontent.com/98400026/226265424-8ebb1270-26a4-46fc-bc8e-ed4383fe7a2f.png">
</p>

### 4. Schema Diagram of the Database : 
<p align =center>
<img width="800" alt="Schema Diagram" src=https://user-images.githubusercontent.com/98400026/226266117-e03eca4f-e180-4dc7-9625-67efbd6767d2.png>
</p>  

### 5. Relationship Analysis :

There is only one primary key in each table and they are the only ones that satisfy each record in the table. There is no partial functional dependency and neither transitive functional dependency. Thus, the relations are in BCNF.

### 6. Results
<p align="center">
<h3>Unified Login Page of Admin and Citizen</h3>
<img width="600" alt="Login Page" src=https://user-images.githubusercontent.com/98400026/226266825-017e25df-5063-4eaa-9e22-ef686224cae6.png>
<h3>Dashboard for Admin</h3>
<img width="600" alt="Admin_Dashboard" src=https://user-images.githubusercontent.com/98400026/226266859-3cd995c9-4ff6-4785-9792-8c76099302d7.png>
<h3>Summary Page Viewable by Admin</h3>
<img width="600" alt="Schema Diagram" src=https://user-images.githubusercontent.com/98400026/226267012-d2eb696d-f31a-43b0-92a5-ad5861a86cfd.png>
<h3>Data Insertion Page of Admin<h3>
<img width="600" alt="Schema Diagram" src=https://user-images.githubusercontent.com/98400026/226266908-5732148b-9a7d-413d-af6a-9eccb12db437.png>
<h3>Data Viewing page of Citizen</h3>
<img width="600" alt="Schema Diagram" src=https://user-images.githubusercontent.com/98400026/226268850-ac818553-fcb1-4cf8-af98-e517d1f68e91.png>
</p>  
  
### 7. Future Scope
* Improving the UI of app
* Converting the app into WebApp
