#include <cstdarg>
#include <cstdio>

// Dummy implementations of logging functions to allow compilation without the full logger library.

// Define char8_t for C++ standards before C++20
#if __cplusplus < 202002L
typedef char char8_t;
#endif

extern "C" {

void logError( const char8_t* pszFormat, ... ) {
    // Empty implementation
}

void logWarning( const char8_t* pszFormat, ... ) {
    // Empty implementation
}

void logInfo( const char8_t* pszFormat, ... ) {
    // Empty implementation
}

void logDebug( const char8_t* pszFormat, ... ) {
    // Empty implementation
}

}
