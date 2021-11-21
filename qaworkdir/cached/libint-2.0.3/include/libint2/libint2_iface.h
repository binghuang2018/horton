#ifndef _libint2_libint2iface_h_
#define _libint2_libint2iface_h_

#ifdef __cplusplus
# include <cstddef>
#else
# include <stddef.h>
#endif
#ifdef __cplusplus
extern "C" {
#endif
extern void (*libint2_build_default[8][8][8][8])(const Libint_t*);
extern void (*libint2_build_eri[8][8][8][8])(const Libint_t*);
void libint2_static_init();
void libint2_static_cleanup();
void libint2_init_default(Libint_t* inteval, int max_am, void* buf);
size_t libint2_need_memory_default(int max_am);
void libint2_cleanup_default(Libint_t* inteval);
void libint2_init_eri(Libint_t* inteval, int max_am, void* buf);
size_t libint2_need_memory_eri(int max_am);
void libint2_cleanup_eri(Libint_t* inteval);
#ifdef __cplusplus
};
#endif

/** Use LIBINT2_PREFIXED_NAME(fncname) to form properly prefixed function name from LIBINT2 API */
#define LIBINT2_PREFIXED_NAME(name) __libint2_prefixed_name__(LIBINT2_API_PREFIX,name)
#define __libint2_prefixed_name__(prefix,name) __prescanned_prefixed_name__(prefix,name)
#define __prescanned_prefixed_name__(prefix,name) prefix##name
/** Use LIBINT2_PREFIXED_NAME(fncname) to form properly prefixed function name from LIBINT2 API */
#define LIBINT2_DEFINED(taskname,symbol) __prescanned_libint2_defined__(taskname,symbol)
#define __prescanned_libint2_defined__(taskname,symbol) LIBINT2_DEFINED_##symbol

#endif

