import random
import numpy as np


def find_double_zeros(_ar1, _ar2, x, y):
    test_arr = np.hstack([_ar1.copy(), np.zeros(_ar1.shape[0], dtype='int8').reshape(_ar1.shape[0], 1),
                          np.ones(_ar1.shape[0], dtype='int8').reshape(_ar1.shape[0], 1) * 2])
    if not sum_ar(test_arr, _ar2, x, y):
        raise ValueError('error in sum_ar in find_double_zeros')
    num_double_zeros = 0
    for _a in range(_ar2.shape[0]):
        for _b in range(_ar2.shape[1]):
            if test_arr[_a + x, _b + y] in [0, 3, 5]:
                neigh_zeros = np.zeros(9).reshape(3, 3) == 1
                for _x in range(3):
                    for _y in range(3):
                        if _b + y + _y - 1 != _ar1.shape[1]:
                            neigh_zeros[_x, _y] = test_arr[_a + x + _x - 1, _b + y + _y - 1] in [0, 3, 5]
                        else:
                            neigh_zeros[_x, _y] = True
                for _i in range(2):
                    for _j in range(2):
                        if all([all(_elem) for _elem in neigh_zeros[_i:_i + 2, _j:_j + 2]]):
                            num_double_zeros += 1
                            break
    return num_double_zeros


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
                elif _ar1[_i + x][_j + y] == 0 and _el != 2:
                    _ar1[_i + x][_j + y] = _el
                elif _ar1[_i + x][_j + y] in [3, 5] and _el == 0:
                    pass
                elif _ar1[_i + x][_j + y] in [3, 5]:
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
                  [0, 2, 3, 2, 0],
                  [0, 2, 2, 2, 0],
                  [0, 0, 0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0],
                  [0, 2, 0],
                  [0, 0, 0]], dtype='int8'),
        np.array([[0, 0, 0, 0],
                  [0, 2, 2, 0],
                  [0, 2, 2, 0],
                  [0, 0, 0, 0]], dtype='int8')
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
        np.array([[0, 0, 0, 1],
                  [0, 2, 0, 0],
                  [0, 2, 2, 0],
                  [0, 0, 0, 0]], dtype='int8'),
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
                      [1, 1, 0, 5, 0, 2, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 5, 0, 1, 1],
                      [1, 1, 1, 1, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]],
                     dtype='int8')),
        np.rot90(
            np.array([[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 1]],
                     dtype='int8'))
    ]
center_fig = np.rot90(np.array([[3, 4, 3, 3, 3, 2, 3],
                                [3, 2, 3, 3, 3, 2, 3],
                                [3, 2, 3, 3, 3, 2, 3],
                                [3, 2, 2, 2, 2, 2, 3],
                                [3, 3, 3, 3, 3, 3, 3]], dtype='int8'), -1)


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
    while coord := find_first_one(pix_ar):
        lst_ok_figures = [[], [], [], []]
        coord = coord[0] - 1, coord[1] - 1

        for _elem in all_figures:
            if sum_ar(pix_ar.copy(), _elem, *coord):
                k = 4
                if find_double_zeros(pix_ar.copy(), _elem, *coord):
                    k = 3
                elif _elem.size >= 56:
                    k = 0
                elif 21 < _elem.size < 56:
                    k = 1
                elif _elem.size <= 21:
                    k = 2
                lst_ok_figures[k].append(_elem)

        for i, ls in enumerate(lst_ok_figures):
            if i == 3:
                print((coord, pix_ar, ls))
                return -1
            if ls:
                sum_ar(pix_ar, random.choice(ls), *coord)
                break
    new_pix_ar = np.array(np.ones(28 * 31).reshape(31, 28), dtype='int8')
    for i, _elem in enumerate(pix_ar):
        new_pix_ar[i] = np.hstack([_elem, _elem[range(13, -1, -1)]])
    if view_print:
        print('final lvl')
        print(new_pix_ar)
    return new_pix_ar


if __name__ == '__main__':
    generation_lvl(view_print=True)
