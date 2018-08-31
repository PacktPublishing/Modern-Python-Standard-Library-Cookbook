import shutil, sys

def withprogressbar(func):
    """Decorates ``func`` to display a progress bar while running.

    The decorated function can yield values from 0 to 100 to
    display the progress.
    """
    def _func_with_progress(*args, **kwargs):
        max_width, _ = shutil.get_terminal_size()

        gen = func(*args, **kwargs)
        while True:
            try:
                progress = next(gen)
            except StopIteration as exc:
                sys.stdout.write('\n')
                return exc.value
            else:
                # Build the displayed message so we can compute
                # how much space is left for the progress bar itself.
                message = '[%s] {}%%'.format(progress)
                bar_width = max_width - len(message) + 3  # Add 3 characters to cope for the %s and %%

                filled = int(round(bar_width / 100.0 * progress))
                spaceleft = bar_width - filled
                bar = '=' * filled + ' ' * spaceleft
                sys.stdout.write((message+'\r') % bar)
                sys.stdout.flush()

    return _func_with_progress
import time

@withprogressbar
def wait(seconds):
    """Waits ``seconds`` seconds and returns how long it waited."""
    start = time.time()
    step = seconds / 100.0
    for i in range(1, 101):
        time.sleep(step)
        yield i  # Send % of progress to withprogressbar

    # Return how much time passed since we started,
    # which is in fact how long we waited for real.
    return time.time() - start

print('WAITED', wait(5))
