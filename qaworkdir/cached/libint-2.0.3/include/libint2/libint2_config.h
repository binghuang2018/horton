/* include/libint2_config.h.  Generated from libint2_config.h.in by configure.  */
/* include/libint2_config.h.  Generated from libint2_config.h.in by configure.  */

/* This file is automatically processed by configure script.
   It MUST NOT be changed manually after configuration, otherwise
   the library will likely fail to compile or produce erroneous results
 */

#ifndef _libint2_include_libint2config_h_
#define _libint2_include_libint2config_h_

/* The host architecture. */
#define LIBINT_HOST_ARCH "x86_64-apple-darwin12.3.0"

/* The target architecture. */
#define LIBINT_TARGET_ARCH "x86_64-apple-darwin12.3.0"

/* The version number. */
#define LIBINT_VERSION "2.0.3-stable"

/* The major version number. */
#define LIBINT_MAJOR_VERSION 2

/* The minor version number. */
#define LIBINT_MINOR_VERSION 0

/* The micro version number. */
#define LIBINT_MICRO_VERSION 3

/* Prefix for all names in API */
/* #undef LIBINT_API_PREFIX */

/* Max AM */
#define LIBINT_MAX_AM 7

/* Max optimized AM */
#define LIBINT_OPT_AM 4

/* Support 1-body derivatives up to this order */
/* #undef INCLUDE_ONEBODY */

/* Support ERI derivatives up to this order */
#define INCLUDE_ERI 0

/* Support 3-center ERI derivatives up to this order */
/* #undef INCLUDE_ERI3 */

/* Support 2-center ERI derivatives up to this order */
/* #undef INCLUDE_ERI2 */

/* Support G12 derivatives up to this order */
/* #undef INCLUDE_G12 */

/* Support G12DKH derivatives up to this order */
/* #undef INCLUDE_G12DKH */

/* Max AM for one-body ints */
/* #undef ONEBODY_MAX_AM */

/* Max optimized AM for one-body ints */
/* #undef ONEBODY_OPT_AM */

/* Max AM for ERI (same for all derivatives; if not defined see ERI_MAX_AM_LIST) */
/* #undef ERI_MAX_AM */

/* Max AM for ERI and its derivatives */
/* #undef ERI_MAX_AM_LIST */

/* Max optimized AM for ERI (same for all derivatives; if not defined see ERI_OPT_AM_LIST) */
/* #undef ERI_OPT_AM */

/* Max optimized AM for ERI and its derivatives */
/* #undef ERI_OPT_AM_LIST */

/* Max AM for 3-center ERI (same for all derivatives; if not defined see ERI3_MAX_AM_LIST) */
/* #undef ERI3_MAX_AM */

/* Max AM for 3-center ERI and its derivatives */
/* #undef ERI3_MAX_AM_LIST */

/* Max optimized AM for 3-center ERI (same for all derivatives; if not defined see ERI3_OPT_AM_LIST) */
/* #undef ERI3_OPT_AM */

/* Max optimized AM for 3-center ERI and its derivatives */
/* #undef ERI3_OPT_AM_LIST */

/* If 1, assume will transform the "unpaired" center (e.g. a in (a|cd)) to solid harmonics */
/* #undef ERI3_PURE_SH */

/* Max AM for 2-center ERI (same for all derivatives; if not defined see ERI2_MAX_AM_LIST) */
/* #undef ERI2_MAX_AM */

/* Max AM for 2-center ERI and its derivatives */
/* #undef ERI2_MAX_AM_LIST */

/* Max optimized AM for 2-center ERI (same for all derivatives; if not defined see ERI2_OPT_AM_LIST) */
/* #undef ERI2_OPT_AM */

/* Max optimized AM for 2-center ERI and its derivatives */
/* #undef ERI2_OPT_AM_LIST */

/* If 1, assume will transform to solid harmonics */
/* #undef ERI2_PURE_SH */

/* Max AM for G12 method integrals */
/* #undef G12_MAX_AM */

/* Max optimized AM for G12 method integrals */
/* #undef G12_OPT_AM */

/* Support [Ti,G12] ? */
/* #undef SUPPORT_T1G12 */

/* Max AM for G12DKH method integrals */
/* #undef G12DKH_MAX_AM */

/* Max optimized AM for G12DKH method integrals */
/* #undef G12DKH_OPT_AM */

/* Whether integral sets can be unrolled */
/* #undef LIBINT_ENABLE_UNROLLING */

/* Whether generic code can be used */
#define LIBINT_ENABLE_GENERIC_CODE 1

/* maximum length of vectors */
/* #undef LIBINT_VECTOR_LENGTH */

/* how to vectorize */
/* #undef LIBINT_VECTOR_METHOD */

/* if can be controlled with posix_memalign, alignment size */

