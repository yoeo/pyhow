"""pyhow module

Print show Python sample codes.

"""

import inspect
import itertools
import os
import pydoc
import sys

import pyhow.samples


_CATEGORY_TAG = "# category: "

_TEMPLATE_PREFIX = """
>>> {module_doc}


"""

_CATEGORY_TEMPLATE = """{step} {category}


{methods}
"""

_STEP_TEMPLATE = "{current_category}/{nb_categories}"

_METHOD_TEMPLATE = """  {method_upper}: {doc}
    |
{codelines}
    |
    |-- {method}() = {result!r}


"""

_CODELINE_TEMPLATE = "    |  {codeline}"


def make_samples():
    """Prepare sample modules."""

    root = 'pyhow.samples.'
    return {
        name[len(root):]: module for name, module in sys.modules.items() if (
            name.startswith(root) and
            not os.path.basename(module.__file__).startswith('_'))
    }


def _bold(text):
    """Format a string in bold by overstriking."""
    return ''.join(ch + '\b' + ch for ch in text)


def _underline(text):
    """Format a string by overstriking."""
    return ''.join('_' + '\b' + ch for ch in text)


def _extract_methods_info(module):
    """Extract methods data from a given python modules."""

    categories = [('uncategorized', -1)]
    categories += [
        (line.strip().replace(_CATEGORY_TAG, ''), line_number)
        for line_number, line in enumerate(inspect.getsourcelines(module)[0])
        if line.strip().startswith(_CATEGORY_TAG)]

    methods = [getattr(module, name) for name in dir(module)]
    methods = [method for method in methods if (
        callable(method) and hasattr(method, '__module__') and
        method.__module__ == module.__name__ and method.__name__ != 'run')]
    methods_info = []
    for method in methods:
        codelines, line_number = inspect.getsourcelines(method)
        methods_info.append({
            'name': method.__name__,
            'doc': method.__doc__.strip() if method.__doc__ else '',
            'codelines': [
                line for line in codelines if line.strip() and
                '"""' not in line],
            'method': method,
            'category': [
                category_name for category_name, category_line_number in
                categories if line_number > category_line_number][-1],
        })
    return methods_info


def show_sample(module):
    """Print sample modules."""

    methods_info = _extract_methods_info(module)
    methods_info = sorted(methods_info, key=lambda x: x['name'])
    methods_info = sorted(methods_info, key=lambda x: x['category'])

    grouped_catergories = itertools.groupby(
        methods_info, key=lambda x: x['category'])

    text = _TEMPLATE_PREFIX.format(module_doc=_bold(module.__doc__.upper()))
    nb_categories = len(set(
        method_info['category'] for method_info in methods_info))
    for current_category, (category_name, category_methods_info) in enumerate(
            grouped_catergories):

        methods_text = ''
        for method_info in category_methods_info:

            codelines_text = ''
            for line in method_info['codelines']:
                codelines_text += _CODELINE_TEMPLATE.format(codeline=line)

            methods_text += _METHOD_TEMPLATE.format(
                method_upper=_bold(method_info['name'].upper()),
                method=_bold(method_info['name']),
                doc=_bold(method_info['doc']),
                result=method_info['method'](),
                codelines=codelines_text.rstrip())

        text += _CATEGORY_TEMPLATE.format(
            step=_bold(_STEP_TEMPLATE.format(
                current_category=current_category+1,
                nb_categories=nb_categories)),
            category=_underline(category_name.upper()),
            methods=methods_text)

    pydoc.getpager()(text)
