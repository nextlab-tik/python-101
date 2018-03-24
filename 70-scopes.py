"""
Advanced: scopes and namespaces
"""

# import self
import __main__


# scopes
e = 1

def scope1():
    e = 2
    print('scope1', e)

    def scope2():
        global e
        e = 3
        print('scope2', e)

    scope2()
    print('scope1', e)


print('scope0', e)
scope1()
print('scope0', e)


# Try block execution logic
def funct(store):
    store['key_a'] = 'value_a'
    store['key_b'] = 'value_b'
    e = 1
    try:
        print("try with return")
        store['key_c'] = 'value_c'
        e = 2
        return e
    except Exception:
        print('catch exception')
        e = 6
    else:
        print('try else')
        e = 5
    finally:
        print("try finally")
        e = 3
        del store['key_a']
        del store['key_c']
        return e


store = {}
ret = funct(store)
print(ret)
print(store)
