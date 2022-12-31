import sys

__all__ = [
        'mgmt',
        'secrets'
        ]

def main(args=None):
    compatible = True
    if sys.version_info < (3, 7):
        compatible = False
    elif not hasattr(sys, 'base_prefix'):
        compatible = False
    if not compatible:
        raise ValueError('This script is only for use with Python >= 3.8')
    else:
        import argparse
        parser = argparse.ArgumentParser(
                prog=__name__,
                description='Creates virtual Python '
                            'environments in one or '
                            'more target '
                            'directories.',
                epilog='Once an environment has been '
                        'created, you may wish to '
                        'activate it, e.g. by '
                        'sourcing an activate script '
                        'in its bin directory.'
                )

    print("main() was executed")

def setup():
    pass
    

