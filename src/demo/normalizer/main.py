# encoding: utf-8

u'''Command-line utility for the demo normalizer'''

import sys
from plone.i18n.normalizer import IDNormalizer

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 2:
        print >>sys.stderr, 'Usage: {} NAME'.format(argv[0])
    normalizer = IDNormalizer()
    print normalizer.normalize(argv[1])


if __name__ == '__main__':
    main(sys.argv)
