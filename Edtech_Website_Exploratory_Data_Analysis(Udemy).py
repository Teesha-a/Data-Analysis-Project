import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r".\udemy_courses.csv")


# **************DISPLAYING DATASET HAVING INFO ABOUT COURSES PROVIDED BY UDEMY*******************
print(df.to_string())


#************** DISPLAYING FEW RECORDS FROM TOP OF DATASET *******************
print("\n                                   ****** FEW RECORDS FROM DATASET STARTING FROM TOP *********                      \n")
print(df.head(7).to_string())


# **************FINDING SHAPE OF OUR DATASET (prints total no. of  rows and colums) ***************
print(" \n      --------------TOTAL ROWS & TOTAL COLUMNS--------------      ")
print("\n","   Total Rows in this Dataset are : ",df.shape[0],"\n", "   Total Columns in this Dataset are : ",df.shape[1])


#**************GETTING BASIC INFORMATION ABOUT OUR DATASET (Rows, Columns, Datatypes, Memory Requirement) ****************
print(df.info())


#*************DISPLAYING ALL THE COLUMN NAMES OF OUR DATASET**************
print("\n------------|| Column Names ||-----------\n")
print(df.columns)


#***************CHECKING FOR NULL VALUES***********
print("\n------||  Checking for Null Values||  ------\n")
print("Any Missing Values ?!!",df.isnull().values.any())


#***************CHECKING DUPLICATE DATA**************
print("Is there any Duplicate Value in our Data ?!! \n",df.duplicated().any(),df.duplicated().sum())

#RUNNING COMMAND TO DROP DUPLICATE VALUES IN DATA
df=df.drop_duplicates()

#RECHECKING DUPLICATE VALUES
print("Is there still any Duplicate Value in our Data ?!! \n",df.duplicated().any(),df.duplicated().sum())


# ******************NUMBER OF COURSES PER SUBJECT***************
sub = df['subject'].value_counts()
print(sub)

# NUMBER OF COURSES PER SUBJECT IN GRAPH FORM
plt.xlabel(" <------------------------Subject------------------------->")
plt.ylabel(" <--------------Number of Courses----------------->")
plt.title("|| Number of Courses Per Subject ||")
plt.bar(sub.index,sub.values,width=0.35)
plt.xticks(fontsize=8)
plt.show()


#**************NUMBER OF COURSES PER LEARNING LEVEL (All, Beginner, Intermediate, Advance) *****************
level = df['level'].value_counts()
print(level)

#NUMBER OF COURSES PER LEVEL IN GRAPH FORM
plt.xlabel(' <----------------Levels-------------->')
plt.ylabel(' <-----------------Number of Courses----------------->')
plt.title("|| Number of Courses per Level ||")
plt.bar(level.index,level.values,width=0.35)
plt.xticks(fontsize=10)
plt.show()


#******************* COUNT  OF FREE & PAID COURSES *****************
paid_courses=df['is_paid'].value_counts()
print(paid_courses)

# DATA OF FREE & PAID COURSES IN PIE CHART FORMAT
label = ['Paid', 'Free']
plt.pie(paid_courses.values,labels=label,autopct='%0.2f%%', shadow=True, explode=[0,0.2])
plt.title("Data of Free & Paid Users")
plt.show()


# ********************COURSES WITH HIGHER NUMBER OF USERS***************

# COURSES WITH HIGHER NUMBER OF USERS WHETHER PAID OR FREE
num_sub=df.groupby('is_paid')['num_subscribers'].sum().sort_values(ascending=False)
print(num_sub)

#**COMPARISON OF USERS BETWEEN PAID AND FREE IN PIE CHART FORMAT**
label = ['Paid', 'Free']
plt.pie(num_sub.values,labels=label,autopct='%0.2f%%', shadow=True, explode=[0,0.1])
plt.title("|| Comparison Between Free & Paid Users ||")
plt.show()


# *********************COURSES WITH HIGHEST NUMBER OF USERS AS PER LEVELS****************
level_sub=df.groupby('level')['num_subscribers'].sum().sort_values(ascending=False)
print(level_sub)

# COURSES WITH HIGHEST NUMBER OF USERS AS PER LEVELS IN PIE FORMAT
plt.pie(level_sub.values,labels=level_sub.index,autopct='%0.1f%%', explode=[0,0,0,0.2])
plt.title("|| USERS OF EACH LEVEL ||")
plt.show()


# ***************MOST POPULAR COURSES AS PER NUMBER OF SUBSCRIBERS****************
print("\n             -----------MOST POPULAR COURSES AS PER NUMBER OF SUBSCRIBERS--------------\n")
top_20=df.sort_values(by='num_subscribers', ascending=False).head(20)
print(top_20.to_string())

# MOST POPULAR COURSES AS PER NUMBER OF SUBSCRIBERS IN GRAPH
x=top_20['course_title']
y=top_20['num_subscribers']
plt.ylabel('<---------------------Course Title-------------------->')
plt.xlabel('<------------------Number of Subscribers------------------>')
plt.title('Most Popular Courses As Per Number of Subscribers')
plt.barh(x,y)
plt.yticks(fontsize=7)
plt.grid(True)
plt.show()

# LEAST POPULAR COURSES AS PER NUMBER OF SUBSCRIBERS
print("\n\n            -----------LEAST POPULAR COURSES AS PER NUMBER OF SUBSCRIBERS--------------\n")
bottom_20=df.sort_values(by='num_subscribers', ascending=False).tail(20)
print(bottom_20.to_string())


# *********************NUMBER OF COURSES RELATED TO PYTHON********************
print("\n\n--------------|| NUMBER OF COURSES RELATED TO PYTHON ||---------------\n")
python_courses=df['course_title'].str.contains('Python', case=False).sum()
print("Total Number of Courses Related to Python are : ",python_courses)

#MOST POPULAR PYTHON COURSES
python_TopCourses = df[df['course_title'].str.contains('Python',case = False)].sort_values(by='num_subscribers', ascending=False).head(10)
print("\n\n--------------|| MOST POPULAR PYHTON COURSES ||---------------\n")
print("\n",python_TopCourses.to_string())

# MOST POPULAR PYTHON COURSES IN GRAPH
x=python_TopCourses['course_title']
y=python_TopCourses['num_subscribers']
plt.ylabel('<---------------------Courses Related To Python-------------------->')
plt.xlabel('<------------------Number of Subscribers------------------>')
plt.title('Most Popular Python Courses As Per Number of Subscribers')
plt.barh(x,y)
plt.yticks(fontsize=7)
plt.grid(True)
plt.show()


