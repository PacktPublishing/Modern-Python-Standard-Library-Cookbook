def function(should_print=False):
    a = 1
    b = 2
    if should_print:
        print('Usually does not execute!')
    return a + b


import trace
import collections


def report_tracing(func, *args, **kwargs):
    outputs = collections.defaultdict(list)
    
    tracing = trace.Trace(trace=False)
    tracing.runfunc(func, *args, **kwargs)
    
    traced = collections.defaultdict(set)
    for filename, line in tracing.results().counts:
        traced[filename].add(line)
    
    for filename, tracedlines in traced.items():
        with open(filename) as f:
            for idx, fileline in enumerate(f, start=1):
                outputs[filename].append((idx, idx in tracedlines, fileline))

    return outputs


def print_traced_execution(tracings):
    for filename, tracing in tracings.items():
        print(filename)
        for idx, executed, content in tracing:
            print('{:04d}{}  {}'.format(idx, 
                                        '+' if executed else ' ', 
                                        content),
                  end='')
        print()


print_traced_execution(
    report_tracing(function)
)

print_traced_execution(
    report_tracing(function, True)
)