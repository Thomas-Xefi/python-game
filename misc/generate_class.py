import importlib


def auto_generate_class(tabAttributes, moduleName, className):
    results = []
    module = importlib.import_module(moduleName)
    for attributes in tabAttributes:
        newClass = getattr(module, className)()
        dictClass = newClass.__dict__.copy()
        for attribute in attributes:
            for key in dictClass.keys():
                newClass.__dict__[key] = attribute
                del dictClass[key]
                break
        results.append(newClass)
    return results
