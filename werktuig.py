#!/usr/bin/python
import os, sys
from optparse import OptionParser
from ConfigParser import ConfigParser

DEFAULT_COMMANDS = {
    'svn update' : 'svn update',
    'update' : 'svn update',
    'up' : 'svn update',
    'u' : 'svn update',
    'svn commit' : 'svn commit',
    'commit' : 'svn commit',
    'c' : 'svn commit',
}

def configuration_editor_run(configuration):
    while True:
        command = raw_input('Command: ')
        if command == 'exit':
            break
        elif command == 'add':
            print add
        elif command == 'write':
            print 'write'
        elif command == 'help':
            print 'help'

def load_configuration(conf):
    conf = "%s/%s" % (os.getenv('HOME'), conf)
    config = ConfigParser()
    config.read(conf)

    configuration = {
        'projects' : {},
        'config' : conf
    }
    for section in config.sections():
        configuration['projects'][section] = {}
        for option in config.options(section):
            configuration['projects'][section][option] = config.get(section, option)
    return configuration

def get_project(configuration, project):
    if configuration.has_key(project): return project
    for section in configuration['projects'].keys():
        if configuration['projects'][section].has_key('alias'):
            if configuration['projects'][section]['alias'] == project:
                return section

def execute_command(configuration, project, command, background=False, nohup=False):
    os.chdir(configuration['projects'][project]['directory'])
    if DEFAULT_COMMANDS.has_key(command):
        command = DEFAULT_COMMANDS[command]
    else:
        try:
            command = configuration['projects'][project][command]
            if background:
                command = command + " &"
            if nohup:
                command = "nohup " + command
            os.system(command)
        except KeyError, e:
            sys.stderr.write('Unknown Command: %s\n' % (command))
            command = None
    if command:
        os.system(command)

def set_env_variable(key, value):
    os.system('export %s=%s' %(key, value))
    return value

def main():
    conf = ".werktuig.conf"
    parser = OptionParser()
    parser.add_option("-p", "--project", dest="project", help="Project", metavar="PROJECT")
    parser.add_option("-c", "--command", dest="command", help="Command", metavar="COMMAND")
    parser.add_option("-b", "--batch", dest="batch", help="Batch", metavar="BATCH")
    parser.add_option("--config-editor", dest="config_editor", help="Config Editor", default=False, action="store_true")
    parser.add_option("--config", dest="config", help="Config", metavar="CONFIG")
    (options, args) = parser.parse_args()
    configuration = load_configuration(conf)

    if options.config_editor:
        configuration_editor_run(configuration)
    if options.project:
        os.environ['WERKTUIG_PROJECT'] = set_env_variable('WERKTUIG_PROJECT', options.project)
    project = get_project(configuration, os.environ['WERKTUIG_PROJECT'])

    if options.command:
        execute_command(configuration, project, options.command)
    elif options.batch:
        for project in configuration['projects']:
            execute_command(configuration, project, options.batch, background=True)

if __name__ == '__main__':
    main()