/* Specifies the ordering of cartesian Gaussians in a shell. Allowed values are defined at the bottom of this file -- also see configure.in*/
#define LIBINT_CGSHELL_ORDERING 1

/* Specifies the class of shell sets generated. Allowed values are defined at the bottom of this file -- also see configure.in*/
#define LIBINT_SHELL_SET 1

/* User-defined real type */

/*Generate FMA instructions? */
/* #undef LIBINT_GENERATE_FMA */

/* Accumulate integrals to the buffer? */
/* #undef LIBINT_ACCUM_INTS */

/* Whether FLOP counting is supported */
/* #undef LIBINT_FLOP_COUNT */

/* Support contracted integrals? */
#define LIBINT_CONTRACTED_INTS 1

/* Generate single evaluator type? */
#define LIBINT_SINGLE_EVALTYPE 1

/* Generate composite evaluators? */
#define LIBINT_USE_COMPOSITE_EVALUATORS 1

/* Strategy for ERI evaluation */
#define LIBINT_ERI_STRATEGY 1

/* --------------------------
  have C++ features?
   -------------------------- */
// see lib/autoconf/ac_check_cpp11.m4

#define HAVE_CXX11 1
#define HAVE_CXX11_LAMBDA 1
/* #undef HAVE_CXX11_ALIGN */

/* define if array has fill member function. */
/* #undef LIBINT_ARRAY_HAS_FILL */

/* define if std::array is available. */
/* #undef LIBINT_HAS_STD_ARRAY */

/* define if std::make_shared and std::allocate_shared are available. */
/* #undef LIBINT_HAS_STD_MAKE_SHARED */

/* define if std::shared_ptr is available. */
/* #undef LIBINT_HAS_STD_SHARED_PTR */

/* define if std::tr1::array is available. */
#define LIBINT_HAS_STD_TR1_ARRAY 1

/* define if std::tr1::shared_ptr is available. */
#define LIBINT_HAS_STD_TR1_SHARED_PTR 1

/* define if std::tr1 type traits are available. */
#define LIBINT_HAS_STD_TR1_TYPE_TRAITS 1

/* define if std type traits are available. */
/* #undef LIBINT_HAS_STD_TYPE_TRAITS */

/* define if Libint is using <array>. */
/* #undef LIBINT_USE_ARRAY */

/* define if Libint is using <boost/tr1/array.hpp>. */
#define LIBINT_USE_BOOST_TR1_ARRAY_HPP 1

/* define if Libint is using <boost/tr1/memory.hpp>. */
#define LIBINT_USE_BOOST_TR1_MEMORY_HPP 1

/* define if Libint is using <boost/tr1/type_traits.hpp>. */
#define LIBINT_USE_BOOST_TR1_TYPE_TRAITS_HPP 1

/* define if Libint is using <memory>. */
/* #undef LIBINT_USE_MEMORY */

/* define if Libint is using <tr1/array>. */
/* #undef LIBINT_USE_TR1_ARRAY */

/* define if Libint is using <tr1/memory>. */
/* #undef LIBINT_USE_TR1_MEMORY */

/* define if Libint is using <tr1/type_traits>. */
/* #undef LIBINT_USE_TR1_TYPE_TRAITS */

/* define if Libint is using <type_traits>. */
/* #undef LIBINT_USE_TYPE_TRAITS */

/* C++ compiler allows template with default params as template template parameter */
/* #undef CXX_ALLOWS_DEFPARAMTEMPLATE_AS_TEMPTEMPPARAM */

/* is shared_ptr in boost? */
#define HAVE_SHARED_PTR_IN_BOOST 1

/*
  Known orderings of cartesian functions
*/
#define LIBINT_CGSHELL_ORDERING_STANDARD 1
#define LIBINT_CGSHELL_ORDERING_INTV3 2
#define LIBINT_CGSHELL_ORDERING_GAMESS 3
#define LIBINT_CGSHELL_ORDERING_ORCA 4
#define LIBINT_CGSHELL_ORDERING_BAGEL 5
/*
  Known sets of shell sets
*/
#define LIBINT_SHELL_SET_STANDARD 1
#define LIBINT_SHELL_SET_ORCA 2

/*
 Libint-independent features
 */

/* have stdint.h ? */
#define HAVE_STDINT_H 1

/* have MPFR library ? */
/* #undef HAVE_MPFR */

/* have posix_memalign ? */

#endif // header guard
/* EXTRA DEFINES DETERMINED BY CONFIGURE OF THE EXPORTED LIBRARY */
#ifndef _libint2_include_libint2config_h_1
#define _libint2_include_libint2config_h_1
#define LIBINT2_ALIGN_SIZE 0
#define HAVE_POSIX_MEMALIGN 1
#define LIBINT2_REALTYPE double
#endif // header guard #2
