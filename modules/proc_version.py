
def parser(stdout, stderr):
    output = {}
    if stdout:
        output = stdout.strip()

    return {'output': output}

def register(main):
    main['proc_version'] = {
        'cmd': 'cat /proc/version',
        'description': 'Version of the Linux kernel, the version of gcc used to compile the kernel, and the time of kernel compilation',
        'parser': parser
    }