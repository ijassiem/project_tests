import subprocess

out = subprocess.check_output('git show --name-only', shell=True)
#out=out.split('\n')
# print '----------'
# print out
if 'hi.py' in out:
    print 'hi.py is found to be the last committed file.'
else:
  print 'hi.py not found.'
#if 'bc8n856M1k' in out:
#    print 'File bc8n856M1k was found.'
