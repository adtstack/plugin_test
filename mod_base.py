from .setup import *

name = 'test'

class ModuleBase(PluginModuleBase):
    db_default = {
        f'{name}_db_version' : '1',
    }

    def __init__(self, page, req):
        super(ModuleBase, self).__init__(P, name=name)

        arg = P.ModelSetting.to_dict()
        try:
            return render_template(f'{__package__}_{name}.html', arg=arg)
        except Exception as e: 
            P.logger.error(f'Exception: {str(e)}')
            P.logger.error(traceback.format_exc())
            return render_template('sample.html', title=f'{__package__}/{name}/{page}')
        
    def process_command(self, command, arg1, arg2, arg3, req):
        if command == 'test_module':
            if arg1 == '':
                return arg2
        else:
            if arg2 == '':
                return arg1
