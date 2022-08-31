import os



a = os.getcwd()

os.chdir(f'{a}\\jstools')
os.system('npm run build')




# BASE_DIR = os.getcwd() # get current file path

# base_dir_list = BASE_DIR.split('\\')
# last = base_dir_list[-1]
# print(last)

# # os.system('cd ..')
# def cd_b():
#     m = os.getcwd()
#     n = m.rfind("\\")
#     d = m[0: n+1]
#     os.chdir(d)
#     print(os.getcwd())

# cd_b()
# a = os.getcwd()
# os.chdir(f'{a}\\env')
# os.chdir(f'{a}\\Scripts')
# os.system('activate')
# cd_b()
# cd_b()
# os.chdir(f'{a}\\{last}')
# os.chdir(f'{a}\\jstools')
# os.system('npm run build')

# print(os.getcwd())


# os.system('activate')
# os.system('cd ../..')
# os.system(f'cd {last}')
# os.system('cd jstools')
# os.system('npm run build')


# os.environ


# print(os.getcwd())