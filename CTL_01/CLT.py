import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import seaborn as sns
import argparse
parser = argparse.ArgumentParser(description="CTL")
parser.add_argument('--counts',default=10000,type=int, help='numbers of Sn')
parser.add_argument('--n',default=30,type=int, help='numbers of sample points')
parser.add_argument('--distribution',default='u',type=str, help='distribution of samples (u for uniform, nm for normal, t for student t)')
parser.add_argument('--tn',default=5,type=int, help='df of distribution of standard_t')
opt = parser.parse_args()
if opt.distribution == 'u':
    a = []
    for i in range(opt.counts):
        Sn_ = 0
        Wn = 0    
        for _ in range(opt.n):
            n_ = np.random.uniform(0,1,1)
            Sn_ = Sn_ + n_
        Wn = (Sn_-0.5*opt.n)/math.sqrt(opt.n/12)
        a.append(Wn)
        a_ = np.array(a)


    x = np.random.normal(size=100000)
    sns.distplot(x,hist=False,label="normal")

    sns.distplot(a_,label="uniform(0,1)")
    plt.savefig("u_n{}_counts{}.png".format(opt.n,opt.counts))
    plt.show()

if opt.distribution == 'nm':
    a = []
    for i in range(opt.counts):
        Sn_ = 0
        Wn = 0    
        for _ in range(opt.n):
            n_ = np.random.standard_normal(size=1)
            Sn_ = Sn_ + n_
        Wn = (Sn_-0)/math.sqrt(opt.n)
        a.append(Wn)
        a_ = np.array(a)


    x = np.random.normal(size=100000)
    sns.distplot(x,hist=False,label="normal")

    sns.distplot(a_,label="normal(0,1)")
    plt.savefig("n_n{}_counts{}.png".format(opt.n,opt.counts))
    plt.show()

if opt.distribution == 't':
    a = []
    for i in range(opt.counts):
        Sn_ = 0
        Wn = 0    
        for _ in range(opt.n):
            n_ = np.random.standard_t(opt.tn,1)
            Sn_ = Sn_ + n_
        Wn = (Sn_)/math.sqrt(opt.n * ( opt.tn / (opt.tn-2)))
        a.append(Wn)
        a_ = np.array(a)


    x = np.random.normal(size=100000)
    sns.distplot(x,hist=False,label="normal")

    sns.distplot(a_,label="standard_tn")
    plt.savefig("t{}_n{}_counts{}.png".format(opt.tn,opt.n,opt.counts))
    plt.show()
