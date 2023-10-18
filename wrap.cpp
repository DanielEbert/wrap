#include <iostream>
#include <vector>
#include <sys/stat.h>
#include <cstdlib>
#include <cstring>
#include <unistd.h>

// TODO: update
const char* HFUZZ_CXX = "/home/user/Downloads/honggfuzz/hfuzz_cc/hfuzz-g++";
const char* HFUZZ_CC = "/home/user/Downloads/honggfuzz/hfuzz_cc/hfuzz-gcc";

bool file_exists(std::string filepath)
{
    struct stat s;
    return stat(filepath.c_str(), &s) == 0;
}

int main(int argc, char* argv[])
{
    std::string argv0_real = std::string(argv[0]) + "_real";

    if (file_exists(argv0_real))
    {
        setenv("HFUZZ_CXX_PATH", argv0_real.c_str(), 1);
        setenv("HFUZZ_CC_PATH", argv0_real.c_str(), 1);
    }

    // Call hfuzz-cc with an argv[0] that includes either '-gcc' or '-g++'
    // so that hfuzz-cc uses gcc flags.
    std::vector<char*> hfuzz_args;

    bool is_cxx = std::string(argv[0]).find("++") != std::string::npos;
    if (!is_cxx)
    {
        hfuzz_args.push_back(strdup("hfuzz-gcc"));
        hfuzz_args.insert(hfuzz_args.end(), argv + 1, argv + argc);
        execvp(HFUZZ_CC, &hfuzz_args[0]);
        perror("Failed to execute HFUZZ_CC: ");
        hfuzz_args.clear();
    }

    hfuzz_args.push_back(strdup("hfuzz-g++"));
    hfuzz_args.insert(hfuzz_args.end(), argv + 1, argv + argc);
    execvp(HFUZZ_CXX, &hfuzz_args[0]);
    perror("Failed to execute HFUZZ_CXX: ");

    return 0;
}