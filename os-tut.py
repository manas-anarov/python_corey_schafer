import os
from  datetime import datetime


# import os
# print(os.getcwd())


# import os
# print(os.getcwd())
# os.chdir('/home/samuray/django_pro/')
# print(os.getcwd())

# import os

# os.chdir('/home/samuray/django_pro/')
# print(os.listdir())

# import os

# os.chdir('/home/samuray/django_pro/')
# # os.mkdir('OS-Demo-2')
# os.rmdir('OS-Demo-2/subdir-1')
# os.makedirs('OS-Demo-2/subdir-1')



# import os

# os.chdir('/home/samuray/django_pro/')
# # os.mkdir('OS-Demo-2')
# os.rmdir('OS-Demo-2/subdir-1')
# os.removedirs('OS-Demo-2/subdir-1')
# print(os.listdir())



# os.chdir('/home/samuray/django_pro/')

# os.rename('OS-Demo-2', 'new')
# print(os.listdir())



# os.chdir('/home/samuray/django_pro/')

# # os.rename('OS-Demo-2', 'new')
# print(os.listdir('/home/samuray/django_pro/'))


# from  datetime import datetime

# os.chdir('/home/samuray/django_pro/')

# mod_time = os.stat('/home/samuray/django_pro/').st_mtime

# print(datetime.fromtimestamp(mod_time))



# from  datetime import datetime

# os.chdir('/home/samuray/django_pro/tutorial_pro')

# for dirpath, dirnames, filenames in os.walk('/home/samuray/django_pro/tutorial_pro'):
# 	print('Path', dirpath)
# 	print('Dirs', dirnames)
# 	print('Files', filenames)
# 	print()




# os.chdir('/home/samuray/django_pro/tutorial_pro')
# # print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), 'text.txt')
# print(file_path)




# os.chdir('/home/samuray/django_pro/tutorial_pro')

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))


# os.chdir('/home/samuray/django_pro/tutorial_pro')

# print(os.path.exists('/tmp/test.txt'))


# os.chdir('/home/samuray/django_pro/tutorial_pro')

# print(os.path.isfile('/tmp/test.txt'))


# os.chdir('/home/samuray/django_pro/tutorial_pro')

# print(os.path.splitext('/tmp/test.txt'))


os.chdir('/home/samuray/django_pro/tutorial_pro')

print(dir(os.path))