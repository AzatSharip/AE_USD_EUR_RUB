import courses
import best_courses
import subprocess
import os
import datetime
import shutil


def write_data():
    with open("data.txt", 'w') as file:
        #file.write('var comp1 = ["на {}","{}","{}","{}","{}"];'.format(courses.date, courses.doll_val, courses.doll_dynamics, courses.euro_val, courses.euro_dynamics) + '\n')
        file.write('var comp1 = ["на сегодня","{}","{}","{}","{}"];'.format(courses.doll_val, courses.doll_dynamics, courses.euro_val, courses.euro_dynamics) + '\n')
        file.write('var doll_minus = ["{}"];\nvar euro_minus = ["{}"];'.format(courses.doll_arrow, courses.euro_arrow) + '\n')
        file.write('var comp_doll = ["{}","{}","{}","{}"];'.format(best_courses.doll_buy, best_courses.doll_buy_b, best_courses.doll_sale, best_courses.doll_sale_b) + '\n')
        file.write('var comp_euro = ["{}","{}","{}","{}"];'.format(best_courses.euro_buy, best_courses.euro_buy_b, best_courses.euro_sale, best_courses.euro_sale_b) + '\n')

def write_prop_to_bat():
    with open("runer.bat", 'w') as file:
        file.write('chcp 1251\n"C:\Program Files\Adobe\Adobe After Effects CC 2018\Support Files\\aerender.exe" -project D:\Personal\GitHub\AE\Courses\get_courses.aep -comp KURSI -OMtemplate KURSI -output D:\Personal\GitHub\AE\Courses\\render\KURSI_[#####].png')

def bat_run():
    program = "runer.bat"
    process = subprocess.Popen(program)
    exit_code = process.wait()

    if exit_code == 0:
        print("Success!")
    else:
        print("Error!")

def make_dir():
    today = datetime.datetime.today()
    year = today.strftime("%Y")
    day = today.strftime("%d")

    month = today.strftime("%m")
    month_dict = {'01':'январь', '02':'февраль', '03':'март', '04':'апрель', '05':'май', '06':'июнь', '07':'июль', '08':'август', '09':'сентябрь', '10':'октябрь', '11':'ноябрь', '12':'декабрь'}
    for keys in month_dict:
        if month == keys:
            month = month_dict[keys]

    global path_in_office
    path_in_office = 'O:\\Графика на эфир\\{}\\{}\\{}'.format(year, month, day)
    try:
        os.makedirs(path_in_office, exist_ok=True)
    except:
        pass


def teleport_files():
    for rootdir, dirs, files in os.walk("D:\Personal\GitHub\AE\Courses\\render"):
        for file in files:
            shutil.copy("D:\\Personal\\GitHub\\AE\\Courses\\render\\" + file, str(path_in_office))
            print("D:\\Personal\\GitHub\\AE\\Courses\\render\\" + file, str(path_in_office))


write_data()
print('Data.txt recorded successfully!')
write_prop_to_bat()
bat_run()
make_dir()
teleport_files()