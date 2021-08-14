FROM debian:10

RUN apt-get update \
  && apt-get install -y build-essential gcc g++ clang \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# RUN apt-get update
# RUN apt-get install swig
# RUN swif -python calculate.i
# RUN gcc -c -fpic calculate_wrap.c calculate.c -I/use/include/python2.7.10
# RUN gcc -shared calculate.o calculate_wrap.o -o _calculate.so
RUN g++ -fPIC -shared -o app/calculate.so app/calculate.cpp

# RUN g++ -fPIC -shared -o app/calc.so app/calc.cpp
#RUN clang -Wall -o hello hello-world/hello.c
#RUN g++ -Wall -o hello hello-world/hello.cpp
#RUN clang++ -Wall -o hello hello-world/hello.cpp

# CMD ./hello

# RUN g++ -fPIC -g -c -Wall app/calc.cpp
# RUN g++ -shared -o app/calc.so 