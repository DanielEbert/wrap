all:
	g++ wrap.cpp -std=c++17 -o wrap && ./wrap myfile.cpp
