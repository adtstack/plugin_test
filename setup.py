setting = {
    'filepath' : __file__,
    'use_db': False, # db 안씀 
    'use_default_setting': True, # default set
    'home_module': None,
    'menu': {
        'uri': __package__,
        'name': 'TEST',
        'list': [
            {
                'uri': 'test',
                'name': '샘플 테스트',
                'list': [
                    {
                        'uri': 'setting',
                        'name': '설정',
                    },
                    {
                        'uri': 'test request',
                        'name': '테스트 요청',
                    },
                    {
                        'uri': 'test list',
                        'name': '테스트 목록',
                    },
                    
                ]
            },
            {
                'uri': 'manual',
                'name': '매뉴얼',
                'list': [
                    {
                        'uri': 'README.md',
                        'name': 'README',
                    },
                ]
            },
            {
                'uri': 'log',
                'name': '로그',
            },
        ]
    },
    'default_route': 'normal',
}

from plugin import *

P = create_plugin_instance(setting)

try:
    from .mod_download import ModuleDownload
    P.set_module_list([ModuleDownload])
except Exception as e:
    P.logger.error(f'Exception:{str(e)}')
    P.logger.error(traceback.format_exc())