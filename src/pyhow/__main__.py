""" Run pyhow. """

import argparse

from pyhow import make_samples, show_sample


DESCRIPTION_PREFIX = "Select one of the following samples:"


def run():
    """ Parse command line and show the required sample. """

    samples = make_samples()
    space = max(len(name) for name in samples)

    description = DESCRIPTION_PREFIX + ''.join([
        "\n  {:<{}}: {}".format(name, space, module.__doc__.strip().lower())
        for name, module in sorted(samples.items(), key=lambda item: item[0])
    ])

    parser = argparse.ArgumentParser(
        prog='pyhow', description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('sample_name', choices=sorted(samples.keys()))
    args = parser.parse_args()

    show_sample(samples[args.sample_name])


if __name__ == '__main__':
    run()
