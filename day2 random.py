import numpy as np

def drawsamples(pmf, number_of_samples):
    a = 0
    cmf = {}
    samples = []
    for (k, v) in pmf.items():
        a=v+a
        cmf[k] = a
    print(cmf)
    for _ in range(number_of_samples):
        rand = np.random.uniform(0, 1)
        flag = 0
        print(rand)
        for k in cmf:
            if rand < cmf[k] and not flag:
                samples.append(k)
                flag = 1
    return samples
pmf = {"ABCD": 0.03703704,"EFGH": 0.07407407,"IJKL": 0.14814815,"MNOP": 0.22222222,"QRST": 0.40740741,"UVWXYZ": 0.1111111}
print(drawsamples(pmf, 1))
