import subprocess

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)

def input_setup_name(name):
    execute_command("hadoop fs -mkdir -p /inputs/")
    execute_command(f"hadoop fs -put /home/{name}/Documents/input.txt /inputs/input.txt")

def run_task_1(name):
    execute_command(f"hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar -input /inputs/input.txt -output /inputs/output1 -mapper mapper.py -reducer reducer.py -file /home/{name}/Documents/mapper.py -file /home/{name}/Documents/reducer.py")

def format_output(output):
    execute_command(f"hadoop fs -cat /inputs/output{output}/part-00000 > /inputs/output{output}.txt")


def run_task(mapper, reducer, output, inp, name):
    execute_command(f"hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar -input /inputs/output{inp}.txt -output /inputs/output{output} -mapper mapper{mapper}.py -reducer reducer{reducer}.py -file /home/{name}/Documents/mapper{mapper}.py -file /home/{name}/Documents/reducer{reducer}.py")

def display(output):
    execute_command(f"hadoop fs -cat /inputs/output{output}/part-00000")

#providing input
input_setup_name('aliza')  #enter username

#running map-reduce
run_task_1('aliza')
format_output('1')
run_task('1','1','2','1', 'aliza')  #enter username
format_output('2')
run_task('2','2','3','2','aliza')   #enter username
format_output('3')
run_task('3','3','4','3','aliza')  #enter username
format_output('4')
run_task('4','4','5','4','aliza')  #enter username
format_output('5')

display('5')
