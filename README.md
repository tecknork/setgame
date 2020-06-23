
# README Sets Game 

### Files 

 - pyproject.toml 
    
     we can define black formatting types in this file. 
 - .flake8 
 
     configurations for flake8.  
     flake8 is a linting tool which checks for code errors and provides ways to 
     improve code style .
     
## TODO LIST 
  - [X] Create Basic ReadMe File
  - [ ] Install pycharm in your computer
  - [ ] Add conda create and activate enviroment command in ReadMe
  - [X] Add images to a folder named images at root of the project. 
  - [ ] Add database run script command
     ```
           python manage.py migrate  
     ```
        This command will create a database table in mongoDB where all the metadata 
        infromation of card will be stored
  - [ ] Create Draw N number of Cards command       
     ```
           python manage.py drawcard -n 12 
     ```
           
  - [ ] Create Check Valid Set Command 
     ```bash
        python manage.py checkset -c 1,10,20 
     ``` 
 

### Install Instruction 

- create new conda environment 
- activate conda evviroment 
- run the following command 
```
    pip install -r requirements.txt;
```
- set enviroment variable 
  ```bash
    export FLASK_APP=manage.py
   ``` 
- run commands 

   ```
   flask migrate 
   flask checkcards -c 12 -c 13 -c 15 
   flask drawcards --cards 12
   ```
  
### Linting and Formatting 

- install requirments-dev.txt file 
- using ./scripts/formatting.sh to fix any linting and formatting errors



