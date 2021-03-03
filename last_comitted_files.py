import subprocess

out = subprocess.check_output('git show --name-only', shell=True)
#out=out.split('\n')
print '----------'
print out
#if 'bc8n54M32k' in out:
#    print 'File bc8n54M32k was found.'
#if 'bc8n856M1k' in out:
#    print 'File bc8n856M1k was found.'
