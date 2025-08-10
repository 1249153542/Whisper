#pragma once

// Dummy implementation of the Tracing namespace to allow compilation without the full tracing library.

#include "ggml.h"
#include <string>
#include <vector>

namespace Tracing
{
    inline void delayTensor(const char*, ggml_tensor*) {}
    inline void delayTensor(const std::initializer_list<const char*>&, ggml_tensor*) {}
    inline void writeDelayedTensors() {}
    inline void tensor(const char*, ggml_tensor*) {}
    inline void vector(const char*, const std::vector<float>&) {}
}
