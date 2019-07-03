CC = g++
CFLAGS = -g -Wall
SRCS = concurso.cpp
PROG = aula

OPENCV = `pkg-config opencv --cflags --libs`
LIBS = $(OPENCV)

$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
