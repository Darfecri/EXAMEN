def caudal(pwf, qmax, pr):
    qo= ( 1 - (0.2 *(pwf/pr)) - (0.8*(pwf/pr)**2))*(qmax)
    return qo

