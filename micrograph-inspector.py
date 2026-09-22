import mrcfile
with mrcfile.open('data/test.mrc') as mrc:
    
    dim = len(mrc.data.shape)
    if dim == 3:
        y = mrc.data.shape[1]
        x = mrc.data.shape[2]

    else:
        y = mrc.data.shape[0]
        x = mrc.data.shape[1]

    print('Height: ', y)
    print('Width: ', x)
    
