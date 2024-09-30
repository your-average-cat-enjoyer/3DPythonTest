import turtle as t
import math as np

faceCoords = [[[-0.5, 0.5, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0]], [[-0.5, 0.5, -2], [-0.5, -0.5, -2], [0.5, -0.5, -2]]]


def _updateRotationMatrices(xAngle, yAngle, zAngle):
    a = np.cos(xAngle)
    b = np.sin(xAngle)
    c = np.cos(yAngle)
    d = np.sin(yAngle)
    e = np.cos(zAngle)
    f = np.sin(zAngle)
    xRotMatrix = [[1, 0, 0], [0, a, -b], [0, b, a]]
    yRotMatrix = [[c, 0, d], [0, 1, 0], [-d, 0, c]]
    zRotMatrix = [[e, -f, 0], [f, e, 0], [0, 0, 1]]
    thetaRotMatrix = _matrixMult(xRotMatrix, yRotMatrix)
    # np.matmul(xRotMatrix,yRotMatrix,zRotMatrix)
    print(thetaRotMatrix)


def _matrixMult(a, b):  # Botched-ass matrix multiplier
    out = [[(a[0] * b[0] + a[1] * b[3] + a[2] * b[6]), (a[0] * b[1] + a[1] * b[4] + a[2] * b[7]),
            (a[0] * b[2] + a[1] * b[5] + a[2] * b[8])],
           [(d * j + e * m + f * p), (d * k + e * n + f * q), (d * l + e * o + f * r)],
           [(g * j + h * m + i * p), (g * k + h * n + i * q), (g * l + h * o + i * r)]]
    return out


def _rotationalTransform(x, y, z, xAngle, yAngle, zAngle):
    transformedCoords = []


_updateRotationMatrices(0, 90, 270)

t.mainloop()
