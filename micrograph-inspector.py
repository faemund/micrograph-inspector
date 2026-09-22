import mrcfile
with mrcfile.open('data/test.mrc') as mrc:
    
    dim = len(mrc.data.shape)
    if dim == 3:
        y = mrc.data.shape[1]
        x = mrc.data.shape[2]
    elif dim == 3:
        y = mrc.data.shape[0]
        x = mrc.data.shape[1]

    print('Height: ', y)
    print('Width: ', x)

    if mrc.is_volume():
        print('File represents: volume.')
    elif mrc.is_image_stack():
        print('File represents: image stack.')
    elif mrc.is_single_image():
        print('File represents: single image.')
    elif mrc.is_volume_stack():
        print('File represents: volume stack.')
    else:
        print('Could not analyze what this file represents')

    print('Voxel size:')
    print('x =', mrc.voxel_size.x, ' Å/px')
    print('y =', mrc.voxel_size.y, ' Å/px')
    print('z =', mrc.voxel_size.z, ' Å/px')
    
