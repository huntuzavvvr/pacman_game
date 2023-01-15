import random
import numpy as np


def find_double_zeros(_ar1, _ar2, x, y):
    _sh = _ar2.shape
    _k = _sh[1]
    if x + _sh[0] - 1 == _ar1.shape[0] or y + _sh[1] - 1 == _ar1.shape[1]:
        _k = -1
    for _i, _elem in enumerate(_ar2):
        for _j, _el in enumerate(_elem[:_k]):
            if _ar1[_i + x][_j + y] == _el == 0:
                _n = 0
                _m = 0
                for __i in range(-1, 2):
                    for __j in range(-1, 2):
                        if _j + __j + y >= _ar1.shape[1]:
                            continue
                        if _ar1[_i + __i + x][_j + __j + y] == _el == 0:
                            _n += 1
                            if _j + y + __j == _ar1.shape[1] - 1:
                                _m += 1
                if _n > 5 or _m > 1:
                    return True
    return False


def revers_ar(_a):
    _k = _a.shape
    _b = np.array(np.zeros(_k[0] * _k[1]).reshape(_k), dtype='int8')
    for i in range(_k[0]):
        _b[i] = _a[_k[0] - i - 1]
    return _b


def find_first_one(_pix_ar):
    for _i in range(31):
        for _j in range(14):
            if _pix_ar[_i, _j] == 1:
                return _i, _j
    return False


def sum_ar(_ar1, _ar2, x=0, y=0):
    try:
        _sh = _ar2.shape
        k = _sh[1]
        if (x + _sh[0] - 1, y + _sh[1] - 1) > _ar1.shape:
            raise IndexError
        if x + _sh[0] - 1 == _ar1.shape[0] or y + _sh[1] - 1 == _ar1.shape[1]:
            k = -1
        for _i, _elem in enumerate(_ar2):
            for _j, _el in enumerate(_elem[:k]):
                if 1 in [_ar1[_i + x][_j + y], _el]:
                    _ar1[_i + x][_j + y] += _el - 1
                elif _ar1[_i + x][_j + y] == _el == 0:
                    pass
                else:
                    raise ValueError
        return True
    except IndexError:
        return False
    except ValueError:
        return False


cent_sym_figures = [
        np.array([[1, 0, 0, 0, 1],
                  [0, 0, 2, 0, 0],
                  [0, 2, 2, 2, 0],
                  [0, 0, 2, 0, 0],
                  [1, 0, 0, 0, 1]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 0],
                  [0, 2, 0, 2, 0],
                  [0, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0],
                  [0, 2, 0],
                  [0, 0, 0]], dtype='int8')
    ]
ax_sym_figures = [
        np.array([[0, 0, 0, 0],
                  [0, 2, 2, 0],
                  [0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 0],
                  [0, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]], dtype='int8')
    ]
none_sym_figures = [
        np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 2, 2, 0, 0, 0],
                  [1, 1, 0, 2, 2, 0, 1, 1],
                  [1, 1, 0, 2, 2, 0, 1, 1],
                  [1, 1, 0, 0, 0, 0, 1, 1]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 2, 2, 0],
                  [1, 1, 1, 0, 2, 2, 0],
                  [1, 1, 1, 0, 2, 2, 0],
                  [1, 1, 1, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
                  [1, 1, 1, 1, 0, 2, 2, 0, 1, 1],
                  [1, 1, 1, 1, 0, 2, 2, 0, 1, 1],
                  [1, 1, 1, 1, 0, 0, 0, 0, 1, 1]], dtype='int8'),
        np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 2, 0, 0, 0, 0, 2, 2, 0],
                  [0, 2, 2, 0, 1, 1, 0, 2, 2, 0],
                  [0, 2, 2, 0, 1, 1, 0, 2, 2, 0],
                  [0, 2, 2, 0, 1, 1, 0, 2, 2, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], dtype='int8')
    ]
all_figures = [*cent_sym_figures]
for elem in [[np.rot90(elem, i) for i in range(2)] for elem in ax_sym_figures]:
    all_figures.extend(elem)
for elem in [[np.rot90(elem, i) for i in range(4)] for elem in none_sym_figures]:
    all_figures.extend(elem)
horizontal_wall_figures = [
        np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], dtype='int8'),
        np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]], dtype='int8'),
    ]
vertical_wall_figures = [
        np.rot90(
            np.array([[1, 2, 2, 2, 2, 2, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 1, 0, 0, 0, 2, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 1, 1],
                      [1, 1, 1, 1, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]],
                     dtype='int8')),
        np.rot90(
            np.array([[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]],
                     dtype='int8'))
    ]
center_fig = np.rot90(np.array([[0, 4, 3, 3, 3, 2, 0],
                                [0, 2, 3, 3, 3, 2, 0],
                                [0, 2, 3, 3, 3, 2, 0],
                                [0, 2, 2, 2, 2, 2, 0],
                                [0, 0, 0, 0, 0, 0, 0]], dtype='int8'), -1)


def generation_lvl(view_print=False):
    pix_ar = np.array(np.ones(14 * 31).reshape(31, 14), dtype='int8')

    # wall generation
    a = sum_ar(pix_ar, random.choice(horizontal_wall_figures), 0, 0)
    b = sum_ar(pix_ar, revers_ar(fig := random.choice([horizontal_wall_figures[2]])), 31 - fig.shape[0],
               14 - fig.shape[1])
    if view_print:
        print(f'horizontal_wall: {a, b}')

    del a, b
    ls_ind = list(range(len(vertical_wall_figures)))
    pix_ar_copy = pix_ar.copy()
    if view_print:
        print('vertical_wall: ', end='')
    while True:
        if sum_ar(pix_ar_copy, vertical_wall_figures[(random.choice(ls_ind))]):
            if view_print:
                print(True)
            pix_ar = pix_ar_copy.copy()
            del pix_ar_copy
            break
        else:
            if view_print:
                print(False, end=', ')
    del ls_ind

    # center_fig generation
    x = sum_ar(pix_ar, center_fig, 11, 9)

    if view_print:
        print(f'center_fig: {x}')
    del x
    # figures generation
    if view_print:
        print('figures generation...')
    ls_found_double_zeros = []
    while coord := find_first_one(pix_ar):
        lst_ok_figures = [[], [], [], []]
        coord = coord[0] - 1, coord[1] - 1

        for _elem in all_figures:
            if sum_ar(pix_ar.copy(), _elem, *coord):
                k = 0
                if x := find_double_zeros(pix_ar, _elem, *coord):
                    k = 3
                elif _elem.size > 56:
                    k = 0
                elif 21 < _elem.size <= 56:
                    k = 1
                elif _elem.size <= 21:
                    k = 2
                ls_found_double_zeros.append(x)
                lst_ok_figures[k].append(_elem)

        for i, ls in enumerate(lst_ok_figures):
            if view_print:
                print(i, end=', ')
                if i == 3:
                    print()
                    print(lst_ok_figures)
            if ls:
                sum_ar(pix_ar, random.choice(ls), *coord)
                break
        if view_print:
            print()

    new_pix_ar = np.array(np.ones(28 * 31).reshape(31, 28), dtype='int8')
    for i, _elem in enumerate(pix_ar):
        new_pix_ar[i] = np.hstack([_elem, _elem[range(13, -1, -1)]])
    if view_print:
        print('final lvl')
        print(new_pix_ar)
    return new_pix_ar


if __name__ == '__main__':
    print(generation_lvl())
