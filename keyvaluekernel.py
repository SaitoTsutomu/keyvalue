from ipykernel.kernelbase import Kernel

class KeyValue(Kernel):
    implementation = 'KeyValue'
    implementation_version = '0.1'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'name': 'KeyValue', 'mimetype': 'text/plain'}
    banner = 'Dictionry of Key, Value'
    _d = {}
    def do_execute(self, code, silent, store_history=True,
             user_expressions=None, allow_stdin=False):
        s = code.strip()
        if not silent:
            if s.startswith('?'):
                c = {'name': 'stdout', 'text': ' '.join(KeyValue._d.keys())}
            else:
                ss = s.split(maxsplit=1)
                if len(ss) == 1:
                    if s in KeyValue._d:
                        c = {'name': 'stdout', 'text': KeyValue._d[s]}
                    else:
                        c = {'name': 'stderr', 'text': 'Not found'}
                else:
                    KeyValue._d[ss[0]] = ss[1]
                    c = {'name': 'stdout', 'text': ss[1]}
            self.send_response(self.iopub_socket, 'stream', c)
        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
    def do_complete(self, code, cursor_pos):
        s = code[:cursor_pos]
        return {'status': 'ok', 'matches': [k for k in KeyValue._d if k.startswith(s)],
                'cursor_start': cursor_pos, 'cursor_end': -1, 'metadata': {}}

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=KeyValue)