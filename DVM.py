import csv
import mysql.connector
import openpyxl
d="what"
day_time=[]
def MYSQL_DB():
    database = {'host': 'local_host','user': 'user','password': '5656','database': 'DVM',}
    connection=mysql.connector.connect(database)
    cursor=connection.cursor()
    create_table= "(CREATE TABLE IF NOT EXISTS Course (EXAMDATES VARCHAR(225),INSTRUCTOR_NAME VARCHAR(225),SECTION VARCHAR(225), SECTIONTYPE VARCHAR(225)"
    cursor.execute(create_table)
    insert_data="(INSERT INTO CREATE_TABLE(EXAMDATES,INSTRUCTOR_NAME,SECTION,SECTIONTYPE) VALUES ({},{},{},{}))".format(d,d,d,d)
    connection.commit()
    connection.close()



password=5656

class Course:

    def __init__(self,examdates,instructor,sections=[],sectiontype=[]):
        self.examdates=examdates  #string
        self.instructor=instructor
        self.sections = list(sections)
        self.sectiontype=list(sectiontype)

    def __str__(self):
        return "{}-{},{},{}".format(self.examdates,self. instructor,self.sections,self.sectiontype)

    def get_all_sections(self,sec,sect):
        self.sections.append(sec)
        self.sectiontype.append(sect)
    def populate_section(self,pas,sec,sect):
        if(pas==password):
            if(sec not in self.sections):
                (self.sections).append(sec)
                self.sectiontype.append(sect)
            else:
                print("Already a section")
        else:
            print("error")


class Sections(Course):



    def __init__(self, examdates, instructor,sections=[],sectiontype=[],main_class={}):

        Course.__init__(self,examdates, instructor,sections=[],sectiontype=[])
        self.main_class = dict(main_class)



    def Clash(self,main_class={}):
        print("Showing you all different tut/lab/lectures in this course")
        print("If this is your tut/lab/lecture enter the respective details else leave blank")
        n=""
        lst=[]
        for i,j in zip(self.sections,self.sectiontype):



            while True:
                print("Section: ", i, j, " ")
                n = input("Enter Day and Time of the above class:(in the format day_time)(time-12:00am)")


                if (n not in day_time):
                    day_time.append(n)
                    break
                else:
                    print("this date time has already been used")
        for i,j,l,m in zip(self.sections,self.sectiontype,self.instructor,day_time):
            main_class.update({l:i+j+m})
class TimeTable(Course):
    lst=[]
    def __int__(self, examdates, instructor,sections=[],sectiontype=[],main_class={}):
        Course.__init__(self, examdates, instructor, sections=[], sectiontype=[],main_class={})
    def Show_Section(self):
        print("hi")
        for i,j,k in zip(self.sections,self.sectiontype,day_time):
            print("hi")
            print("Available Sections: ",i+j)
            print("Available on: ",k)

    def enroll_subject(self,sec,sect,day_tim):
        self.lst.append(sec)
        self.lst.append(sect)
        self.lst.append(day_tim)
    def check_clashes(self):

        with open(r"C:\Users\Admin\Documents\csv_store_tt.txt", newline="") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if(row[2]==self.lst[2]):
                    print("There already exists a class at this time")
                    print("Please enroll subject at another time")
                else:


                    print("please function call export_to_csv function")
    def export_to_csv(self): #one by one for all subjects
        with open(r"C:\Users\Admin\Documents\csv_store_tt.txt","w", newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(self.lst)


meow=Sections("26/11/2023","Debs")
meow.get_all_sections("t1","lab")
meow.get_all_sections("t2","lab")
meow.get_all_sections("t3","lab")
meow.get_all_sections("t4","lab")
print(meow.Clash())
meow=TimeTable("26/11/2023","Debs")
print(meow.Show_Section())

#print(meow.populate_section(5656))
sec=""
sect=" "



