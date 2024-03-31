import subprocess

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)

def input_setup(name):
    execute_command("hadoop fs -mkdir -p /inputs/")
    execute_command(f"hadoop fs -put /home/{name}/Documents/inputq.txt /inputs/inputq.txt")

def run_task_1(name):
    execute_command(f"hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar -input /inputs/input.txt -output /inputs/output8 -mapper mapper.py -reducer reducer.py -file /home/{name}/Documents/mapper.py -file /home/{name}/Documents/reducer.py")

def format_output(output):
    execute_command(f"hadoop fs -cat /inputs/output{output}/part-00000 > /inputs/output{output}.txt")


def run_task(mapper, reducer, output, inp, name):
    execute_command(f"hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar -input /inputs/output{inp}.txt -output /inputs/output{output} -mapper mapper{mapper}.py -reducer reducer{reducer}.py -file /home/{name}/Documents/mapper{mapper}.py -file /home/{name}/Documents/reducer{reducer}.py")

def display(output):
    execute_command(f"hadoop fs -cat /inputs/output{output}/part-00000")

def take_user_query():
    inp = input("Search : ")
    return inp

def write_string_to_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def concatenate_with_string(input_file, output_file, string_to_concatenate):
    with open(input_file, 'r') as f:
        file_content = f.read()

def similarity(name):
    execute_command(f"hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar -input /inputs/output5.txt /inputs/output10.txt -output /inputs/output11 -mapper mapper7.py -reducer reducer7.py -file /home/{name}/Documents/mapper7.py -file /home/{name}/Documents/reducer7.py")

#make input file
inp = take_user_query()
file_path = '/home/aliza/Documents/inputq.txt'
write_string_to_file(file_path, inp)

#providing input
input_setup('aliza')  #enter username

#running map-reduce
run_task_1('aliza')
format_output('8')
run_task('1','1','7','6', 'aliza')  #enter username
format_output('2')
run_task('2','2','8','7','aliza')   #enter username
format_output('3')
run_task('3','3','9','8','aliza')  #enter username
format_output('4')
run_task('4','4','10','9','aliza')  #enter username

format_output('10')
similarity('aliza')

format_output('11')
run_task('6','6','12','11','aliza')  #enter username

format_output('12')

display('12')

