# Data4Life_Challenge

I had never before done anything with Python Multithreading, but took it as a challenge to implement it in Python and not in C#, although I already have experience in parallelization in C#.
So, naturally I would try out different things.

The commits "**First Version**" and "**Second Version**" show an implementation where I tried to implement the management process of how many threads can be there at the same time by hand. I unfortunately was not able to successfully implement this, the amount of threads would always eat away my resources.

On the commit "**ThreadPoolExecutor**" I tried out the concurrent api provided by Python. This way of doing things bags the problem, that you have to specify how many tasks can be run paralell. This leads to a application that is not working at its most potential, since the number of threads is restricted. On the other side setting the number of threads high, could again eat away all resources and crash the program.

On the commit "**Implimented AsyncIO**" I implemented the asyncIO api, which is also provided by python. This api allows me to instantiate as many threads as possible and manages the resource handling by its self.

I tested the implementation with 12000 email adresses and it takes about 2 seconds
